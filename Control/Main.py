'''
Created on Aug 11, 2014

@author: davide
'''

from Model.Athlete import Athlete
import Foundation.Database
import View.Main
import datetime
from Foundation.Database import Database

class Main():
    def __init__(self):
        view =  View.Main.Main()        
        #view.showVersion()
        #view.showMainWindow()
        
        mydb = Database()
        return 
        
        selectedProfile = dict([("Name","Davide"), ("Surname","Cristini")])
        
        exercisesList = ["flessioni", "flessioni super potenti"]
        person = Athlete("Davide", "Cristini", "Male", datetime.date(1991,8,10), "187", "70", exercisesList)
        
        print person