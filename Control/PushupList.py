'''
Created on Aug 18, 2014

@author: davide
'''

from PySide.QtCore import Slot 
from View.Widgets.PushupList import PushupList as PushupList_Widget 
from Foundation.Pushup import Pushup as Pushup_Database

class PushupList():
    '''
    classdocs
    '''

    def __init__(self, athlete):
        '''
        Constructor
        '''
        
        self.athlete = athlete    
        self.pushups = self._getPushups()
        self.pushupsListWidget = PushupList_Widget(self.pushups)
        self.pushupsListWidget.deletePushup.connect(self.deletePushup) 
        
    # Slot    
    def refreshList(self):
        updatedPushups = self._getPushups()
        self.pushupsListWidget.reloadPushupsList(updatedPushups)
    
    # Slot
    @Slot(int)
    def deletePushup(self, pushupId):
        database = Pushup_Database()
        database.deletePushup(pushupId)
        self.refreshList() 
                
    def getListWidget(self):
        return self.pushupsListWidget     
    
    def _getPushups(self):
        database = Pushup_Database()
        pushups = database.getPushupsByAthlete(self.athlete._name)
        
        return pushups
        