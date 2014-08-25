'''
Created on Aug 18, 2014

@author: davide
'''
from View.Widgets.ProfileCreation import ProfileCreation as ProfileCreationWidget
from Foundation.Athlete import Athlete

class ProfileCreation():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.pushupCreationDialog = ProfileCreationWidget()         
        
    def runCreationDialog(self):
        return self.pushupCreationDialog.getAthleteProfile()
        
    def runCreationDialogAndStore(self):
        athlete = self.pushupCreationDialog.getAthleteProfile()
        print athlete
         
        if athlete is not False :
            database = Athlete()
            database.store(athlete)
        
    
        