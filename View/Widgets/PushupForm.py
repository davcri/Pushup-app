'''
Created on Aug 17, 2014

@author: davide
'''


from PySide.QtCore import QDate
from PySide.QtGui import QWidget, \
                         QFormLayout, QSpinBox, QCalendarWidget, \
                         QPushButton
from Model.Pushup import Pushup as Pushup_Model
from Foundation.Pushup import Pushup as Pushup_Foundation
from datetime import date

class PushupForm(QWidget):
    '''
    classdocs
    '''
    
    def __init__(self, athlete):
        '''
        Constructor
        '''
        QWidget.__init__(self)
        
        self.athlete = athlete
        self.pushupForm = QFormLayout()
        self.createGUI()
    
    def createGUI(self):
        self.avgHeartRate = QSpinBox()
        self.avgHeartRate.setMinimum(40)
        self.avgHeartRate.setMaximum(250)
        self.avgHeartRate.setValue(120)
        
        self.series = QSpinBox()
        self.series.setMinimum(1)
        
        self.date = QCalendarWidget()
        self.date.setMaximumDate(QDate.currentDate())
        
        self.repetitions = QSpinBox()
        
        self.addButton = QPushButton("Add pushup")
        self.addButton.clicked.connect(self.createPushup)
        
        self.pushupForm.addRow("Average Heart Rate", self.avgHeartRate)
        self.pushupForm.addRow("Series", self.series)
        self.pushupForm.addRow("Repetitions", self.repetitions)
        self.pushupForm.addRow("Exercise Date", self.date)
        
        self.pushupForm.addWidget(self.addButton)
        
        self.setLayout(self.pushupForm)
        
    def createPushup(self):
        print "Storing pushup"
        
        exerciseDate = self.date.selectedDate()
        exerciseDate = self.qDate_to_date(exerciseDate)
        
        pushup = Pushup_Model(self.athlete._name, 
                        exerciseDate, 
                        self.avgHeartRate.value(), 
                        self.series.value(),
                        self.repetitions.value())
        
        db = Pushup_Foundation()
        db.store(pushup)
        
        return pushup
    
    def qDate_to_date(self, qDate):        
        return date(qDate.year(), qDate.month(),qDate.day())
        
        
        