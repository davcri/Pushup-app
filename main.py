'''
Created on Aug 11, 2014

This file is the starting point of the application.
Run this file to to start Pushup-app :)

You can do it opening the terminal in the Pushup-app folder and typing : 
    "python ./main.py"

@author: davide
'''

from os import sys

from PySide.QtGui import QApplication 

from Control.MainWindow import MainWindow
from Control.ProfileSelector import ProfileSelector
from Control.ProfileCreation import ProfileCreation
from Foundation.Athlete import Athlete as Athlete_Database


def getAthleteProfile():
    database = Athlete_Database()
    athletes = database.getAthletes()
    
    if len(athletes) == 0: 
        _profileCreation = ProfileCreation()    
        athlete = _profileCreation.runCreationDialog()
        
        if athlete is not False :
            database.store(athlete)
        else :
            athlete = False
            print "No athlete created. Pushup-app quitting"
            
    elif len(athletes) == 1:
        athlete = athletes[0]
        
    elif len(athletes) > 1:
        profileSelection = ProfileSelector(athletes)
        profileSelection.runSelectionDialog()
        
        athlete = profileSelection.getSelectedAthlete()
    
    return athlete 

#
# Application starts here !
#
qtApplication = QApplication(sys.argv)

athlete = getAthleteProfile()
    
if athlete is not False :
    mainController = MainWindow(athlete)
    mainController.showMainWindow()
    
    sys.exit(qtApplication.exec_())
else :
    sys.exit(qtApplication.quit())