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
        self.pushupsListWidget = QListWidget(self)
        self.pushupsListWidget.setMinimumHeight(250)
        
        self.pushupsListWidget.setAlternatingRowColors(True)
        
        self._populateListWidget()
        
        self.layout.addWidget(self.pushupsListWidget)
        
        self.setLayout(self.layout)
    
    def _populateListWidget(self):
        pushupDict = self._getPushupDictionary()
        
        for dayOfExercise in pushupDict:                  
            listItemContent = "Date : "+ dayOfExercise + "\n"
            
            for pushup in pushupDict[dayOfExercise]:
                listItemContent += "Series : " + str(pushup._series) + " Repetition : " + str(pushup._repetitions) + "\n"
                             
            listItem = QListWidgetItem(listItemContent)
            self.pushupsListWidget.addItem(listItem)
        
            
    def _getPushupDictionary(self):
        '''
        Returns a dictionary with the following structure : 
        - Key : date of the exercises. Type datetime.date
        - Value : list containing pushups made that day . Type : [Pushup model object]    
        
        example : 
        {
            2014-08-18: [pushupModelObj1, pushupModelObj2, pushupModelObj3],
            2014-08-19: [pushupModelObj4, pushupModelObj5, pushupModelObj6]
        } 
        '''
        pushupDateList = {} # dictionary initialization
        
        for pushup in self.pushups:
            if not pushupDateList.has_key(pushup._date):
                pushupsList = [pushup]
                pushupDateList[pushup._date] = pushupsList
            else:
                pushupDateList[pushup._date].append(pushup)
                 
#         for k in pushupDateList.keys():
#             print k
#             
#             for pu in pushupDateList[k]:
#                 print pu
         
        return pushupDateList    
        
        
        
        
        
        
        
        
        
        
        
        
        
        