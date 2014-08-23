'''
Created on Aug 11, 2014

@author: davide
'''

from Foundation.Athlete import Athlete as Athlete_Foundation
from Foundation.Exercise import Exercise as Exercise_Foundation
from Foundation.Pushup import Pushup as Pushup_Foundation

from View.MainWindow import MainWindow as Main_View
from View.Widgets.ProfileCreation import ProfileCreation
from View.Widgets.PushupForm import PushupForm

class MainWindow():
    def __init__(self, athlete): 
        self.athlete = athlete
        self.pushups = athlete.getPushups()
        
        self.pushupCreationDialog = PushupForm(self.athlete)
        
        self.showMainWindow()     
    
    def showMainWindow(self):                    
        self.mainWindow =  Main_View(self.athlete, self.pushups)
        self.mainWindow.addPushupBtn.clicked.connect(self._showPushup_DialogForm) 
        self.mainWindow.show()          
                    
    def createAthlete (self):
        profileCreation = ProfileCreation()
        athlete = profileCreation.getAthleteProfile() 
        
        return athlete
    
    def storeAthlete(self, athlete):
        database = Athlete_Foundation()
        database.store(athlete)
    
    def loadAthlete(self, selectedProfile):
        athleteDb = Athlete_Foundation()
        return athleteDb.load(selectedProfile)
    
    def loadAthletes(self):
        athleteDb = Athlete_Foundation()
        return athleteDb.getAthletes()
    
    def storeExercise(self, exercise):
        database = Exercise_Foundation()
        database.add(exercise)
        
    def loadExercises(self, athleteName):
        database = Exercise_Foundation()        
        return database.getExercisesByAthleteName(athleteName)
    
    def storePushup(self, pushup):
        database = Pushup_Foundation()
        database.store(pushup)
        
    def loadPushups(self, athleteName):
        db = Pushup_Foundation()
        lists = db.getPushupsByAthlete(athleteName)
        
        return lists  
    
    def _showPushup_DialogForm(self):
        self.pushupCreationDialog.exec_()
