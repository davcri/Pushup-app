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

    def __init__(self, athlete, pushups):
        '''
        Constructor
        '''
        
        self.athlete = athlete    
        self.pushups = pushups
        self.pushupsListWidget = PushupList_Widget(self.pushups)
        self.pushupsListWidget._deletePushup.connect(self._deletePushup) 
        
    # Slot    
    def refreshList(self):
        updatedPushups = self._getPushups()
        self.pushupsListWidget.reloadPushupsList(updatedPushups)
    
    # Slot
    @Slot(int)
    def _deletePushup(self, pushupId):
        database = Pushup_Database()
        database._deletePushup(pushupId)
        self.refreshList() 
                
    def getListWidget(self):
        return self.pushupsListWidget     
    
    def _getPushups(self):
        database = Pushup_Database()
        pushups = database.getPushupsByAthlete(self.athlete._name)
        
        return pushups
        