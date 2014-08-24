'''
Created on Aug 11, 2014

@author: davide
'''
from PySide.QtCore import Slot

from Model.Pushup import Pushup as Pushup_Model

from Foundation.Pushup import Pushup as Pushup_Foundation

from Control.GraphPlotter import GraphPlotter
from Control.ProfileCreation import ProfileCreation

from View.MainWindow import MainWindow as Main_View
from View.Widgets.PushupForm import PushupForm

class MainWindow():
    def __init__(self, athlete): 
        self.athlete = athlete
        self.pushups = athlete.getPushups()
        self.mainWindow =  Main_View(self.athlete, self.pushups)
        
        self.pushupCreationDialog = PushupForm(self.athlete)
        
        self.graphController = GraphPlotter(self.mainWindow.graphWidget, self.pushups)
        self.graphController.initPlotWidget()
        
        self.initSlots()
        self.showMainWindow()     
        
    def showMainWindow(self):                            
        self.mainWindow.show()          
    
    def initSlots(self):
        self.pushupCreationDialog.pushupCreated.connect(self.storePushup)
        self.mainWindow.addPushupBtn.clicked.connect(self._showPushup_DialogForm) 
        self.mainWindow.pushupsListWidget.deletePushup.connect(self.deletePushup)
        self.mainWindow.profileCreationMenu_Requested.connect(self.profileCreation)
        
    @Slot()
    def _showPushup_DialogForm(self):
        self.pushupCreationDialog.exec_()             
    
    @Slot(Pushup_Model)
    def storePushup(self, pushup):
        database = Pushup_Foundation()
        database.store(pushup)
        
        self.refreshGUI()
    
    @Slot(int)
    def deletePushup(self, pushupId):
        database = Pushup_Foundation()
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
    

