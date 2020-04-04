from tools.dataSet import dataSet
from tools.disease import disease
from tools.cycleStep import timeStep
import tools.attributes as attributes
import pandas as pd
from tqdm import tqdm

class simulation(timeStep):
    def __init__(self):
        #import required resources
        self.disease = disease(attributes)
        self.data = dataSet(attributes)
        self.summary = pd.DataFrame(columns = attributes.summaryColumns)

    def initialize(self):
        #intialize the simulation
        self.data.generate()
        self.data.initialize()

    def start(self):
        #start simulation
        for i in tqdm(range(attributes.simulation["cycles"]),desc="Simulating Disease"):
            self.nextCycle(i)

    def summarizeSimulation(self):
        #print summary
        self.summary["newlyInfected"] = (self.summary["infected"] - self.summary["infected"].shift(fill_value=0)).astype(int)
        print(self.summary)


if __name__ == "__main__":
    sim = simulation()

    sim.initialize()

    sim.start()

    sim.summarizeSimulation()