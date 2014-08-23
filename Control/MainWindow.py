'''
Created on Aug 11, 2014

@author: davide
'''

# from Model.Exercise import Exercise as Exercise_Model
# from Model.Athlete import Athlete as Athlete_Model
# from Model.Pushup import Pushup as Pushup_Model
from Foundation.Athlete import Athlete as Athlete_Foundation
from Foundation.Exercise import Exercise as Exercise_Foundation
from Foundation.Pushup import Pushup as Pushup_Foundation

from PySide.QtGui import QApplication
from View.MainWindow import MainWindow as Main_View
from View.Widgets.ProfileSelection import ProfileSelection
from View.Widgets.ProfileCreation import ProfileCreation

import sys

class MainWindow():
    def __init__(self, athlete): 
        self.athlete = athlete
        self.pushups = athlete.getPushups()
        
        self.showMainWindow()     
    
    def showMainWindow(self):
        #qtApplication.setStyleSheet("*{background-color : blue}")
                    
        self.mainWindow =  Main_View(self.athlete, self.pushups)  
        self.mainWindow.show()
                 
                    
        
    def showMainWindow_Old(self):
        self.qtApplication = QApplication(sys.argv)
        #qtApplication.setStyleSheet("*{background-color : blue}")
        
        athletesList = self.loadAthletes()
        
        if len(athletesList) == 0:            
            athlete = self.createAthlete()
            
            if athlete != False:
                self.storeAthlete(athlete)
            
                emptyPushupList = []
                mainWindow =  Main_View(athlete, emptyPushupList)   
                mainWindow.show() 
            else:
                print "No athlete created. Pushup-app quitting"
                sys.exit(self.qtApplication.quit())
            
        elif len(athletesList) == 1:
            athlete = athletesList[0]
            pushups = self.loadPushups(athlete._name)
            
            mainWindow =  Main_View(athlete, pushups)   
            mainWindow.show()
            
        elif len(athletesList) > 1:
            profileSelection = ProfileSelection(athletesList)
               
            if profileSelection.execDialogWindow() == True :
                selectedAthleteProfile = profileSelection.getSelectedProfile()
                pushups = self.loadPushups(selectedAthleteProfile._name)
                           
                mainWindow =  Main_View(selectedAthleteProfile, pushups)  
                mainWindow.show()
                 
        sys.exit(self.qtApplication.exec_())                   
                    
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
            
    
            
