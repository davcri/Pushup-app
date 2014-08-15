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
        Database.__init__(self)
        
    def load(self, athleteName):
        connection = sqlite3.connect(self._databaseName)
        connection.row_factory = sqlite3.Row
        
        result = connection.execute("SELECT * FROM athlete WHERE name=:searchParam", {"searchParam" :athleteName})
        result = result.fetchall()
                
        i=0
        for i in range(len(result)):
            row = result[i]
            i += 1
        
        if i>1 :
            print "Database corrupted. More than one tuple for the same Primary Key"
            athlete = False
        else :                        
            if len(row) == 0 :
                print "Error. No profile found for " + "'" +athleteName + "'"   
                   
            #converting a string into a datetime object
            birthDateString = row["birthDate"]
            birthDate = datetime.datetime.strptime(birthDateString, "%Y-%m-%d")
            
            athlete = Model.Athlete.Athlete(row["name"],
                                            row["surname"],
                                            row["sex"],
                                            birthDate,
                                            row["height"],
                                            row["weight"])
                
        return athlete
    
    def store(self, athlete):       
        database = sqlite3.connect(self._databaseName)
        
        database.execute("INSERT INTO athlete VALUES (:name, :surname, :sex, :birthDate, :height, :weight)", {"name": athlete._name, "surname": athlete._surname, "sex":athlete._sex, "birthDate":athlete._birthDate, "height":athlete._height, "weight":athlete._weight})
               
        database.commit()
        database.close()