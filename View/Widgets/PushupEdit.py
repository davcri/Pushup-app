'''
Created on Aug 20, 2014

@author: davide
'''

from PySide.QtGui import QDialog, QPushButton, QHBoxLayout, QVBoxLayout

class PushupEdit(QDialog):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
        QDialog.__init__(self)
        self._initGUI()
        
    def _initGUI(self):
        #layout = QFormLayout()
        hLayout = QHBoxLayout()
        vLayout = QVBoxLayout()
        
        self.okBtn = QPushButton("Ok")
        self.cancelBtn = QPushButton("Cancel")
        self.okBtn.clicked.connect(self.accept)
        self.cancelBtn.clicked.connect(self.reject)
        
        hLayout.addWidget(self.okBtn)
        hLayout.addWidget(self.cancelBtn)
        
        vLayout.addLayout(hLayout)
        self.setLayout(vLayout)
        