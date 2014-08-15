'''
Created on Aug 10, 2014

@author: davide
'''

import datetime

class Person:
    ''' Represents a person '''
      
    def __init__(self, name, surname, sex, birthDate, height, weight):
        ''' Initialize a person '''
        self._name = name 
        self._surname = surname
        self._sex = sex
        self._birthDate = birthDate # datetime object
        self._height = height # in centimeters (cm)
        self._weight = weight # in Kilograms (Kg)
                    
    def getAge(self):
        ''' Gets the age of a person '''
        today = datetime.datetime.today()
        ageDelta = today - self._birthDate
        
        daysInYear = 365.242199
        years = ageDelta.days / daysInYear 
        
        return int(years)
     
    def loadExercises(self):
        pass
         
    def __str__(self):
        personData = self._name + "\n" + self._surname + "\n" + self._sex + "\n" 
        personData += str(self._birthDate) + "\n" + str(self.getAge()) + " years old\n"
        personData += str(self._height) + " cm" +"\n" + str(self._weight) + " Kg" + "\n"    
     
        return personData           

