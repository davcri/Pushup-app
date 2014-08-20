'''
Created on Aug 15, 2014

@author: davide
'''

from Foundation.Database import Database
from Model.Pushup import Pushup as Pushup_Model
#from Foundation.Exercise import Exercise

class Pushup(Database):
    def __init__(self):
        Database.__init__(self)
    
    def store(self, pushup):
        
        connection = Database.connect(self)
        
        connection.execute("INSERT INTO exercise VALUES (null, :athleteName, :date, :avgHeartRate)", 
                          {"athleteName":pushup._athleteName, "date":pushup._date, "avgHeartRate": pushup._averageHeartRate})
        
        cursor = connection.execute("SELECT max(id) as lastId FROM exercise")
        exerciseId = cursor.fetchone()["lastId"]
        

        connection.execute("INSERT INTO pushup VALUES(:exerciseId, :repetitions, :series)",
                           {"exerciseId":exerciseId, "repetitions":pushup._repetitions, "series":pushup._series})
         
        connection.commit()
        connection.close()
    
    
    def getPushupsByAthlete(self, athleteName):
        connection = Database.connect(self)
        
        cursor = connection.execute("SELECT * FROM pushup inner join exercise on " +\
                                    "exerciseId=id WHERE athleteName = :name",
                                    {"name":athleteName})
        
        pushupsList = []        
        pushupRows = cursor.fetchall()
        
        for row in pushupRows:
            pushupObj = self._loadPushupFromRow(row)
            pushupsList.append(pushupObj) 
                   
        return pushupsList
        
    
    def getAllPushups(self):
        connection = Database.connect(self)
        
        cursor = connection.execute("SELECT * FROM pushup inner join exercise on exerciseId=id")
        pushupRows = cursor.fetchall()
        #keys = pushupRows[0].keys() # useful to check row keys.
        
        pushupsList = []        
        
        for row in pushupRows:
            pushupObj = self._loadPushupFromRow(row)
            pushupsList.append(pushupObj)   
        
        return pushupsList
    
    def deletePushup(self, id):
        connection = Database.connect(self)
        
        connection.execute("DELETE FROM pushup WHERE exerciseId=:id ", {"id":id})
        connection.commit()
        connection.close()
        
        
    def _loadPushupFromRow(self, row):
        pushupObj = Pushup_Model(row["athleteName"],
                                 row["date"], 
                                 row["avgHeartRate"], 
                                 row["series"],
                                 row["repetitions"])
        pushupObj.setId(row["exerciseId"])
           
        return pushupObj
        