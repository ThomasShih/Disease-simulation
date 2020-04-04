import numpy as np

individual = {
            "pResistanceOffset" :np.round(np.linspace(0,1,11),1), #how careful is someone from trying not to get infected?
            "pInfectorOffset"   :np.round(np.linspace(0,1,11),1), #how careful is someone from infecting other if infected?
            "age"               :range(0,80,1),
            "status"            :["susceptible"],
            "status_enlapsed"   :[0], #how long has it been since the last status has changed?
            "x_coord"           :range(-5,5,1),
            "y_coord"           :range(-5,5,1),
        } 

population = {
            "populationSize" : 20,
        }

disease = {
            "name"              : "disease",
            "immunityChance"    : 0.1,  #What are the chances that someone is already immune
            "mortality"         :.02,   #How likely is someone to die at the end of the disease
            "reproductionValue" : 1,    #How likely the disease is to spread between people at a distance of one meter for one time unit
            #What is the proflie of people being able to infect, and when they are symptomatic?
            "contagious"        : list(map(bool,[0,0,0,0,1,1,1,1,1,1])),
            "symptomatic"       : list(map(bool,[0,0,0,0,0,0,1,1,1,1])),
            "movementProfile"   :               [5,5,5,5,5,5,5,5,5,5] #how far can an individual after being infected
        }

removedCategory = ["immune","deceased","recovered"]
summaryColumns = ["susceptible","infected"] + removedCategory + ["newlyInfected"]

simulation = {
            "cycles"      : 100,
            "moveRemoved" : False,
            "xBoundary"   : (individual["x_coord"][0],individual["x_coord"][-1]),
            "yBoundary"   : (individual["y_coord"][0],individual["y_coord"][-1]),
        }