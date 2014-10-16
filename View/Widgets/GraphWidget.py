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
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        '''
        Constructor
        '''
    
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(1,1,1)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
        #self.figure = Figure(figsize=(100,100), dpi=72, facecolor=(0.9,1,1), edgecolor=(0,0,0))
        #FigureCanvas.__init__(self, self.figure)        
 
 
            
#         pqt_graph.setConfigOption('background', (255,255,255))
#         pqt_graph.setConfigOption('foreground', (0,0,0))
#         pqt_graph.setConfigOption('plot', 'k')
#         pqt_graph.setConfigOption('antialias',True)
#         
#         pqt_graph.PlotWidget.__init__(self)
        
#    def customPlot(self, x,y):     
#         penStyle = pqt_graph.mkPen((0,0,0,100), width=1.5)   
#         
#         self.showGrid(True,True)
#         self.setLabel('left', "Total Pushups")
#         self.setLabel('bottom', "Day")
#         self.plot(x, y, pen=penStyle, symbolBrush=(80,100,255), symbolPen='w')