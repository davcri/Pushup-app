'''
Created on Aug 11, 2014

@author: davide
'''

from Model.Athlete import Athlete
import Foundation.Database
import Foundation.Athlete
import View.Main
import datetime
from Foundation.Database import Database

class Main():
    def __init__(self):
        view =  View.Main.Main()        
        #view.showVersion()
        #view.showMainWindow() 
        
        selectedProfile = "Davide" # hard coded
        
        athleteDb = Foundation.Athlete.Athlete()
        print athleteDb.load(selectedProfile)
        
        #exercisesList = ["flessioni", "flessioni super potenti"]
        #person = Athlete("Davide", "Cristini", "Male", datetime.date(1991,8,10), "187", "70", exercisesList)
