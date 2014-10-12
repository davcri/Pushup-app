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

    def __init__(self, athlete=False):
        '''
        Constructor
        '''
        QWidget.__init__(self)
            
        self.initGUI()
        
        if athlete is not False:
            self.athlete = athlete
            self.setProfile(athlete)
        
    def initGUI(self):
        self.vLayout = QVBoxLayout()
        
        text = QLabel("<h3><b>Your profile</b></h3>")
        
        profileLayout = QFormLayout()
        
        self.nameLabel = QLabel()
        self.surnameLabel = QLabel()
        self.ageLabel = QLabel()
        self.bmiLabel = QLabel()
        self.heightLabel = QLabel()
        self.massLabel = QLabel()
        
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
    
    def setProfile(self, athlete):
        self.athlete = athlete
        
        self.nameLabel.setText(self.athlete._name)
        self.surnameLabel.setText(self.athlete._surname)      
        self.ageLabel.setText(str(self.athlete.getAge()))
        self.bmiLabel.setText(str(self.athlete.getBMI()))
        self.heightLabel.setText(str(self.athlete._height) + " cm")
        self.massLabel.setText(str(self.athlete._mass) + " Kg")
        