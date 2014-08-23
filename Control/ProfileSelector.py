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
        self.profileSelection = ProfileSelection(self.athletesList)
        
    def getSelectedAthlete(self):
        if self.profileSelection.execDialogWindow() == True :
            selectedAthleteProfile = self.profileSelection.getSelectedProfile()
            return selectedAthleteProfile
            #pushups = self.loadPushups(selectedAthleteProfile._name)
                       
            #mainWindow =  Main_View(selectedAthleteProfile, pushups)  
            #mainWindow.show()
        else :
            return False         
                           
        
        
        