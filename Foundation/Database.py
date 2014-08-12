'''
Created on Aug 12, 2014

@author: davide
'''

import sqlite3 
import os

databaseName = "push app.db"

def databaseExists():
    return os.path.isfile(databaseName)
    
class Database:    
    def __init__(self):              
               
        if not databaseExists() :
            connection = sqlite3.connect(databaseName)
            connection.execute("CREATE TABLE exercise(athlete text primary key, repetition int, series int, date text)")
        else :
            connection = sqlite3.connect(databaseName)
            pass
        
    def close(self):
        connection.commit()    
        connection.close()      
        
     
#             connection.execute("CREATE TABLE flessioni (ripetizioni int, serie int, data text)")
#         else :
#             connection = sqlite3.connect(databaseName)    
#             currentDate = datetime.today()
#                
#             connection.execute("INSERT INTO flessioni VALUES (?,?,?)", (4, 5, currentDate))
#             x = connection.execute("SELECT * FROM flessioni")
#                 
#             pushupList = x.fetchall()
#             print pushupList
                
              