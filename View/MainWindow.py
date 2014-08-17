'''
Created on Aug 11, 2014

@author: davide
'''

import PySide
from PySide.QtCore import QSize
from PySide.QtGui import QApplication, QMainWindow
from PySide.QtGui import QVBoxLayout
from PySide.QtGui import QMenuBar, QToolBar, QAction
from PySide.QtGui import QMessageBox, QLabel
from PySide.QtGui import QWidget, QMessageBox

from View.Profile import Profile 
 
class MainWindow(QMainWindow):
    def __init__(self, athlete): 
        QMainWindow.__init__(self)
        self.setWindowTitle("Pushup app")       
        
        self.athlete = athlete
        
        self._initWidth = 700
        self._initHeight = 600
        self.resize(QSize(self._initWidth, self._initHeight))
        self.centerWindow()
        
        self.createUI()        
            
    def createUI(self):
        self.mainWidget = QWidget()
        self._createMenus()
        
        verticalLayout = QVBoxLayout()
        
        profileGUI = Profile(self.athlete)
        verticalLayout.addWidget(profileGUI)
                
        self.mainWidget.setLayout(verticalLayout)
        self.setCentralWidget(self.mainWidget)
    
    def _createMenus(self):
        self._createActions()
        
        fileMenu = self.menuBar().addMenu("File")
        about = self.menuBar().addMenu("About")
        
        fileMenu.addAction(self.exit)
        about.addAction(self.aboutQtAction)
        about.addAction(self.aboutApplicationAction)
        #self.menuBar().addMenu("File")
        #self.toolBarArea("te")
    
    def actionExit(self):
        self.close()
        
    def actionAboutApplication(self):
        text = "Pushup app is a work in progress application.<br><br>\
                For developmente info look at the \
                <a href=\"https://github.com/davcri/Push-up-app\">Github Page</a> <br>"
        QMessageBox.about(self, "About Pushup app", text)   
    
    def actionAboutQt(self):
        QMessageBox.aboutQt(self)
        
    def _createActions(self):             
        self.aboutQtAction = QAction("About PySide (Qt)", self)
        self.aboutApplicationAction = QAction("About Pushup App", self)
        
        self.exit = QAction("Exit", self)   
        
        self.exit.triggered.connect(self.actionExit)
        self.aboutQtAction.triggered.connect(self.actionAboutQt)
        self.aboutApplicationAction.triggered.connect(self.actionAboutApplication)        
        
                
    def centerWindow(self):
        displayWidth = QApplication.desktop().width()
        displayHeight = QApplication.desktop().height()
        
        self.move(displayWidth/2.0 - self._initWidth/2.0, 
                  displayHeight/2.0 - self._initHeight/2.0)        
                
    def showVersion(self):
        pySideV = "<b>PySide</b> version : " + PySide.__version__
        QtCoreV = "<b>QtCore</b> version : " + PySide.QtCore.__version__
        
        msgBox = QMessageBox()
        msgBox.setText(pySideV + "<br>" + QtCoreV)
        msgBox.exec_()
        