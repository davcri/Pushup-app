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
        self.createGUI()
    
    def createGUI(self):
        self.layout = QVBoxLayout()
        
        self.pushupsList = QListWidget(self)
        self.pushupsList.addItem(QListWidgetItem("asd"))
        
        self.layout.addWidget(self.pushupsList)
        self.setLayout(self.layout)
        