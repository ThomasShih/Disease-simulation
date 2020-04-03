from tools.dataSet import dataSet
from tools.disease import disease
from tools.cycleStep import timeStep
import numpy as np

class attributes:
    def __init__(self):
        self.individual = {
            "pResistanceOffset" :np.round(np.linspace(0,2,21),1), #how careful is someone from trying not to get infected?
            "pInfectorOffset"   :np.round(np.linspace(0,2,21),1), #how careful is someone from infecting other if infected?
            "age"               :range(0,80,1),
            "status"            :["uninfected"],
            "x_coord"           :range(0,100,1),
            "y_coord"           :range(0,100,1),
        } 

        self.population = {
            "populationSize" : 100,
        }

        self.disease = {
            "name"              : "disease",
            "immunityChance"    : 0.1,  #What are the chances that someone is already immune
            "incubation"        : 4,    #How long does a virus incubate before being symptomatic
            "symptomatic"       : 4,    #How long is someone able to have symptoms
            "infectious"        : 6,    #How long is someone able to infect others
            "mortality"         :.02,   #How likely is someone to die
            "reproductionValue" : 1,    #How likely the disease is to spread between people at a distance of one meter for one time unit
        }

class simulation(timeStep):
    def __init__(self):
        self.attributes = attributes()
        self.disease = disease(self.attributes)
        self.data = dataSet(self.attributes)
        self.data.generate()
        self.data.initialize()

        print(self.data)

if __name__ == "__main__":
    sim = simulation()