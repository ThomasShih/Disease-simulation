from tools.dataSet import dataSet
from tools.disease import disease
from tools.cycleStep import timeStep
import numpy as np
import pandas as pd
from tqdm import tqdm

class attributes:
    def __init__(self):
        self.individual = {
            "pResistanceOffset" :np.round(np.linspace(0,2,21),1), #how careful is someone from trying not to get infected?
            "pInfectorOffset"   :np.round(np.linspace(0,2,21),1), #how careful is someone from infecting other if infected?
            "age"               :range(0,80,1),
            "status"            :["susceptible"],
            "status_enlapsed"   :[0], #how long has it been since the last status has changed?
            "x_coord"           :range(0,10,1),
            "y_coord"           :range(0,10,1),
        } 

        self.population = {
            "populationSize" : 100,
        }

        self.disease = {
            "name"              : "disease",
            "immunityChance"    : 0.1,  #What are the chances that someone is already immune
            #What is the proflie of people being able to infect, and when they are symptomatic?
            "contagious" : list(map(bool,[0,0,0,0,1,1,1,1,1,1])),
            "symptomatic": list(map(bool,[0,0,0,0,0,0,1,1,1,1])),
            "mortality"         :.02,   #How likely is someone to die at the end of the disease
            "reproductionValue" : 1,    #How likely the disease is to spread between people at a distance of one meter for one time unit
        }

        self.summaryRename = {
            "immune"   : "removed",
            "deceased" : "removed",
            "recovered": "removed",
        }

class simulation(timeStep):
    def __init__(self):
        #import required resources
        self.attributes = attributes()
        self.disease = disease(self.attributes)
        self.data = dataSet(self.attributes)
        self.summary = pd.DataFrame(columns = ["susceptible","infected","removed","newlyInfected"])

        #intialize the simulation
        self.data.generate()
        self.data.initialize()

        #start simulation
        for i in tqdm(range(40),desc="Simulating Disease"):
            self.nextCycle(i)

        #print summary
        self.summary["newlyInfected"] = (self.summary["infected"] - self.summary["infected"].shift(fill_value=0)).astype(int)
        print(self.summary)


if __name__ == "__main__":
    sim = simulation()