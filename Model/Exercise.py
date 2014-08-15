'''
Created on Aug 11, 2014

@author: davide
'''

from datetime import datetime

class Exercise:
    ''' Generic exercise class'''
    def __init__(self, athleteName, date = datetime.now(), avgHeartRate = 0):
        self._athleteName = athleteName
        self._date = date
        self._averageHeartRate = avgHeartRate
    
    def __str__(self):
        objectInfo = "Name = " + self._athleteName + "\n"
        objectInfo += "Timestamp [Y - M - D H:m:s:ms] = " + str(self._date) + "\n"
        objectInfo += "Average heart rate : " + str(self._averageHeartRate) + " bpm" + "\n"
       
        return objectInfo
        

# flessioni = Exercise("Flessioni", datetime.now(), 100)
# print flessioni