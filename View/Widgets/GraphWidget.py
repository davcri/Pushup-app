'''
Created on Aug 21, 2014

@author: davide
'''

#import pyqtgraph as pqt_graph

import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

from PySide.QtGui import QSizePolicy

class GraphWidget(FigureCanvas):
    '''
    classdocs
    '''
    def __init__(self, parent=None, width=1, height=1, dpi=100):
        '''
        Constructor
        '''       
        fig = Figure(figsize=(width, height), 
                     dpi=dpi, 
                     frameon = False)
        self.axes = fig.add_subplot(1,1,1)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)
        
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.updateGeometry()
        
    def drawGraph(self, x, y):
        self.axes.plot(x,y)
        self.axes.grid('on')
        
        self.draw()