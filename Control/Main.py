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

from datetime import date


class Main():
    def __init__(self):
        #self.showMainWindow()
        profile =  "assd"
        me = Athlete_Model(profile, "Cristini", "Male", date(1991,8,10), 188, 70)
        self.storeAthlete(me)
        
        print self.loadAthlete(profile)
            
                
    def storeAthlete(self, athlete):
        database = Athlete_Foundation()
        database.store(athlete)
    
    def loadAthlete(self, selectedProfile):
        athleteDb = Athlete_Foundation()
        return athleteDb.load(selectedProfile)
        
    def storeExercise(self, exercise):
        database = Exercise_Foundation()
        database.add(exercise)
        
    def loadExercises(self, athleteName):
        database = Exercise_Foundation()        
        return database.getExercisesByAthleteName(athleteName)
    
    def storePushup(self, pushup):
        database = Pushup_Foundation()
        database.store(pushup)
        
    def loadPushups(self):
        db = Pushup_Foundation()
        lists = db.load()
        
        return lists
            
    def showMainWindow(self):
        mainWindow =  Main_View()        
        mainWindow.showMainWindow() 
        #mainWindow.showVersion()