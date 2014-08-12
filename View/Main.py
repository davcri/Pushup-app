'''
Created on Aug 11, 2014

@author: davide
'''

import sys 
import PySide

#from PySide.QtCore import 
from PySide.QtCore import QSize
from PySide.QtGui import QApplication
from PySide.QtGui import QMessageBox
from PySide.QtGui import QLabel
from PySide.QtGui import QWidget
from PySide import QtCore
from PyQt4 import QtGui

#from PySide.QtGui import QMainWindow 

 
class Main:
    def __init__(self): 
        # Create the application object 
        self._app = QApplication(sys.argv)
        
        self._minWidth = 800
        self._minHeight = 600
        
        self._displayWidth = QApplication.desktop().width()
        self._displayHeight = QApplication.desktop().height()        
        
    def showMainWindow(self):
        mainWindow = QWidget()
        mainWindow.setMinimumSize(QSize(self._minWidth, self._minHeight))
        mainWindow.move(self._displayWidth/2.0 -self._minWidth/2.0, 
                        self._displayHeight/2.0 -self._minHeight/2.0)
                                  
        label = QLabel("Push app", mainWindow)
        
        mainWindow.show()
        
        self._app.exec_()
            
    def showVersion(self):
        pySideV = "<b>PySide</b> version : " + PySide.__version__
        QtCoreV = "<b>QtCore</b> version : " + PySide.QtCore.__version__
        
        msgBox = QMessageBox()
        msgBox.setText(pySideV + "<br>" + QtCoreV)
        msgBox.exec_()
        