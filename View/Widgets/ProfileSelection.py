'''
Created on Aug 16, 2014

@author: davide
'''

from PySide.QtCore import Signal, Qt
from PySide.QtGui import QDialog
from PySide.QtGui import QMessageBox
from PySide.QtGui import QHBoxLayout, QVBoxLayout
from PySide.QtGui import QLabel, QPushButton, QListWidget 
from PySide.QtGui import QListWidgetItem, QIcon
from PySide.QtGui import QAbstractItemView

from Model.Athlete import Athlete as Athlete_Model
from View.Widgets.ProfileFormWidget import ProfileFormWidget
 
class ProfileSelection(QDialog):
    '''
    classdocs
    '''
    
    removeProfile = Signal(Athlete_Model)
    profileSelected = Signal(Athlete_Model)
    profileUpdate_request = Signal(Athlete_Model, Athlete_Model)
    lastProfileDeleted = Signal()
    
    def __init__(self, athletesList):
        '''
        Constructor
        '''  
        QDialog.__init__(self)
        self.setWindowTitle("Profile Selection")
        
        self.athletesList = athletesList
            
        self._initGUI()      
    
    def _initGUI(self):
        topHLayout = QHBoxLayout()
        hLayout = QHBoxLayout()
        vLayout = QVBoxLayout()
        
        # Label
        greeterText = QLabel("Welcome to <b>Pushup app</b>." + \
                             "<br><br> Select a profile:")
        vLayout.addWidget(greeterText)        
            
        # List 
        self.list = QListWidget()
        self.list.setMinimumWidth(150)
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
        
        topHLayout.addWidget(self.list)
        self.profileWidget = ProfileFormWidget()
        self.profileWidget.hide()
        
        topHLayout.addWidget(self.profileWidget)    
       
        vLayout.addLayout(topHLayout)        
        vLayout.addLayout(hLayout)
        
        # Buttons
        self.okBtn = QPushButton("Ok")
        self.okBtn.setDisabled(True)
        self.okBtn.setDefault(True)
        self.okBtn.clicked.connect(self._okButtonSlot)
        self.list.itemDoubleClicked.connect(self._okButtonSlot)
                
        cancelBtn = QPushButton("Cancel")      
        cancelBtn.clicked.connect(self._cancelButtonSlot)
        
        self.editBtn = QPushButton("Edit")
        self.editBtn.setDisabled(True)
        self.editBtn.setCheckable(True)
        self.editBtn.clicked.connect(self._toggleProfileEdit)
        
        self.saveBtn = QPushButton("Save changes") # Saves the changes made on the profile 
        self.saveBtn.hide()
        self.saveBtn.clicked.connect(self._saveButtonSlot)
    
        self.removeProfileBtn = QPushButton("Remove Profile")
        self.removeProfileBtn.setDisabled(True)
        self.removeProfileBtn.clicked.connect(self._removeProfile_Dialog)
        
        hLayout.addWidget(self.editBtn)
        hLayout.addWidget(self.removeProfileBtn)
        hLayout.addWidget(cancelBtn)
        hLayout.addWidget(self.okBtn)
        hLayout.addWidget(self.saveBtn)

        self.setLayout(vLayout)
    
    def getSelectedProfile(self):
        selectedListItem = self.list.selectedItems()[0]
        athleteProfile = selectedListItem.data(Qt.UserRole)
        
        return athleteProfile
    
    def updateList(self, athletes):
        self.list.clear()
        self.athletesList = athletes
        
        for athlete in self.athletesList:
            iconW = QIcon.fromTheme("user-available")
            # doens't work on Mac and Windows
            # http://qt-project.org/doc/qt-4.8/qicon.html#fromTheme
           
            listW = QListWidgetItem(iconW, athlete._name)
            listW.setData(Qt.UserRole, athlete)
           
            self.list.addItem(listW)
    
    def resetWidget(self):
        """ Resets the widget to the initial laoyout. 
        
        Should be used only in specific cases
        """
        self.editBtn.setChecked(False)
        self._toggleProfileEdit()
            
    def _removeProfile_Dialog(self):
        """Runs a prompt dialog.
        
        Ask the user if he really wants to remove the selected profile.
        """
        confirmationDialog = QMessageBox()
        confirmationDialog.setText("Do you really want to remove the selected profile ?")
        confirmationDialog.setInformativeText("Profile deletion can not be undone")
        confirmationDialog.setIcon(QMessageBox.Question)
        confirmationDialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirmationDialog.accepted.connect(self._emitRemoveProfile)
        ret = confirmationDialog.exec_()
        
        if ret==QMessageBox.Yes:
            self._emitRemoveProfile()
                
    def _emitRemoveProfile(self):
        athlete = self.getSelectedProfile()
        
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
    
    def _saveButtonSlot(self):
        selectedProfile = self.getSelectedProfile()
        updatedProfile = self.profileWidget.getProfile()
    
        self.profileUpdate_request.emit(selectedProfile, updatedProfile)
        
        #self._toggleProfileEdit()
        
    def _toggleProfileEdit(self):
        if self.editBtn.isChecked():
            self.profileWidget.setProfile(self.getSelectedProfile())
            self.profileWidget.show()
            self.saveBtn.show()
            self.okBtn.hide()
            self.removeProfileBtn.hide()
        else:
            self.saveBtn.hide()
            self.profileWidget.hide()
            self.okBtn.show()
            self.removeProfileBtn.show()
    
    def _activateButtons(self):
        selectedItems = self.list.selectedItems()
        
        if len(selectedItems)!=0 :
            self.okBtn.setDisabled(False)
            self.removeProfileBtn.setDisabled(False)
            self.editBtn.setDisabled(False)
        else :
            self.okBtn.setDisabled(True)
            self.removeProfileBtn.setDisabled(True)
            self.editBtn.setDisabled(True)