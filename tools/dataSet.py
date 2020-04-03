import random
import pandas as pd
import numpy as np
from tqdm import tqdm

class dataSet:
    def __init__(self,length=100):
        self.length = length
        self.individualAttributes = {
            "pResistanceOffset" :np.round(np.linspace(0,2,21),1), #how careful is someone from trying not to get infected?
            "pInfectorOffset"   :np.round(np.linspace(0,2,21),1), #how careful is someone from infecting other if infected?
            "age"               :range(0,80,1),
            "status"            :["uninfected"],
            "x_coord"           :range(0,100,1),
            "y_coord"           :range(0,100,1),
        } 
        self.populationAttributes = {
            "immunityChance" : 0.05,
        }

    def __str__(self):
        try: return self.data.__str__()
        except: print("data has not yet been generated")
        return
    
    def display(self):
        try: print(self.data)
        except: print("data has not yet been generated")
        return

    def generate(self):
        """Generates a random dataset with a series of attributes"""
        self.data = pd.DataFrame(columns=list(self.individualAttributes.keys()))

        for _ in tqdm(range(self.length),desc="Generating Random Dataset"):
            self.data = self.data.append(dict((item,random.choice(self.individualAttributes[item])) for item in self.individualAttributes)\
                        ,ignore_index=True)
        return

    def initialize(self):
        """applies certain intial parameters to a model"""
        self.data["status"] = self.data.apply(\
                                        lambda x: "immune" if random.random() <= self.populationAttributes["immunityChance"] else x["status"]\
                                        ,axis=1)
        return

if __name__ == "__main__":
    data = dataSet(100)
    data.generate()
    data.initialize()
    print(data)