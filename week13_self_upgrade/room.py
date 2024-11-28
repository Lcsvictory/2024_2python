import datetime


class Room:
    def __init__(self, number:str):
        self.number = number
        self.history = []
    def add_timestamp(self, intime, outtime):
        self.history.append(TimeStamp(intime, outtime))

class TimeStamp:
    def __init__(self, intime, outtime = None):
        self.intime = intime
        self.outtime = outtime

    def diff_seconds(self):
        if self.outtime:
            return (self.outtime - self.intime).total_seconds()
        return (datetime.datetime.now() - self.intime).total_seconds()

    def is_rent(self):
        if self.outtime:
            if self.outtime >= datetime.datetime.now():
                return False
            if self.outtime <= datetime.datetime.now():
                return True
        else:
            return False
