'''
Created on Aug 11, 2014

@author: davide
'''

from View.Main import Main as Main_View
from Foundation.Athlete import Athlete as Athlete_Foundation
#from Model.Exercise import Exercise as Exercise_Model
#from Model.Athlete import Athlete as Athlete_Model
from Foundation.Exercise import Exercise as Exercise_Foundation
#import datetime


class Main():
    def __init__(self):
        #self.showMainWindow()        
        print self.loadExercises("dum")
        
    def addProfile(self, athlete):
        database = Athlete_Foundation()
        database.store(athlete)
    
    def showProfile(self, selectedProfile):
        athleteDb = Athlete_Foundation()
        athleteDb.load(selectedProfile)
        
    def addExercise(self, exercise):
        database = Exercise_Foundation()
        database.add(exercise)
        
    def loadExercises(self, athleteName):
        database = Exercise_Foundation()        
        exercises = database.getExercisesByAthleteName(athleteName)
        return exercises
            
    def showMainWindow(self):
        mainWindow =  Main_View()        
        mainWindow.showMainWindow() 
        #mainWindow.showVersion()