'''
Created on Aug 20, 2014

@author: davide
'''

from PySide.QtCore import Slot, Signal, QObject

from Model.Pushup import Pushup as Pushup_Model
from Foundation.Pushup import Pushup as Pushup_Database
from View.Widgets.PushupForm import PushupForm

class PushupCreator(QObject):
    '''
    classdocs
    '''
    
    pushupStored = Signal()
    
    def __init__(self, athlete):
        '''
        Constructor
        '''
        
        QObject.__init__(self)
        self.pushupCreation_Dialog = PushupForm(athlete)
        self.pushupCreation_Dialog.pushupCreated.connect(self.storePushup)
        
    def showCreationDialog(self):
        self.pushupCreation_Dialog.exec_()
    
    @Slot(Pushup_Model)
    def storePushup(self, pushup):
        database = Pushup_Database()
        database.store(pushup)
        
        self.pushupStored.emit()
    