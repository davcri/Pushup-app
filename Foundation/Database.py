'''
Created on Aug 12, 2014

@author: davide
'''

import sqlite3 
import os
   
class Database:    
    _databaseName = "Pushup-app.db"
    _databasePath = os.path.dirname(os.path.dirname(__file__)) + "/"
    
    def __init__(self):      
        self._databaseFileName = self._databasePath + self._databaseName
        
        if not self.databaseExists():
            connection = self.connect()

            connection.execute("CREATE TABLE athlete(name text primary key, surname text, sex text, birthDate text, height real, mass real)")                
            connection.execute("CREATE TABLE exercise(id INTEGER primary key, athleteName text, date text, avgHeartRate real, FOREIGN KEY(athleteName) REFERENCES athlete(name))")
            connection.execute("CREATE TABLE pushup(exerciseId int, repetitions int, series int, FOREIGN KEY(exerciseId) REFERENCES exercise(id))") 
                
            print "Database created"
        else :
            connection = sqlite3.connect(self._databaseFileName)
            
        connection.commit()    
        connection.close()      
    
    def connect(self):
        connection = sqlite3.connect(self._databaseFileName)
        # Uses a different row_factory. "Row" enables access to row by name
        connection.row_factory = sqlite3.Row
        # Enables foreign key support
        connection.execute("PRAGMA foreign_keys=ON")
        
        return connection
    
    def databaseExists(self):
        return os.path.isfile(self._databaseFileName)