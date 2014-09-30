'''
Created on Aug 16, 2014

@author: davide
'''

from datetime import date

from PySide.QtGui import QDialog, QLabel
from PySide.QtGui import QFormLayout, QVBoxLayout,QHBoxLayout, QPushButton
from PySide.QtGui import QLineEdit, QCalendarWidget, QRadioButton
from PySide.QtGui import QDoubleSpinBox
from PySide.QtCore import QDate

from Model.Athlete import Athlete
from View.Widgets.ProfileWidget import ProfileWidget
 
class ProfileCreation(QDialog):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        QDialog.__init__(self)
        self.setWindowTitle("Profile Creation")
        self.athleteProfile = False
        
    def getAthleteProfile(self):
        self._execProfileCreation() # Modal dialog
        # execProfileCreation sets the self.athleteProfile variable !
        
        return self.athleteProfile
        
    def _execProfileCreation(self):
        profileWidget = ProfileWidget()
        
        self.setLayout(profileWidget.getLayout())
        
        return self.exec_()
    
    # Slot     
    def _createProfile(self):                
        print "Profile creation"
        
        qDate = self.birthdate.selectedDate()
        birthDate = self.qDate_to_date(qDate)
        print birthDate
        
        self.athleteProfile = Athlete(self.name.text(),
                                 self.surname.text(),
                                 self._getSex(),
                                 birthDate,
                                 self.height.value(),
                                 self.mass.value()) 
        
        self.accept()
        
    def qDate_to_date(self, qDate):        
        return date(qDate.year(), qDate.month(),qDate.day())
    
    def _getSex(self):
        if (self.male.isChecked()):
            return "Male"
        elif (self.female.isChecked()):
            return "Female"
        else :
            print "Error: No sex selected"
            return False