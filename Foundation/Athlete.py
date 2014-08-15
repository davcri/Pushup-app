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
        connection = Database.connect(self)
        #connection = sqlite3.connect(self._databaseName)
        #connection.row_factory = sqlite3.Row
        
        result = connection.execute("SELECT * FROM athlete WHERE name=:searchParam",
                                    {"searchParam" :athleteName})
        result = result.fetchall()
                
        i=0
        row = []
        for i in range(len(result)):
            row = result[i]
            i += 1
        
        if i>1 :
            print "Database corrupted. More than one tuple for the same Primary Key"
            athlete = False
        else :                        
            if len(row) == 0 :
                print "Error. No profile found for " + "'" +athleteName + "'"
                athlete = False   
            else:
                #converting a string into a date object
                birthDateString = row["birthDate"]
                birthDate = self.stringToDate(birthDateString)
                
                athlete = Model.Athlete.Athlete(row["name"],
                                                row["surname"],
                                                row["sex"],
                                                birthDate,
                                                row["height"],
                                                row["mass"])                
        return athlete
    
    def store(self, athlete):    
        if self.nameAlreadyExists(athlete._name):
            print "Error: Name '" + athlete._name + "' already taken.\n" 
        else:
            database = Database.connect(self)
                    
            database.execute("INSERT INTO athlete VALUES (:name, :surname, :sex, :birthDate, :height, :mass)",
                             {"name": athlete._name, "surname": athlete._surname,
                              "sex":athlete._sex, "birthDate":athlete._birthDate,
                              "height":athlete._height, "mass":athlete._mass})
                   
            database.commit()
            database.close()

    def nameAlreadyExists(self, name):
        connection = Database.connect(self)
        
        cursor = connection.execute("SELECT * FROM athlete WHERE name==:name", {"name": name})
        result = cursor.fetchall()
        
        if len(result) == 0:
            nameAlreadyExists = False
        else:
            nameAlreadyExists = True
        
        cursor.close()
        
        return nameAlreadyExists        
        
    def stringToDate(self, string):
        #strptime() allows to convert a string into a datetime object
        datetimeObj = datetime.datetime.strptime(string, "%Y-%m-%d")
        
        #date() allows to convert a datetime object to a date object
        dateObj = datetimeObj.date()
    
        return dateObj