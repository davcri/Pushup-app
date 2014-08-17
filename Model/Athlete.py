'''
Created on Aug 11, 2014

@author: davide
'''

from Model.Person import Person
# import Foundation.Athlete
#from datetime import date

class Athlete(Person):
    def __init__(self, name, surname, sex, birthDate, height, mass):
        Person.__init__(self, name, surname, sex, birthDate, height, mass)
        #self._exercises = exercises
        #athleteDb = Foundation.Athlete.Athlete()   
    
    def getBMI(self):
        heightInMeters = self._height/100
        
        bodyMassIndex = self._mass / (heightInMeters**2)
        
        return round(bodyMassIndex,1)
                 
    def __str__(self):
        athleteInfo = Person.__str__(self)
        #athleteInfo += str(self._exercises)
        
        return athleteInfo
    
    

        
