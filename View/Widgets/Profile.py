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
        vLayout = QVBoxLayout()
        
        text = QLabel("<h3><b>Your profile</b></h3>")
        
        profileLayout = QFormLayout()
        
        nameLabel = QLabel(self.athlete._name)
        surnameLabel = QLabel(self.athlete._surname)
        ageLabel = QLabel(str(self.athlete.getAge()))
        bmiLabel = QLabel(str(self.athlete.getBMI()))
        heightLabel = QLabel(str(self.athlete._height) + " cm")
        massLabel = QLabel(str(self.athlete._mass) + " Kg")
        
        profileLayout.addRow("Name", nameLabel)        
        profileLayout.addRow("Surname", surnameLabel)
        profileLayout.addRow("Age", ageLabel)
        profileLayout.addRow("Body Mass Index", bmiLabel)
        profileLayout.addRow("Height", heightLabel)
        profileLayout.addRow("Mass", massLabel)
                
        vLayout.addWidget(text)
        vLayout.addLayout(profileLayout)
        
        vLayout.addStretch(1)
        self.setLayout(vLayout)
    
        