'''
Created on Aug 11, 2014

@author: davide
'''

from View.Main import Main as Main_View
from Model.Exercise import Exercise as Exercise_Model
from Model.Athlete import Athlete as Athlete_Model
from Model.Pushup import Pushup as Pushup_Model
from Foundation.Athlete import Athlete as Athlete_Foundation
from Foundation.Exercise import Exercise as Exercise_Foundation
from Foundation.Pushup import Pushup as Pushup_Foundation

import datetime


class Main():
    def __init__(self):
        #self.showMainWindow()    
        
        #at = Athlete_Model("dav", "s", "m", datetime.datetime.today(), 180, 90)
        #ex = Exercise_Model("dav", datetime.datetime.today(), 90)
        
        #self.addProfile(at)
        #self.addExercise(ex)
        #self.addPushUp()        
        p = Pushup_Model("dav", datetime.datetime.today(), 80, 1, 15)
        db = Pushup_Foundation()
        db.store(p)
        
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
    
    def addPushUp(self):
        database = Pushup_Foundation()
        database.addPushup("super")
            
    def showMainWindow(self):
        mainWindow =  Main_View()        
        mainWindow.showMainWindow() 
        #mainWindow.showVersion()