import random
import pandas as pd
import numpy as np
from tqdm import tqdm

class timeStep:
    def __init__(self):
        pass

    def removals(self):
        pass

    def infectIndividuals(self):
        pass

    def movement(self):
        pass

    def nextCycle(self):
        self.removals() #Infected individuals would either die or recover once they have reached the end of their illness, remove them from being infectious
        self.infectIndividuals() #Calculate which individuals would be infected for this timestep
        self.movement() #People travel around, calculate whom will travel and how far