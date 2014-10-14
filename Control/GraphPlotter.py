'''
Created on Aug 21, 2014

@author: davide
'''


class GraphPlotter():
    '''
    classdocs
    '''

    def __init__(self, pushupWidget, pushups):
        '''
        Constructor
        '''
        self.graphWidget = pushupWidget
        self.pushups = pushups
    
    def getGraphWidget(self):
        return self.graphWidget
    
    def initPlotWidget(self):                                            
        #self.graphWidget.clear()
        
        pushupDateList = {} # dictionary initialization
     
        for pushup in self.pushups:
            if not pushupDateList.has_key(pushup._date):
                pushupDateList[pushup._date] = pushup._repetitions
            else :
                pushupDateList[pushup._date] += pushup._repetitions
        
        x = []
        y = []
             
        for k in sorted(pushupDateList.keys()):
            x.append(k)
            y.append(pushupDateList[k])
            
        #self.graphWidget.customPlot(range(len(x)), y) 
    
    def refreshGraph(self, updatedPushups):
        self.pushups = updatedPushups
        self.initPlotWidget()
        
        