'''
Created on Aug 17, 2014

@author: davide
'''


from PySide.QtCore import QDate, Qt
from PySide.QtGui import QWidget, QDialog, \
                         QFormLayout, QVBoxLayout, QSpinBox, QCalendarWidget, \
                         QPushButton
from Model.Pushup import Pushup as Pushup_Model
from Foundation.Pushup import Pushup as Pushup_Foundation
from datetime import date

class PushupForm(QDialog):
    '''
    classdocs
    '''
    
    def __init__(self, athlete):
        '''
        Constructor
        '''
        QDialog.__init__(self)
        self.setWindowTitle("Pushup form")
        
        self.athlete = athlete
        self.pushupForm = QFormLayout()
        self.createGUI()
    
    def createGUI(self):
        self.series = QSpinBox()
        self.series.setMinimum(1)
        
        self.repetitions = QSpinBox()
        
        self.avgHeartRate = QSpinBox()
        self.avgHeartRate.setMinimum(40)
        self.avgHeartRate.setMaximum(250)
        self.avgHeartRate.setValue(120)
        
        self.date = QCalendarWidget()
        self.date.setMaximumDate(QDate.currentDate())
        
        self.addButton = QPushButton("Add pushup")
        self.addButton.setMaximumWidth(90)
        self.addButton.clicked.connect(self._createPushup)
        
        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.setMaximumWidth(90)
        self.cancelButton.clicked.connect(self.reject)
        
        self.pushupForm.addRow("Series", self.series)
        self.pushupForm.addRow("Repetitions", self.repetitions)
        self.pushupForm.addRow("Average Heart Rate", self.avgHeartRate)
        self.pushupForm.addRow("Exercise Date", self.date)
        
        btnsLayout = QVBoxLayout()
        btnsLayout.addWidget(self.addButton)
        btnsLayout.addWidget(self.cancelButton)        
        btnsLayout.setAlignment(Qt.AlignRight)
        
        layoutWrapper = QVBoxLayout()
        layoutWrapper.addLayout(self.pushupForm)
        layoutWrapper.addLayout(btnsLayout)
        
        self.setLayout(layoutWrapper)
        
        
    def _createPushup(self):
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
        self.accept()
        
        return pushup
    
    def qDate_to_date(self, qDate):        
        return date(qDate.year(), qDate.month(),qDate.day())
        
        
        