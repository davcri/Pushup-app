'''
Created on Aug 23, 2014

@author: davide
'''

from View.Widgets.ProfileSelection import ProfileSelection

class ProfileSelector():
    '''
    classdocs
    '''
    
    def __init__(self, athletes):
        '''
        Constructor
        '''
        self.athletesList = athletes
        self._profileSelection = ProfileSelection(self.athletesList)
        
    def getSelectedAthlete(self):
        if self._profileSelection.execDialogWindow() == True :
            selectedAthleteProfile = self._profileSelection.getSelectedProfile()
        else :
            selectedAthleteProfile = False         
        
        return selectedAthleteProfile
                           
        
        
        