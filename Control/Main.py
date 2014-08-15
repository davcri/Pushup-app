'''
Created on Aug 11, 2014

@author: davide
'''

from View.Main import Main as Main_View
from Foundation.Athlete import Athlete as Athlete_Foundation
from Model.Exercise import Exercise as Exercise_Model
from Model.Athlete import Athlete as Athlete_Model
from Foundation.Exercise import Exercise as Exercise_Foundation
import datetime




class Main():
    def __init__(self):
        #self.showMainWindow()        
        dum = Athlete_Model("dum", "asd", "Male", datetime.date.today(), 180, 90)
        self.addProfile(dum)
        
        exercise = Exercise_Model("dum", datetime.datetime.today(), 110)  
              
        self.addExercise(exercise)
        
    def addProfile(self, athlete):
        database = Athlete_Foundation()
        database.store(athlete)
    
    def showProfile(self, selectedProfile):
        athleteDb = Athlete_Foundation()
        print athleteDb.load(selectedProfile)
    
    def addExercise(self, exercise):
        database = Exercise_Foundation()
        database.add(exercise)
        pass
    
    def showMainWindow(self):
        mainWindow =  Main_View()        
        mainWindow.showMainWindow() 
        #mainWindow.showVersion()