'''
Created on Aug 17, 2014

@author: davide
'''

from PySide.QtGui import QWidget, QLabel, QVBoxLayout

class Profile(QWidget):
    '''
    classdocs
    '''

    def __init__(self, athlete):
        '''
        Constructor
        '''
        QWidget.__init__(self)
        self.athlete = athlete
        self.initGUI()
        
    def initGUI(self):
        vLayout = QVBoxLayout()
        
        text = QLabel("<h3><b>Pushup app</b></h3>")
        
        profileInfo = QLabel(str(self.athlete))
        
        vLayout.addWidget(text)
        vLayout.addWidget(profileInfo)
        
        vLayout.addStretch(1)
        self.setLayout(vLayout)
    
        