from math import sqrt, pi, sin, cos
import random

def booleanFromProbability(probability):
    """Generates a boolean based off a probability"""
    return True if random.random() <= probability else False

def getDistance(person1,person2):
    """returns the distance between two people"""
    return sqrt(((person2.x_coord-person1.x_coord)**2)+
                ((person2.y_coord-person1.y_coord)**2))

class disease:
    def __init__(self,attributes):
        self.symptomatic        = attributes.disease["symptomatic"]
        self.contagious         = attributes.disease["contagious"]
        self.mortality          = attributes.disease["mortality"]
        self.reproductionValue  = attributes.disease["reproductionValue"]
        self.movementProfile    = attributes.disease["movementProfile"]
        self.xBoundary          = attributes.simulation["xBoundary"]
        self.yBoundary          = attributes.simulation["yBoundary"]
        self.angles             = range(360) #I only want this array generated once, hence placing it in init
    
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
                individual["status"] = "infected"
                #reset the status_enlapsed attribute
                individual["status_enlapsed"] = 0
                return individual
        return individual

    def getContagiousIndividuals(self,data):
        """Returns a dataframe of individuals of whom is contagious"""
        infectedData = data[data.status == "infected"]
        daysOfInterest = list(filter(lambda item: item[1] == True,list(enumerate(self.contagious))))
        infectiousDays = list(map(lambda x:x[0],daysOfInterest))
        return infectedData[infectedData["status_enlapsed"].isin(infectiousDays)]

    def movement(self,individual):
        """Calculates and moves individuals"""

        #assumes that healthy individuals have a movement profile of infected indivuals at day 1
        try:
            R =  self.movementProfile[individual["status_enlapsed"]]\
                if individual["status"] == "infected"\
                else self.movementProfile[0]
        except (IndexError): 
            R = self.movementProfile[0]

        #move the individual to a random point in circle with radius R
            #get movement amount
        r = random.choice(range(R))
            #get angle of movement
        theta = random.choice(self.angles)*(pi/180)
            #get movement
        moveY , moveX = round(sin(theta)*r) , round(cos(theta)*r)
        individual["x_coord"],individual["y_coord"] = individual["x_coord"] + moveX,individual["y_coord"] + moveY
            #make sure movement is within boundaries
        if individual["x_coord"] < self.xBoundary[0]:
            individual["x_coord"] = self.xBoundary[0]
        elif individual["x_coord"] > self.xBoundary[1]:
            individual["x_coord"] = self.xBoundary[1]

        if individual["y_coord"] < self.yBoundary[0]:
            individual["y_coord"] = self.yBoundary[0]
        elif individual["y_coord"] > self.yBoundary[1]:
            individual["y_coord"] = self.yBoundary[1]

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