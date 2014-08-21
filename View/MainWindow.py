'''
Created on Aug 11, 2014

@author: davide
'''

from PySide.QtCore import QSize
from PySide.QtGui import QApplication, QMainWindow, \
                         QVBoxLayout, QHBoxLayout, \
                         QAction, QPushButton, \
                         QWidget, QMessageBox, QLabel

from View.Widgets.Profile import Profile
from View.Widgets.PushupForm import PushupForm
from View.Widgets.PushupEdit import PushupEdit
from Control.ProfileCreation import ProfileCreation as ProfileCreation_Control
from Control.PushupList import PushupList as PushupList_Control
from Control.GraphPlotter import GraphPlotter

class MainWindow(QMainWindow):
    def __init__(self, athlete, pushups): 
        QMainWindow.__init__(self)
        self.setWindowTitle("Pushup app")       
        
        self.athlete = athlete
        self.pushups = pushups
               
        self.pushupCreationDialog = PushupForm(self.athlete)
        self.editDialog = PushupEdit()
        
        self._initWidth = 1000
        self._initHeight = 600
        self.resize(QSize(self._initWidth, self._initHeight))
        
        self.createGUI()
        self._centerWindow()        
            
    def createGUI(self):
        self.mainWidget = QWidget()
        self._createMenus()
        
        hLayout = QHBoxLayout()
        vLayout = QVBoxLayout()
        innerVLayout = QVBoxLayout()
        
        profileBox = Profile(self.athlete)
        addPushupBtn = QPushButton("Add Pushup")
        addPushupBtn.clicked.connect(self._showPushup_DialogForm)
        addPushupBtn.setMaximumWidth(100)
        self.editBtn = QPushButton("Edit")
        self.editBtn.clicked.connect(self._showEditDialog)
        self.editBtn.setDisabled(True)
        self.editBtn.setMaximumWidth(100)
        
        self.pushupListController = PushupList_Control(self.athlete, self.pushups)
        self.pushupCreationDialog.pushupAdded.connect(self.pushupListController.refreshList)
        
        pushupsList = self.pushupListController.getListWidget()
        pushupsList.pushupsListWidget.clicked.connect(self._enableEditButton)
        # pushupsList = PushupList_Widget(self.pushups) 
        
        graphController = GraphPlotter(self.pushups)
        self.graphWidget = graphController.getGraphWidget()
        self.graphWidget.setMaximumSize(400, 300)
                
        vLayout.addWidget(profileBox)
        
        hLayout.addWidget(pushupsList)
        innerVLayout.addWidget(self.graphWidget)
        hLayout.addLayout(innerVLayout)
        
        vLayout.addLayout(hLayout)
        
        vLayout.addWidget(addPushupBtn)
        vLayout.addWidget(self.editBtn)
        
        self.mainWidget.setLayout(vLayout)
        self.setCentralWidget(self.mainWidget)
    
    def _showPushup_DialogForm(self):
        self.pushupCreationDialog.exec_()    
        
    def _showEditDialog(self):
        self.editDialog.exec_()
        
    def _enableEditButton(self):
        self.editBtn.setDisabled(False)
            
    def _createMenus(self):
        self._createActions()
        
        fileMenu = self.menuBar().addMenu("File")
        profile = self.menuBar().addMenu("Profile")
        about = self.menuBar().addMenu("About")
        
        fileMenu.addAction(self.exit)
        profile.addAction(self._createProfile)
        about.addAction(self.aboutQtAction)
        about.addAction(self.aboutApplicationAction)
    
    def _actionExit(self):
        self.close()
    
    def _actionCreateProfile(self): 
        profileCreation = ProfileCreation_Control()
        profileCreation.runCreationDialogAndStore()        
           
    def _actionAboutApplication(self):
        text = "Pushup app is a work in progress application.<br><br>\
                For developmente info look at the \
                <a href=\"https://github.com/davcri/Push-up-app\">Github Page</a> <br>"
        QMessageBox.about(self, "About Pushup app", text)   
    
    def _actionAboutQt(self):
        QMessageBox.aboutQt(self)
        
    def _createActions(self):             
        self.aboutQtAction = QAction("About PySide (Qt)", self)
        self.aboutApplicationAction = QAction("About Pushup App", self)
        self._createProfile = QAction("Create new profile", self)
        
        self.exit = QAction("Exit", self)   
        
        self.exit.triggered.connect(self._actionExit)
        self._createProfile.triggered.connect(self._actionCreateProfile)
        self.aboutQtAction.triggered.connect(self._actionAboutQt)
        self.aboutApplicationAction.triggered.connect(self._actionAboutApplication)        
        
                
    def _centerWindow(self):
        displayWidth = QApplication.desktop().width()
        displayHeight = QApplication.desktop().height()
        
        self.move(displayWidth/2.0 - self._initWidth/2.0, 
                  displayHeight/2.0 - self._initHeight/2.0 - 50)        
    
