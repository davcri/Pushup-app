'''
Created on Aug 15, 2014

@author: davide
'''
from PySide.QtCore import QObject
from Model.Exercise import Exercise

class Pushup(object, Exercise):
    '''
    classdocs
    '''

    def __init__(self, athleteName, date, avgHeartRate, series, repetitions):
        '''
        Constructor
        '''        
        Exercise.__init__(self, athleteName, date, avgHeartRate)
        self._series = series
        self._repetitions = repetitions
        
    def __str__(self):
        objInfo = Exercise.__str__(self)
        objInfo += "Series = " + str(self._series) + "\n" 
        objInfo += "Repetitions = " + str(self._repetitions) +"\n"
        
        return objInfo
        
        