import random
import pandas as pd
import numpy as np
import tools.attributes as attributes

class modelling:
    def getLandscape(self,dataSet):
        #sort the data

        data = dataSet.sort_values(by=["x_coord","y_coord"])[["x_coord","y_coord"]]

        #build a 2d numpy array of how this looks
        dataMap = np.zeros((attributes.individual["x_coord"][-1]+1,attributes.individual["x_coord"][-1]+1))

        for _,row in data.iterrows():
            x=row["x_coord"]
            y=row["y_coord"]
            dataMap[x-1][y-1] += 1

        return dataMap

    def distanceCutoff(self):
        if (attributes.simulation["distanceCutoff"]!=None):
            return #don't calculate again if already done
        else:
            attributes.simulation["distanceCutoff"]=0
            while(True):
                attributes.simulation["distanceCutoff"]+=1
                if self.disease.infectionProbability(attributes.simulation["distanceCutoff"],0,0) <= attributes.simulation["simplification"]:
                    return attributes.simulation["distanceCutoff"]

        