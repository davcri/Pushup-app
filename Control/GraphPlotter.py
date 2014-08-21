'''
Created on Aug 21, 2014

@author: davide
'''

from View.Widgets.PlotWidget import PlotWidget

class GraphPlotter():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
        self.plot = PlotWidget()
    
    def getGraphWidget(self):
        return self.plot
        
        