'''
Created on Aug 12, 2014

@author: davide
'''

from Foundation.Database import Database
import Model.Athlete
import sqlite3 

import datetime

class Athlete(Database):    
    def __init__(self):              
        pass
    
    def load(self, primaryKey):
        connection = sqlite3.connect(self._databaseName)
        
#         result = connection.execute("SELECT * FROM exercise WHERE athlete = :primaryKeyParam", {"primaryKeyParam" :primaryKey})
#         exercises = result.fetchall()
#         
        
        athlete = Model.Athlete.Athlete("Da", "surname", "sex", datetime.date.today() , "height", "weight", "exercises")
                
        return athlete
    
    def store(self, athlete):
        pass