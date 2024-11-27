import datetime



class TimeStamp:
    def __init__(self, start:datetime.datetime, end:datetime.datetime):
        self.start = start
        self.end = end
    
    def diff_seconds(self):
        if not self.end:
            return (datetime.datetime.now() - self.start).total_seconds()
        return (self.end - self.start).total_seconds()

    def is_not_exit(self):
        if not self.end:
            return True
        return False
    
class Room:
    def __init__(self, number:str, history:list): # 기본값을 빈 리스트로 설정하면 이 클래스의 객체는 빈 리스트를 공유해서 사용한다.
        self.number = number
        self.history = history
    
    def add_timestamp(self, start:datetime.datetime, end:datetime.datetime):
        self.history.append(TimeStamp(start, end))
        