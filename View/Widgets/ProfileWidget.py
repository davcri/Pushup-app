'''
Created on Sep 30, 2014

@author: davide
'''

from PySide.QtCore import QDate
from PySide.QtGui import QDialog, QLabel
from PySide.QtGui import QDoubleSpinBox
from PySide.QtGui import QFormLayout, QVBoxLayout, QHBoxLayout, QPushButton
from PySide.QtGui import QLineEdit, QCalendarWidget, QRadioButton

from Model.Athlete import Athlete


class ProfileWidget():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
#     def getAthleteProfile(self):
#         self._execProfileCreation() # Modal dialog
#         # execProfileCreation sets the self.athleteProfile variable !
#         
#         return self.athleteProfile
        
    def getLayout(self):
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
        
        cancelBtn = QPushButton("Cancel")
        
        btnLayout = QVBoxLayout()
        btnLayout.addWidget(createBtn)
        btnLayout.addWidget(cancelBtn)
        
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
        self.layout.addLayout(btnLayout)
        
        return self.layout