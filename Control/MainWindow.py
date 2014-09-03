'''
Created on Aug 11, 2014

@author: davide
'''
from PySide.QtCore import Slot

from Foundation.Pushup import Pushup as Pushup_Foundation
from Foundation.Athlete import Athlete as Athlete_Database

from Control.GraphPlotter import GraphPlotter
from Control.ProfileCreation import ProfileCreation
from Control.PushupCreator import PushupCreator
from Control.ProfileSelector import ProfileSelector

from View.MainWindow import MainWindow as MainWindow_View


class MainWindow():
    def __init__(self, athlete): 
        self.athlete = athlete
        self.pushups = athlete.getPushups()
        self.mainWindow = MainWindow_View(self.athlete, self.pushups)
        
        self.graphController = GraphPlotter(self.mainWindow.graphWidget, self.pushups)
        self.graphController.initPlotWidget()
        
        self._initComponents()
        self._initSlots()
        
        self.showMainWindow()     
            
    def _initComponents(self):
        self.pushupCreation_Controller = PushupCreator(self.athlete)
        self.pushupCreation_Controller.pushupStored.connect(self.refreshGUI)
        
    def _initSlots(self):
        self.mainWindow.addPushupBtn.clicked.connect(self._showPushup_DialogForm) 
        self.mainWindow.pushupsListWidget.deletePushup.connect(self.deletePushup)
        self.mainWindow.pushupsListWidget.deletePushups_in_a_day.connect(self._deleteDay)
        self.mainWindow.profileCreationMenu_Requested.connect(self._profileCreation)
        self.mainWindow.profileSelectionDialog_Requested.connect(self._profileSelection)
    
    def showMainWindow(self):                            
        self.mainWindow.show()            
    
    @Slot()
    def _showPushup_DialogForm(self):        
        self.pushupCreation_Controller.showCreationDialog()      
    
    @Slot(int)
    def deletePushup(self, pushupId):
        database = Pushup_Foundation()
        database.deletePushup(pushupId)
        
        self.refreshGUI()
    
    @Slot(tuple)
    def _deleteDay(self, pushupsId):        
        database = Pushup_Foundation()
        
        database.deletePushups(pushupsId)
                
        self.refreshGUI()
#         for pushupId in pushupsId:
#             database.deletePushup(pushupId)
#         
#         self.refreshGUI()
        
    @Slot()
    def _profileCreation(self):
        profileCreationDialog = ProfileCreation()
        profileCreationDialog.runCreationDialogAndStore()
    
    @Slot()
    def _profileSelection(self):
        database = Athlete_Database()
        athletes = database.getAthletes()
        
        profileSelector = ProfileSelector(athletes) # Modal window appears
        
        athleteSelected = profileSelector.getSelectedAthlete()
                 
        if athleteSelected != self.athlete and athleteSelected is not False:
            self.athlete = athleteSelected
            self._initComponents()
            self.refreshGUI()            
        
    def refreshGUI(self):
        database = Pushup_Foundation()
        updatedPushups = database.getPushupsByAthlete(self.athlete._name)
        
        self.mainWindow.pushupsListWidget.reloadPushupsList(updatedPushups)
        self.mainWindow.profileBox.refreshProfile(self.athlete)
        self.graphController.refreshGraph(updatedPushups)