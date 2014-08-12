'''
Created on Aug 11, 2014

@author: davide
'''

from Model.Person import Person
# import Foundation.Athlete
#from datetime import date

class Athlete(Person):
    def __init__(self, name, surname, sex, birthDate, height, weight, exercises):
        Person.__init__(self, name, surname, sex, birthDate, height, weight)
        self._exercises = exercises
        #athleteDb = Foundation.Athlete.Athlete()   
                 
    def __str__(self):
        athleteInfo = Person.__str__(self)
        athleteInfo += str(self._exercises)
        
        return athleteInfo
    

        
