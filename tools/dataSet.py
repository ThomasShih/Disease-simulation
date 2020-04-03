import random
import pandas as pd
from tqdm import tqdm

class dataSet:
    def __init__(self,attributes):
        self.attributes = attributes

    def __str__(self):
        try: return self.data.__str__()
        except: "data has not yet been generated"
        return

    def __repr__(self):
        try: return self.data.__str__()
        except: "data has not yet been generated"
        return

    def display(self):
        print(True)
        try: print(self.data)
        except: print("data has not yet been generated")
        return

    def generate(self):
        """Generates a random dataset with a series of attributes"""
        self.data = pd.DataFrame(columns=list(self.attributes.individual.keys()))

        for _ in tqdm(range(self.attributes.population["populationSize"]),desc="Generating Random Dataset"):
            self.data = self.data.append(dict((item,random.choice(self.attributes.individual[item])) for item in self.attributes.individual)\
                        ,ignore_index=True)
        return

    def initialize(self):
        """applies certain intial parameters to a model"""
        self.data["status"] = self.data.apply(\
                                        lambda x: "immune" if random.random() <= self.attributes.disease["immunityChance"] else x["status"]\
                                        ,axis=1)
        return

if __name__ == "__main__":
    data = dataSet(100)
    data.generate()
    data.initialize()
    print(data)