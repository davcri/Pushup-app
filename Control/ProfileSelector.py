'''
Created on Aug 23, 2014

@author: davide
'''

from PySide.QtCore import Slot, Signal, QObject

from View.Widgets.ProfileSelection import ProfileSelection as ProfileSelectionWidget
from Foundation.Athlete import Athlete as Athlete_Database
from Model.Athlete import Athlete as Athlete_Model

class ProfileSelector(QObject):
    '''
    classdocs
    '''
    
    profileSelected = Signal(Athlete_Model)
    profileDeleted = Signal(Athlete_Model)
    lastProfileDeleted = Signal()
    
    def __init__(self, athletes):
        '''
        Constructor
        '''
        QObject.__init__(self)
        
        self.selectedProfile = False
        self.athletesList = athletes
        self._profileSelection = ProfileSelectionWidget(self.athletesList)
        
        self._profileSelection.profileSelected.connect(self._propagateProfileSelected)
        self._profileSelection.removeProfile.connect(self.removeProfile)
    
    def runSelectionDialog(self):
        self._profileSelection.exec_()
            
    def getSelectedAthlete(self):
        return self.selectedProfile 
    
    @Slot(Athlete_Model)
    def _propagateProfileSelected(self, selectedProfile):
        """ Propagates the profileSelected signal """
        self.selectedProfile = selectedProfile
        self.profileSelected.emit(selectedProfile)
        
    @Slot(Athlete_Model)
    def removeProfile(self, athlete):
        database = Athlete_Database()
        database.delete(athlete._name)
        
        self.profileDeleted.emit(athlete)
        
        if database.countAthletes() == 0 :
            self.lastProfileDeleted.emit()