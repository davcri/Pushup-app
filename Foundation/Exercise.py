'''
Created on Aug 11, 2014

@author: davide
'''

from Foundation.Database import Database

class Exercise(Database):
    def __init__(self):
        Database.__init__(self)
        pass
    
    def add(self, exercise):        
        connection = Database.connect(self)
                        
        connection.execute("INSERT INTO exercise VALUES (:athleteName, :date, :avgHeartRate)", {"athleteName":exercise._athleteName, "date":exercise._date, "avgHeartRate": exercise._averageHeartRate})
        
        connection.commit()
        connection.close()
                
    def load(self):      
        #result = connection.execute("SELECT * FROM exercise WHERE athlete = :primaryKeyParam", {"primaryKeyParam" :primaryKey})
        #exercises = result.fetchall()
        pass
      