'''
Created on Aug 15, 2014

@author: davide
'''

from Foundation.Database import Database
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
    
        