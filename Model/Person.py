'''
Created on Aug 10, 2014

@author: davide
'''

import datetime

class Person:
    ''' Represents a person '''
      
    def __init__(self, name, surname, sex, birthDate, height, mass):
        ''' Initialize a person '''
        self._name = name 
        self._surname = surname
        self._sex = sex
        self._birthDate = birthDate # date object
                
        if self.getAge_inDays() < 0:
            print "Birth date "+ str(self._birthDate) + " is invalid." + \
                  " Resetting birth date to " + str(datetime.date.today())
            print "Is your system date correct ?" +\
                  " Or are you just trying to being funny ?\n"
            self._birthDate = datetime.date.today()        
        
        self._height = height # in centimeters (cm)
        self._mass = mass # in Kilograms (Kg)
                    
    def getAge(self):
        ''' Gets the age of a person, measured in years '''        
        daysInYear = 365.242199
        years = self.getAge_inDays() / daysInYear 
        
        return int(years)
    
    def getAge_inDays(self):
        timedeltaObj = datetime.date.today() - self._birthDate
        
        return timedeltaObj.days
             
    def __str__(self):
        personData = self._name + "\n" + self._surname + "\n" + self._sex + "\n" 
        personData += str(self._birthDate) + "\n" + str(self.getAge()) + " years old\n"
        personData += str(self._height) + " cm" +"\n" + str(self._mass) + " Kg" + "\n"    
     
        return personData           

