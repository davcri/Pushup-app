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
    def __init__(self):
        self.showMainWindow()     
    
    def showMainWindow(self):
        qtApplication = QApplication(sys.argv)
        
        athletesList = self.loadAthletes()
        
        if len(athletesList) == 0:            
            print "No athlete registered"
            
            profileCreation = ProfileCreation()
            athlete = profileCreation.getAthleteProfile() 
            
            if athlete != False:
                self.storeAthlete(athlete)
                emptyPushupList = []
                mainWindow =  Main_View(athlete, emptyPushupList)   
                mainWindow.show() 
            else:
                print "No athlete created. Pushup-app quitting"
                sys.exit(qtApplication.quit())            
        elif len(athletesList) == 1:
            athlete = athletesList[0]
            pushups = self.loadPushups(athlete._name)
            
            mainWindow =  Main_View(athlete, pushups)   
            mainWindow.show()
            
        elif len(athletesList) > 1:
            profileSelection = ProfileSelection(athletesList)
               
            if profileSelection.execDialogWindow() == True :
                selectedProfile = profileSelection.getSelectedProfile()           
                mainWindow =  Main_View(selectedProfile) # NOT TESTED !   
                mainWindow.show()
                 
        sys.exit(qtApplication.exec_())                   
                
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
            
    
            
