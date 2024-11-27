#week13_A_room.py

from datetime import datetime as dt


class TimeStamp:
    def __init__(self, intime, outtime=None):
        self.intime = intime
        self.outtume = outtime

    def is_rent(self):
        return not self.outtime
    
    def diff_seconds(self):
        if self.outtime:
            return (self.outtime - self.intime).totalseconds()
        return (dt.now() - self.intime).totalseconds()
    
class Room2:
    def __init__(self, number):
        self.number = number
        self.history = []

    def add_timestamp(self, intime, outtime):
        self.history.append(TimeStamp(intime, outtime))


    
