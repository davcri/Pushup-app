'''
Created on Aug 11, 2014

@author: davide
'''

import PySide
from PySide.QtCore import QSize
from PySide.QtGui import QApplication, QMainWindow, \
                         QVBoxLayout, QHBoxLayout, \
                         QAction, QPushButton, \
                         QWidget, QMessageBox, QLabel

from View.Widgets.Profile import Profile
from View.Widgets.ProfileCreation import ProfileCreation 
from View.Widgets.PushupForm import PushupForm
from View.Widgets.PushupList import PushupList as PushupList_Widget
from Control.ProfileCreation import ProfileCreation as ProfileCreation_Control

class MainWindow(QMainWindow):
    def __init__(self, athlete, pushups): 
        QMainWindow.__init__(self)
        self.setWindowTitle("Pushup app")       
        
        self.athlete = athlete
        self.pushups = pushups
        
        self._initWidth = 700
        self._initHeight = 600
        self.resize(QSize(self._initWidth, self._initHeight))
        # self._centerWindow()
        
        self.createGUI()        
            
    def createGUI(self):
        self.mainWidget = QWidget()
        self._createMenus()
        
        hLayout = QHBoxLayout()
        vLayout = QVBoxLayout()
        innerVLayout = QVBoxLayout()
        
        profileGUI = Profile(self.athlete)
        addPushupBtn = QPushButton("Add Pushup")
        addPushupBtn.clicked.connect(self._pushupForm)
        
        pushupsList = PushupList_Widget(self.pushups) 
        
        vLayout.addWidget(profileGUI)
        hLayout.addWidget(pushupsList)
        innerVLayout.addWidget(QLabel("More info (TODO)"))
        innerVLayout.addWidget(addPushupBtn)
        hLayout.addLayout(innerVLayout)
        
        vLayout.addLayout(hLayout)
        
                        
        
        self.mainWidget.setLayout(vLayout)
        self.setCentralWidget(self.mainWidget)
    
    def _pushupForm(self):
        dialog = PushupForm(self.athlete)
        dialog.exec_()
        
    def _createMenus(self):
        self._createActions()
        
        fileMenu = self.menuBar().addMenu("File")
        profile = self.menuBar().addMenu("Profile")
        about = self.menuBar().addMenu("About")
        
        fileMenu.addAction(self.exit)
        profile.addAction(self._createProfile)
        about.addAction(self.aboutQtAction)
        about.addAction(self.aboutApplicationAction)

        #self.toolBarArea("te")
    
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
                  displayHeight/2.0 - self._initHeight/2.0)        
        