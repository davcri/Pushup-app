'''
Created on Aug 15, 2014

@author: davide
'''

from datetime import datetime

from Foundation.Database import Database
from Model.Pushup import Pushup as Pushup_Model


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
    
    def deletePushup(self, exerciseId):
        connection = Database.connect(self)
        
        connection.execute("DELETE FROM pushup WHERE exerciseId=:id ", {"id": exerciseId})
        connection.execute("DELETE FROM exercise WHERE id=:id",{"id": exerciseId})

        connection.commit()
        connection.close()
    
    def deletePushups(self, exercisesIdList):
        connection = Database.connect(self)
        
        for exerciseId in exercisesIdList:
            connection.execute("DELETE FROM pushup WHERE exerciseId=:id ", {"id": exerciseId})
            connection.execute("DELETE FROM exercise WHERE id=:id",{"id": exerciseId})

        connection.commit()
        connection.close()
    
    def deletePushupsByAthlete(self, athleteName):
        puhsupsList = self.getPushupsByAthlete(athleteName)

        pushupsIdList = []
                
        for pushup in puhsupsList:
            pushupsIdList.append(pushup._id)
        
        self.deletePushups(pushupsIdList)
        
    def getPushupsByAthlete(self, athleteName):
        connection = Database.connect(self)
        
        cursor = connection.execute("SELECT * FROM pushup inner join exercise on " +\
                                    "exerciseId=id WHERE athleteName = :name ORDER BY date",
                                    {"name":athleteName})
        
        pushupsList = []        
        pushupRows = cursor.fetchall()
        
        for row in pushupRows:
            pushupObj = self._getPushupFromRow(row)
            pushupsList.append(pushupObj) 
        
        return pushupsList
        
    
    def getAllPushups(self):
        connection = Database.connect(self)
        
        cursor = connection.execute("SELECT * FROM pushup inner join exercise on exerciseId=id")
        pushupRows = cursor.fetchall()
        #keys = pushupRows[0].keys() # useful to check row keys.
        
        pushupsList = []        
        
        for row in pushupRows:
            pushupObj = self._getPushupFromRow(row)
            pushupsList.append(pushupObj)   
        
        return pushupsList
        
    def _getPushupFromRow(self, row):
        dateString = row["date"]
        
        dateObj = datetime.strptime(dateString, "%Y-%m-%d").date()
        
        pushupObj = Pushup_Model(row["athleteName"],
                                 dateObj, 
                                 row["avgHeartRate"], 
                                 row["series"],
                                 row["repetitions"])
        pushupObj.setId(row["exerciseId"])
           
        return pushupObj