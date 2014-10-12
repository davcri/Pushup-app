'''
Created on Aug 18, 2014

@author: davide
'''

from PySide.QtCore import Slot, Signal, QObject

from View.Widgets.ProfileCreation import ProfileCreation as ProfileCreationWidget
from Foundation.Athlete import Athlete as Athlete_Foundation
from Model.Athlete import Athlete as Athlete_Model

class ProfileCreation(QObject):
    '''
    classdocs
    '''
    
    profileCreated = Signal(Athlete_Model)
    
    def __init__(self):
        '''
        Constructor
        '''
        QObject.__init__(self)
        
        self.profileCreationDialog = ProfileCreationWidget()   
        self.profileCreationDialog.profileCreated.connect(self.storeProfile)
        self.profileCreationDialog.buttonBox.rejected.connect(self.reject)
        
    def run(self):
        self.profileCreationDialog.exec_()
    
    @Slot(Athlete_Model)
    def storeProfile(self, athlete):
        self.profileCreationDialog.accept() # Close the dialog window
        self.profileCreated.emit(athlete) # Propagate the profile created signal
          
        database = Athlete_Foundation()
        database.store(athlete)
            
    @Slot()
    def reject(self):
        self.profileCreationDialog.reject()