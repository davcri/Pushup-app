'''
Created on Aug 11, 2014

@author: davide
'''
from PySide.QtCore import Slot

from Foundation.Pushup import Pushup as Pushup_Foundation

from Control.GraphPlotter import GraphPlotter
from Control.ProfileCreation import ProfileCreation
from Control.PushupCreator import PushupCreator

from View.MainWindow import MainWindow as MainWindow_View


class MainWindow():
    def __init__(self, athlete): 
        self.athlete = athlete
        self.pushups = athlete.getPushups()
        self.mainWindow =  MainWindow_View(self.athlete, self.pushups)
        
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
        self.mainWindow.pushupsListWidget.deletePushups_in_a_day.connect(self.deleteDay)
        self.mainWindow.profileCreationMenu_Requested.connect(self.profileCreation)
    
    def showMainWindow(self):                            
        self.mainWindow.show()            
    
    @Slot()
    def _showPushup_DialogForm(self):        
        self.pushupCreation_Controller.showCreationDialog()
        #self.pushupCreationDialog.exec_()             
    
    @Slot(int)
    def deletePushup(self, pushupId):
        database = Pushup_Foundation()
        database.deletePushup(pushupId)
        
        self.refreshGUI()
    
    @Slot(tuple)
    def deleteDay(self, pushupsId):        
        database = Pushup_Foundation()
        
        for pushupId in pushupsId:
            database.deletePushup(pushupId)
        
        self.refreshGUI()
        
    @Slot()
    def profileCreation(self):
        profileCreationDialog = ProfileCreation()
        profileCreationDialog.runCreationDialogAndStore()
        
    def refreshGUI(self):
        database = Pushup_Foundation()
        updatedPushups = database.getPushupsByAthlete(self.athlete._name)
        
        self.mainWindow.pushupsListWidget.reloadPushupsList(updatedPushups)
        self.graphController.refreshGraph(updatedPushups)
        
    
    
    
    # Unused methods
    #__________________________________________
    
#     def createAthlete (self):
#         profileCreation = ProfileCreation()
#         athlete = profileCreation.getAthleteProfile() 
#         
#         return athlete
#     
#     def storeAthlete(self, athlete):
#         database = Athlete_Foundation()
#         database.store(athlete)
#     
#     def loadAthlete(self, selectedProfile):
#         athleteDb = Athlete_Foundation()
#         return athleteDb.load(selectedProfile)
#     
#     def loadAthletes(self):
#         athleteDb = Athlete_Foundation()
#         return athleteDb.getAthletes()
#     
#     def storeExercise(self, exercise):
#         database = Exercise_Foundation()
#         database.add(exercise)
#         
#     def loadExercises(self, athleteName):
#         database = Exercise_Foundation()        
#         return database.getExercisesByAthleteName(athleteName)
#     
#     def loadPushups(self, athleteName):
#         db = Pushup_Foundation()
#         lists = db.getPushupsByAthlete(athleteName)
#         
#         return lists  
    

