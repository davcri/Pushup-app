'''
Created on Aug 11, 2014

@author: davide
'''

from Model.Person import Person
from Foundation.Pushup import Pushup

class Athlete(object, Person):
    def __init__(self, name, surname, sex, birthDate, height, mass):
        Person.__init__(self, name, surname, sex, birthDate, height, mass)
        
        database = Pushup()
        self.pushups = database.getPushupsByAthlete(self._name)
    
    def getBMI(self):
        heightInMeters = self._height/100
        
        bodyMassIndex = self._mass / (heightInMeters**2)
        
        return round(bodyMassIndex,1)
                 
    def getPushups(self):
        return self.pushups
    
    def __str__(self):
        athleteInfo = Person.__str__(self)
        #athleteInfo += str(self._exercises)
        
        return athleteInfo
    
    def __eq__(self, other):
        if self._name == other._name :
            
            return True
        else :
            return False
        
    def __ne__(self, other):
        return not self.__eq__(other)

        
