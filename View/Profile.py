'''
Created on Aug 17, 2014

@author: davide
'''

from PySide.QtGui import QWidget, QLabel, QVBoxLayout

class Profile(QWidget):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        QWidget.__init__(self)
        vLayout = QVBoxLayout()
        
        text = QLabel("<h3><b>Pushup app</b></h3>")
        
        vLayout.addWidget(text)
        vLayout.addStretch(1)
        self.setLayout(vLayout)
    
        