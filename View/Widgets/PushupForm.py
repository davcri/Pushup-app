'''
Created on Aug 17, 2014

@author: davide
'''

from datetime import date

from PySide.QtCore import Qt, QDate, Signal
from PySide.QtGui import QDialog, QPushButton, QCheckBox
from PySide.QtGui import QFormLayout, QVBoxLayout, QSpinBox, QCalendarWidget
                         
from Model.Pushup import Pushup as Pushup_Model


class PushupForm(QDialog):
    '''
    classdocs
    '''
    pushupCreated = Signal(Pushup_Model)
    
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
        self.repetitions.setMaximum(512)
        
        self.avgHeartRateToggle = QCheckBox()
        self.avgHeartRateToggle.toggled.connect(self._toggleHeartRateSpinBox)
        
        self.avgHeartRate = QSpinBox()
        self.avgHeartRate.setMinimum(30)
        self.avgHeartRate.setMaximum(250)
        self.avgHeartRate.setValue(120)
        self.avgHeartRate.setDisabled(True)
        
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
        self.pushupForm.addRow("Store average heart rate ? ", self.avgHeartRateToggle)
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
        exerciseDate = self.date.selectedDate()
        exerciseDate = self.qDate_to_date(exerciseDate)
        
        if self.avgHeartRateToggle.isChecked():
            heartRate = self.avgHeartRate.value()
        else:
            heartRate = None
            
        pushup = Pushup_Model(self.athlete._name, 
                              exerciseDate, 
                              heartRate, 
                              self.series.value(),
                              self.repetitions.value())

        self.pushupCreated.emit(pushup)
        self.accept()       
    
    def _toggleHeartRateSpinBox(self):
        if self.avgHeartRateToggle.isChecked():
            self.avgHeartRate.setDisabled(False)
        else:
            self.avgHeartRate.setDisabled(True)
        
    def qDate_to_date(self, qDate):        
        return date(qDate.year(), qDate.month(),qDate.day())
        