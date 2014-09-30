'''
Created on Aug 18, 2014

@author: davide
'''

from PySide.QtCore import Slot

from View.Widgets.ProfileCreation import ProfileCreation as ProfileCreationWidget
from Foundation.Athlete import Athlete as Athlete_Foundation
from Model.Athlete import Athlete as Athlete_Model

class ProfileCreation():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.profileCreationDialog = ProfileCreationWidget()   
        self.profileCreationDialog.profileCreated.connect(self.storeProfile)
        self.profileCreationDialog.buttonBox.rejected.connect(self.reject)
        
    def run(self):
        self.profileCreationDialog.exec_()
    
    @Slot(Athlete_Model)
    def storeProfile(self, athlete):
        self.profileCreationDialog.accept() # close the dialog window
        self.profileCreationDialog.profileWidget.getProfile()
          
        database = Athlete_Foundation()
        database.store(athlete)
            
    @Slot()
    def reject(self):
        self.profileCreationDialog.reject()