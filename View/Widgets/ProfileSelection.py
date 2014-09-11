'''
Created on Aug 16, 2014

@author: davide
'''

from PySide.QtCore import Signal, Qt
from PySide.QtGui import QDialog
from PySide.QtGui import QHBoxLayout, QVBoxLayout
from PySide.QtGui import QLabel, QPushButton, QListWidget 
from PySide.QtGui import QListWidgetItem, QIcon
from PySide.QtGui import QAbstractItemView

from Model.Athlete import Athlete as Athlete_Model
 
class ProfileSelection(QDialog):
    '''
    classdocs
    '''
    
    removeProfile = Signal(Athlete_Model)
    profileSelected = Signal(Athlete_Model)
    lastProfileDeleted = Signal()
    
    def __init__(self, athletesList):
        '''
        Constructor
        '''  
        QDialog.__init__(self)
        self.setWindowTitle("Profile Selection")
        
        self.athletesList = athletesList
        self.selectedProfile = False
        
        self._initGUI()      
    
    def _initGUI(self):
        hLayout = QHBoxLayout()
        vLayout = QVBoxLayout()
        
        # Label
        greeterText = QLabel("Welcome to <b>Pushup app</b>." + \
                             "<br><br> Select a profile:")
        vLayout.addWidget(greeterText)        
            
        # List 
        self.list = QListWidget()
        self.list.setSelectionMode(QAbstractItemView.SingleSelection)
        # SingleSelection is the default value, but I prefer to be sure
        self.list.itemSelectionChanged.connect(self._activateButtons) 
        
        for athlete in self.athletesList:
            iconW = QIcon.fromTheme("user-available")
            # doens't work on Mac and Windows
            # http://qt-project.org/doc/qt-4.8/qicon.html#fromTheme
            
            listW = QListWidgetItem(iconW, athlete._name)
            listW.setData(Qt.UserRole, athlete)
            
            self.list.addItem(listW)
                
        vLayout.addWidget(self.list)
        
        vLayout.addLayout(hLayout)
        
        # Buttons
        self.okBtn = QPushButton("Ok")
        self.okBtn.setDisabled(True)
        self.okBtn.clicked.connect(self._okButtonSlot)
        self.list.itemDoubleClicked.connect(self._okButtonSlot)
                
        cancelBtn = QPushButton("Cancel")      
        cancelBtn.clicked.connect(self._cancelButtonSlot)
        
        self.removeProfileBtn = QPushButton("Remove Profile")
        self.removeProfileBtn.setDisabled(True)
        self.removeProfileBtn.clicked.connect(self._emitRemoveProfile)
        
        hLayout.addWidget(self.okBtn)
        hLayout.addWidget(cancelBtn)
        hLayout.addWidget(self.removeProfileBtn)        

        self.setLayout(vLayout)
            
    def _emitRemoveProfile(self):
        selectedListItem = self.list.selectedItems()[0]
        athlete = selectedListItem.data(Qt.UserRole)
        
        rowToDelete = 0
        for index, element in enumerate(self.athletesList):
            if element == athlete:
                rowToDelete = index
                
        self.list.takeItem(rowToDelete)
        self.athletesList.remove(athlete)        
        self.removeProfile.emit(athlete)
    
    def _okButtonSlot(self):
        athlete = self.list.selectedItems()[0].data(Qt.UserRole)
        
        self.accept() # is it correct ? Maybe self.close() is better ?
        # Or should I redefine the accept() method ?
        
        #athleteProfile = self.getSelectedProfile()
        
        self.profileSelected.emit(athlete)
    
    def _cancelButtonSlot(self):
        if len(self.athletesList) == 0:
            self.lastProfileDeleted.emit()
        
        self.reject()
    
    def _activateButtons(self):
        selectedItems = self.list.selectedItems()
        
        if len(selectedItems)!=0 :
            self.okBtn.setDisabled(False)
            self.removeProfileBtn.setDisabled(False)
        else :
            self.okBtn.setDisabled(True)
            self.removeProfileBtn.setDisabled(True)
        