'''
Created on Aug 11, 2014

@author: davide
'''

from Control.MainWindow import MainWindow
from Control.ProfileSelector import ProfileSelector
from Control.ProfileCreation import ProfileCreation
from Foundation.Athlete import Athlete as Athlete_Database

from PySide.QtGui import QApplication 
from os import sys
 
qtApplication = QApplication(sys.argv)

database = Athlete_Database()
athletes = database.getAthletes()

if len(athletes) == 0:
    profileCreation = ProfileCreation()    
    athlete = profileCreation.runCreationDialog()
    
    if athlete is not False :
        database.store(athlete)
    else :
        print "No athlete created. Pushup-app quitting"
        sys.exit(qtApplication.quit())
        
elif len(athletes) == 1:
    athlete = athletes[0]
    
elif len(athletes) > 1:
    profileSelection = ProfileSelector(athletes)
    athlete = profileSelection.getSelectedAthlete()
    
    assert athlete is not False
        #sys.exit(self.qtApplication.exec_())

mainController = MainWindow(athlete) # calls the MainWindow controller
mainController.showMainWindow()
sys.exit(qtApplication.exec_())