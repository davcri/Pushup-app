'''
Created on Aug 17, 2014

@author: davide
'''

from PySide.QtCore import Qt, Signal
from PySide.QtGui import QWidget, QVBoxLayout, QListWidgetItem
from PySide.QtGui import QTreeWidget, QTreeWidgetItem, QAction, QMenu, QCursor
                         
class PushupList(QWidget):
    '''
    classdocs
    ''' 
    
    deletePushup = Signal(int)
    deletePushups_in_a_day = Signal(tuple)
    
    def __init__(self, pushups):
        '''
        Constructor
        '''
        QWidget.__init__(self)
        
        self.pushups = pushups
        self.createGUI()
    
    def createGUI(self):
        self.layout = QVBoxLayout()
        # self.pushupsListWidget = QListWidget(self)
        self.pushupsListWidget = QTreeWidget(self)
        
        self.pushupsListWidget.setMinimumHeight(250)        
        #self.pushupsListWidget.setMaximumWidth(500)
        self.pushupsListWidget.setAlternatingRowColors(True)
        
        self.pushupsListWidget.doubleClicked.connect(self.doubleClick_Test)
        
        self.pushupsListWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.pushupsListWidget.customContextMenuRequested.connect(self._customMenu)
        
        self._populateTree()
        
        self.layout.addWidget(self.pushupsListWidget)
        
        self.setLayout(self.layout)   
    
    # Slot
    def _customMenu(self):
        selectedItems = self.pushupsListWidget.selectedItems()
        
        if selectedItems is not None :
            selectedItem = selectedItems[0] 
            
            if selectedItem.parent() is not None : # Child Item selected
                menu = QMenu()
                
                delete = QAction(self.pushupsListWidget)
                delete.setText("Delete this pushup")
                delete.triggered.connect(self._emitDeleteSignal)
                menu.addAction(delete)
                menu.exec_(QCursor.pos())
            else : # Top level Item selected
                menu = QMenu()
             
                delete = QAction(self.pushupsListWidget)
                delete.setText("Delete this day and all of its exercises")
                delete.triggered.connect(self._emitDeleteDaySignal)
                menu.addAction(delete)
                menu.exec_(QCursor.pos())
    
    def _emitDeleteSignal(self):
        selectedItem = self.pushupsListWidget.selectedItems()[0]
        pushupId = selectedItem.data(0, Qt.UserRole)._id
        
        self.deletePushup.emit(pushupId)
    
    def _emitDeleteDaySignal(self):
        selectedItem = self.pushupsListWidget.selectedItems()[0]
        
        treeWidgetItems = selectedItem.takeChildren()
        
        pushupsIdList = []
        for item in treeWidgetItems:
            pushup = item.data(0, Qt.UserRole)._id
            pushupsIdList.append(pushup)
            
        self.deletePushups_in_a_day.emit(pushupsIdList)

    def _populateTree(self):
        self.pushupsListWidget.clear()
        self.pushupsListWidget.setColumnCount(4)
        self.pushupsListWidget.setHeaderLabels(["Date", "TotalPushups", 
                                                "Series", "Repetitions",
                                                "Average Heart Rate"])
        self.pushupsListWidget.setSortingEnabled(True)
        self.pushupsListWidget.setColumnWidth(0, 180)
        self.pushupsListWidget.setColumnWidth(4, 150)
        
        pushupDict = self._getPushupDictionary()
        
        for it, dayOfExercise in enumerate(sorted(pushupDict.keys())):                  
             
            dateItem = QTreeWidgetItem()
            
            dayLabel = dayOfExercise.strftime("%Y/%m/%d")
            
            dateItem.setText(0, "\n" + dayLabel + "\nDay : " + str(it))
            
            self.pushupsListWidget.addTopLevelItem(dateItem)
            
            totalPushups = 0
            for pushup in pushupDict[dayOfExercise]:
                pushupItem = QTreeWidgetItem()
                
                pushupItem.setText(2, "#" + str(pushup._series))
                pushupItem.setText(3, str(pushup._repetitions))
                pushupItem.setText(4, str(pushup._averageHeartRate))
                pushupItem.setData(0, Qt.UserRole, pushup)
                
                totalPushups = totalPushups + pushup._repetitions 
                
                dateItem.addChild(pushupItem)  
            
            dateItem.setText(1, str(totalPushups))
                 
                
    def doubleClick_Test(self):
        selectedItems = self.pushupsListWidget.selectedItems()
        
        if selectedItems is not None :
            selectedItem = selectedItems[0] 
            
            if selectedItem.parent() is not None : # Child Item selected
                selectedPushups = self.pushupsListWidget.selectedItems()[0].data(0, Qt.UserRole)
                print selectedPushups._id    
            else :
                print "Top level widget double clicked"                
        
    def reloadPushupsList(self, pushups):
        self.pushups = pushups
        self._populateTree()
        
    def _populateListWidget(self):
        ''' 
        unused old method
        '''
        
        self.pushupsListWidget.clear()
        
        pushupDict = self._getPushupDictionary()
        
        for dayOfExercise in pushupDict:                  
            listItemString = "Date : " + dayOfExercise + "\n"
            listItem_Data = []
            
            for pushup in pushupDict[dayOfExercise]:
                listItemString += "Series : " + str(pushup._series) + \
                                  " Repetition : " + str(pushup._repetitions) + "\n"
                listItem_Data.append(pushup)
                             
            listItem = QListWidgetItem(listItemString)
            listItem.setData(Qt.UserRole, listItem_Data)
            
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        