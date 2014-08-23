'''
Created on Aug 21, 2014

@author: davide
'''

import pyqtgraph as pqt_graph

class GraphWidget(pqt_graph.PlotWidget):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pqt_graph.setConfigOption('background', (255,255,255))
        pqt_graph.setConfigOption('foreground', (0,0,0))
        pqt_graph.setConfigOption('plot', 'k')
        pqt_graph.setConfigOption('antialias',True)
        
        pqt_graph.PlotWidget.__init__(self)
        
    def customPlot(self, x,y):     
        penStyle = pqt_graph.mkPen((0,0,0,100), width=1.5)   
        
        self.showGrid(True,True)
        self.setLabel('left', "Total Pushups")
        self.setLabel('bottom', "Day")
        self.plot(x, y, pen=penStyle, symbolBrush=(80,100,255), symbolPen='w')
        

        
        
        
            
        