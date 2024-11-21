import datetime

class Room1:
    def __init__(self, number:str, start:datetime.datetime, end:datetime.datetime):
        self.room_number = number
        self.start = start
        self.end = end
    
    def diff_seconds(self):
        if not self.end:
            return (datetime.datetime.now() - self.start).total_seconds()
        temp = self.end - self.start
        return temp.total_seconds()
    
    
class TimeStamp:
    def __init__(self, start:datetime.datetime, end:datetime.datetime):
        self.start = start
        self.end = end
    
    def diff_seconds(self):
        if not self.end:
            return (datetime.datetime.now() - self.start).total_seconds()
        temp = self.end - self.start
        return temp.total_seconds()
    
    def is_not_exit(self):
        if self.end:
            return True
        return False
    
class Room2:
    def __init__(self, number:str, history:list):
        self.room_number = number
        self.history = history
        
    def add_timestamp(self, start, end):
        self.history.append(TimeStamp(start, end))