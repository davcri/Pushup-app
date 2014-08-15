'''
Created on Aug 12, 2014

@author: davide
'''

import sqlite3 
import os
   
class Database:    
    _databaseName = "Push app.db"
    
    def __init__(self):      
        if not self.databaseExists():
            connection = self.connect()

            connection.execute("CREATE TABLE athlete(name text primary key, surname text, sex text, birthDate text, height real, weight real)")                
            connection.execute("CREATE TABLE exercise(athleteName text, date text, avgHearRate real, FOREIGN KEY(athleteName) REFERENCES athlete(name))") 
            # exercise primary key is the rowid column that sqlite generates by default
            # Read http://www.sqlite.org/lang_createtable.html#rowid
        else :
            connection = sqlite3.connect(self._databaseName)
            
        connection.commit()    
        connection.close()      
    
    def connect(self):
        connection = sqlite3.connect(self._databaseName)
        # enables foreign key support
        connection.execute("PRAGMA foreign_keys=ON")
        
        return connection
    
    def databaseExists(self):
        return os.path.isfile(Database._databaseName)