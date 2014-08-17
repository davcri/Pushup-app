'''
Created on Aug 11, 2014

@author: davide
'''

import PySide
from PySide.QtCore import QSize
from PySide.QtGui import QApplication, QMainWindow
from PySide.QtGui import QLabel, QVBoxLayout
from PySide.QtGui import QMessageBox
from PySide.QtGui import QWidget

from View.Profile import Profile 
 
class MainWindow(QMainWindow):
    def __init__(self, athlete): 
        QMainWindow.__init__(self)
        self.setWindowTitle("Pushup app")       
        
        self._initWidth = 700
        self._initHeight = 600
        self.resize(QSize(self._initWidth, self._initHeight))
        self.centerWindow()
        self.createUI()
            
    def createUI(self):
        self.mainWidget = QWidget()        
        
        verticalLayout = QVBoxLayout()
        
        profileGUI = Profile()
        verticalLayout.addWidget(profileGUI)
                
        self.mainWidget.setLayout(verticalLayout)
        self.setCentralWidget(self.mainWidget)
            
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
        