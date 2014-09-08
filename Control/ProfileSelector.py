'''
Created on Aug 23, 2014

@author: davide
'''

from PySide.QtCore import Slot, QObject

from View.Widgets.ProfileSelection import ProfileSelection as ProfileSelectionWidget

from Foundation.Athlete import Athlete as Athlete_Database

from Model.Athlete import Athlete as Athlete_Model

class ProfileSelector(QObject):
    '''
    classdocs
    '''
    
    def __init__(self, athletes):
        '''
        Constructor
        '''
        QObject.__init__(self)
        
        self.selectedProfile = False
        self.athletesList = athletes
        self._profileSelection = ProfileSelectionWidget(self.athletesList)
        
        self._profileSelection.profileSelected.connect(self.saveSelectedProfile)
        self._profileSelection.removeProfile.connect(self.removeProfile)
        
        self._profileSelection.exec_()
        
    def getSelectedAthlete(self):
        return self.selectedProfile 
    
    @Slot(Athlete_Model)
    def saveSelectedProfile(self, selectedProfile):
        self.selectedProfile = selectedProfile
    
    @Slot(Athlete_Model)
    def removeProfile(self, athlete):
        database = Athlete_Database()
        
        database.delete(athlete._name)