'''
Created on Aug 16, 2014

@author: davide
'''

from PySide.QtGui import QDialog, QLabel
from PySide.QtGui import QFormLayout, QVBoxLayout,QHBoxLayout, QPushButton
from PySide.QtGui import QLineEdit, QCalendarWidget, QRadioButton
from PySide.QtGui import QDoubleSpinBox
from PySide.QtCore import QDate

from datetime import date

from Model.Athlete import Athlete
 
class ProfileCreation(QDialog):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        QDialog.__init__(self)
        self.athleteProfile = False
        
    def getAthleteProfile(self):
        self.execProfileCreation() # Modal dialog
        # execProfileCreation sets the self.athleteProfile variable !
        
        return self.athleteProfile
        
    def execProfileCreation(self):
        self.layout = QVBoxLayout()
        self.form = QFormLayout()
        
        #--------------------------------
        self.name = QLineEdit()
        self.surname = QLineEdit()
        
        self.birthdate = QCalendarWidget()
        self.birthdate.setGridVisible(True)
        self.birthdate.setMinimumDate(QDate(1850,1,1))
        self.birthdate.setMaximumDate(QDate.currentDate())
        
        self.male = QRadioButton("Male")
        self.male.setChecked(True)
        self.female = QRadioButton("Female")
        
        self.height = QDoubleSpinBox()
        self.height.setMaximum(250)
        self.height.setMinimum(50)
        self.height.setValue(165)
        self.height.setSuffix(" cm")
        
        self.mass = QDoubleSpinBox()
        self.mass.setMaximum(300)
        self.mass.setMinimum(20)
        self.mass.setValue(60)
        self.mass.setSuffix(" Kg")
        
        createBtn = QPushButton("Create")
        createBtn.setDefault(True)
                
        self.form.addRow("Name", self.name)
        self.form.addRow("Surname", self.surname)
        self.form.addRow("Birth date",self.birthdate)
        
        sexLayout = QHBoxLayout()
        sexLayout.addWidget(self.male)
        sexLayout.addWidget(self.female)
        self.form.addRow("Sex", sexLayout)
        
        self.form.addRow("Height", self.height)
        self.form.addRow("Mass", self.mass)
                
        self.layout.addWidget(QLabel("<h3>Create your profile!</h3><hr>"))
        self.layout.addLayout(self.form)
        self.layout.addWidget(createBtn)
        
        createBtn.clicked.connect(self.createProfile)
    
        #--------------------------------
        
        self.setLayout(self.layout)
        
        return self.exec_()
    
    # Slot     
    def createProfile(self):                
        print "Profile creation"
        
        qDate = self.birthdate.selectedDate()
        birthDate = self.qDate_to_date(qDate)
        
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