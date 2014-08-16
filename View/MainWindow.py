'''
Created on Aug 11, 2014

@author: davide
'''

#import sys 
import PySide
from PySide.QtCore import QSize
from PySide.QtGui import QApplication, QMainWindow, QPushButton
from PySide.QtGui import QLabel, QComboBox, QVBoxLayout, QHBoxLayout
from PySide.QtGui import QMessageBox, QDialog
from PySide.QtGui import QWidget

#from PySide.QtGui import QMainWindow 

 
class MainWindow(QMainWindow):
    def __init__(self): 
        QMainWindow.__init__(self)
        self.setWindowTitle("Pushup app")       
        
        self._initWidth = 700
        self._initHeight = 600
        self.resize(QSize(self._initWidth, self._initHeight))
        self.centerWindow()
        self.addStuff()
            
    def addStuff(self):
        self.mainWidget = QWidget()        
        
        verticalLayout = QVBoxLayout()
        
        
        text = QLabel("<h3><b>Pushup app</b></h3>")
        
        verticalLayout.addWidget(text)
        
        verticalLayout.addStretch(1)
        
        go_button = QPushButton('&Go')
        verticalLayout.addWidget(go_button)
                 
        comboBox = QComboBox()
        comboBox.addItem("pappa")
        comboBox.addItem("asd")
        comboBox.addItem("gr")
        verticalLayout.addWidget(comboBox)        
        
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
        