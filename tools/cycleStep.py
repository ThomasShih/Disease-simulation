import random
import pandas as pd
import numpy as np
from tqdm import tqdm

class timeStep:
    def removals(self):
        pass

    def infectIndividuals(self):
        """Calculate which individuals should be infected this cycle"""

        contaigousDataSet = self.disease.getContagiousIndividuals(self.data())
        suspectibleIndividuals = self.data().status == "susceptible"
        self.data.data[suspectibleIndividuals] = self.data()[suspectibleIndividuals]\
                                                .apply(lambda x: self.disease.chanceToBeInfected(x,contaigousDataSet=contaigousDataSet),axis=1)
        return

    def movement(self):
        pass

    def summarize(self,cycleID):
        snapShot = self.data.data["status"].value_counts()\
                       .rename(self.attributes.summaryRename).rename("Day " + str(cycleID))
        self.summary = self.summary.append(snapShot)
        return

    def nextCycle(self,cycleID):
        self.removals() #Infected individuals would either die or recover once they have reached the end of their illness, remove them from being infectious
        self.infectIndividuals() #Calculate which individuals would be infected for this timestep
        self.movement() #People travel around, calculate whom will travel and how far
        self.summarize(cycleID) #The actual data file will likely be too hard to interperet, therefore make a summary of the file
        self.data.data["status_enlapsed"] = self.data()["status_enlapsed"] + 1

        return