'''
Created on Aug 17, 2014

@author: davide
'''

from PySide.QtGui import QWidget, QListWidget, QVBoxLayout, QListWidgetItem

class PushupList(QWidget):
    '''
    classdocs
    '''

    def __init__(self, pushups):
        '''
        Constructor
        '''
        QWidget.__init__(self)
        self.pushups = pushups
        self.createGUI()
    
    def createGUI(self):
        self.layout = QVBoxLayout()
        
        self.pushupsList = QListWidget(self)
        
        for pushup in self.pushups:
            listItem = QListWidgetItem(pushup._athleteName + " " + str(pushup._series) + " " + str(pushup._repetitions))
            self.pushupsList.addItem(listItem)
        
        self.layout.addWidget(self.pushupsList)
        self.setLayout(self.layout)
        