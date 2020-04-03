from math import sqrt
import random

def booleanFromProbability(probability):
    """Generates a boolean based off a probability"""
    return True if random.random() <= probability else False

def getDistance(person1,person2):
    """returns the distance between two people"""
    return sqrt(((person2.x_coord-person1.x_coord)**2)+
                ((person2.y_coord-person1.y_coord)**2))

class disease:
    def __init__(self,name="disease"):
        self.incubation         = 4  #How long does a virus incubate before being symptomatic
        self.symptomatic        = 4  #How long is someone able to have symptoms
        self.infectious         = 6  #How long is someone able to infect others
        self.mortality          =.02 #How likely is someone to die
        self.reproductionValue  = 1 #How likely the disease is to spread between people at a distance of one meter for one time unit
    
    def infectionProbability(self,distance,infecterModifier,infecteeModifier):
        """based on the assumption that the chance for transmission depends on how close they are and how careful each party is against transmission"""
        rValue = self.reproductionValue - infecteeModifier - infecteeModifier
        rValue = rValue if rValue > 0 else 0

        #im pulling this formula out of thin air, will modify once I can find something online
        try: probability = rValue / (distance**2)
        except: probability = 1 #if distance is zero, there will be an exception. Just assume that there is 100% chance of transmission

        return probability

    def chanceToBeInfected(self,individual,contaigousDataSet):
        """for a given individual, the chance that they will be infected depends on how likely others will infect"""
        for _,row in contaigousDataSet[["x_coord","y_coord","pInfectorOffset"]].iterrows():
            if booleanFromProbability(self.infectionProbability(getDistance(individual,row[["x_coord","y_coord"]]),row["pInfectorOffset"],individual["pResistanceOffset"])):
                individual["status"] = "incubation"
                return individual
        return individual

if __name__ == "__main__":
    import dataSet

    data = dataSet.dataSet(100)
    data.generate()
    data.initialize()

    d = disease()
    chanceToBeInfected = d.chanceToBeInfected

    print(data.data)
    contaigousDataSet = data.data.sample(20)
    data.data = data.data.apply(lambda x: chanceToBeInfected(x,contaigousDataSet=contaigousDataSet),axis=1)
    print(data.data)