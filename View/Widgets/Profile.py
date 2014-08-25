'''
Created on Aug 17, 2014

@author: davide
'''

from PySide.QtGui import QWidget, QLabel
from PySide.QtGui import QFormLayout, QVBoxLayout

class Profile(QWidget):
    '''
    classdocs
    '''

    def __init__(self, athlete):
        '''
        Constructor
        '''
        QWidget.__init__(self)
        self.athlete = athlete
        self.initGUI()
        
    def initGUI(self):
        self.vLayout = QVBoxLayout()
        
        text = QLabel("<h3><b>Your profile</b></h3>")
        
        profileLayout = QFormLayout()
        
        self.nameLabel = QLabel(self.athlete._name)
        self.surnameLabel = QLabel(self.athlete._surname)
        self.ageLabel = QLabel(str(self.athlete.getAge()))
        self.bmiLabel = QLabel(str(self.athlete.getBMI()))
        self.heightLabel = QLabel(str(self.athlete._height) + " cm")
        self.massLabel = QLabel(str(self.athlete._mass) + " Kg")
        
        profileLayout.addRow("Name", self.nameLabel)        
        profileLayout.addRow("Surname", self.surnameLabel)
        profileLayout.addRow("Age", self.ageLabel)
        profileLayout.addRow("Body Mass Index", self.bmiLabel)
        profileLayout.addRow("Height", self.heightLabel)
        profileLayout.addRow("Mass", self.massLabel)
                
        self.vLayout.addWidget(text)
        self.vLayout.addLayout(profileLayout)
        
        self.vLayout.addStretch(1)
        self.setLayout(self.vLayout)
    
    def refreshProfile(self, athlete):
        self.athlete = athlete
        
        self.nameLabel.setText(self.athlete._name)
        self.surnameLabel.setText(self.athlete._surname)      
        self.ageLabel.setText(str(self.athlete.getAge()))
        self.bmiLabel.setText(str(self.athlete.getBMI()))
        self.heightLabel.setText(str(self.athlete._height) + " cm")
        self.massLabel.setText(str(self.athlete._mass) + " Kg")
        