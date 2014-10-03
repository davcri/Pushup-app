'''
Created on Aug 16, 2014

@author: davide
'''

from PySide.QtCore import Signal
from PySide.QtGui import QDialog
from PySide.QtGui import QDialogButtonBox
from PySide.QtGui import QLabel
from PySide.QtGui import QVBoxLayout
from PySide.QtGui import QPushButton

from Model.Athlete import Athlete
from View.Widgets.ProfileWidget import ProfileWidget
 
class ProfileCreation(QDialog):
    '''
    classdocs
    '''
    profileCreated = Signal(Athlete)
    
    def __init__(self):
        '''
        Constructor
        '''
        QDialog.__init__(self)
        
        self._initGUI()
        self.athleteProfile = False
    
    def _initGUI(self):
        self.setWindowTitle("Profile Creation")
        self.profileWidget = ProfileWidget()
        
        self.profileLayout = self.profileWidget.getLayout()
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel)
        self.okBtn = QPushButton("Ok")
        self.okBtn.setDefault(True)
        self.okBtn.clicked.connect(self._createProfile)
        self.buttonBox.addButton(self.okBtn, QDialogButtonBox.AcceptRole)
        
        vLayout = QVBoxLayout()
        vLayout.addWidget(QLabel("<h3>Create a new profile!</h3><hr>"))
        vLayout.addLayout(self.profileLayout)
        vLayout.addWidget(self.buttonBox)
        
        self.setLayout(vLayout)        

    def _createProfile(self):
        athleteProfile = self.profileWidget.getProfile()
        self.profileCreated.emit(athleteProfile)