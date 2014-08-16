'''
Created on Aug 16, 2014

@author: davide
'''

from PySide.QtGui import QWidget, QLabel
from PySide.QtGui import QFormLayout, QVBoxLayout,QHBoxLayout, QPushButton
from PySide.QtGui import QLineEdit, QCalendarWidget, QRadioButton
from PySide.QtGui import QDoubleSpinBox
 
class ProfileCreation(QWidget):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        QWidget.__init__(self)
    
    def execProfileCreation(self):
        self.layout = QVBoxLayout()
        self.form = QFormLayout()
        
        #--------------------------------
        name = QLineEdit()
        surname = QLineEdit()
        birthdate = QCalendarWidget()
        male = QRadioButton("Male")
        female = QRadioButton("Female")
        height = QDoubleSpinBox()
        mass = QDoubleSpinBox()
        createBtn = QPushButton("Create")
                
        self.form.addRow("Name", name)
        self.form.addRow("Surname", surname)
        self.form.addRow("Birth date",birthdate)
        
        sexLayout = QHBoxLayout()
        sexLayout.addWidget(male)
        sexLayout.addWidget(female)
        self.form.addRow("Sex", sexLayout)
        
        self.form.addRow("Height (meters)", height)
        self.form.addRow("Mass (Kilograms)", mass)
                
        self.layout.addWidget(QLabel("<h3>Your profile data</h3><hr>"))
        self.layout.addLayout(self.form)
        self.layout.addWidget(createBtn)
        #--------------------------------
        
        self.setLayout(self.layout)
        self.show()