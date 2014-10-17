'''
Created on Aug 11, 2014

@author: davide
'''

from PySide.QtCore import QSize, Signal
from PySide.QtGui import QApplication, QMainWindow
from PySide.QtGui import QVBoxLayout, QHBoxLayout
from PySide.QtGui import QAction, QPushButton
from PySide.QtGui import QWidget, QMessageBox

from View.Widgets.Profile import Profile
from View.Widgets.PushupList import PushupList
from View.Widgets.GraphWidget import GraphWidget

class MainWindow(QMainWindow):
    
    profileCreationMenu_Requested = Signal()
    profileSelectionDialog_Requested = Signal()
    pushupCreationMenu_Requested = Signal()
    
    def __init__(self, athlete, pushups): 
        QMainWindow.__init__(self)
        self.setWindowTitle("Pushup app")       
        
        self.athlete = athlete
        self.pushups = pushups
        
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
        
        self.profileBox = Profile(self.athlete)
        self.addPushupBtn = QPushButton("Add Pushup")
        self.addPushupBtn.setMaximumWidth(100)
        
        self.pushupsListWidget = PushupList(self.pushups) 
        
        self.graphWidget = GraphWidget()
        #self.graphWidget.setMaximumSize(400, 300)
                
        vLayout.addWidget(self.profileBox)
        
        hLayout.addWidget(self.pushupsListWidget)
        innerVLayout.addWidget(self.graphWidget)
        hLayout.addLayout(innerVLayout)
        
        vLayout.addLayout(hLayout)
        
        vLayout.addWidget(self.addPushupBtn)
        
        self.mainWidget.setLayout(vLayout)
        self.setCentralWidget(self.mainWidget)
            
    def _createMenus(self):
        self._createActions()
        
        fileMenu = self.menuBar().addMenu("&File")
        profile = self.menuBar().addMenu("&Profile")
        about = self.menuBar().addMenu("&About")
        
        fileMenu.addAction(self.exit)
        profile.addAction(self._switchProfile)
        profile.addAction(self._createProfile)
        about.addAction(self.aboutQtAction)
        about.addAction(self.aboutApplicationAction)
    
    def _createActions(self):             
        # About Menu
        self.aboutQtAction = QAction("About PySide (Qt)", self)
        self.aboutApplicationAction = QAction("About Pushup App", self)
        
        # Profile Menu
        self._createProfile = QAction("Create new profile", self)
        self._switchProfile = QAction("Switch profile", self)
        
        #File Menu
        self.exit = QAction("Exit", self)   
        
        self.exit.triggered.connect(self._actionExit)
        self._createProfile.triggered.connect(self._actionCreateProfile)
        self._switchProfile.triggered.connect(self._actionSwitchProfile)
        self.aboutQtAction.triggered.connect(self._actionAboutQt)
        self.aboutApplicationAction.triggered.connect(self._actionAboutApplication)  
        
    def _actionExit(self):
        self.close()
    
    def _actionCreateProfile(self): 
        self.profileCreationMenu_Requested.emit()        
    
    def _actionSwitchProfile(self):
        self.profileSelectionDialog_Requested.emit()
        
    def _actionAboutApplication(self):
        text = "Pushup app is a work in progress application.<br><br>\
                For development information look at the \
                <a href=\"https://github.com/davcri/Push-up-app\">Github Page</a> <br>"
        QMessageBox.about(self, "About Pushup app", text)   
    
    def _actionAboutQt(self):
        QMessageBox.aboutQt(self)
                        
    def _centerWindow(self):
        displayWidth = QApplication.desktop().width()
        displayHeight = QApplication.desktop().height()
        
        self.move(displayWidth/2.0 - self._initWidth/2.0, 
                  displayHeight/2.0 - self._initHeight/2.0 - 50)        
    
    def cleanUI(self):
        self.profileBox.ageLabel.setText("")
        self.profileBox.nameLabel.setText("")
        self.profileBox.surnameLabel.setText("")
        self.profileBox.bmiLabel.setText("")
        self.profileBox.heightLabel.setText("")
        self.profileBox.massLabel.setText("")
        
        self.pushupsListWidget.pushupsListWidget.clear()
        # the first pushupListWidget is the name of the PushupList instance
        # the second is the name of a property of the PushupList instance
        
        self.addPushupBtn.setDisabled(True)
        self.graphWidget.clear()