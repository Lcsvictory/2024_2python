import datetime
import os

mypath = "C:\\202001098-1"
dFormat = "%Y-%m-%d %H:%M:%S"

mlt = []

class Room:
    def __init__(self, number):
        self.number = number
        self.history = []

    def add_timestamp(self, intime, outtime):
        self.history.append(TimeStamp(intime, outtime))

class TimeStamp:
    def __init__(self, intime, outtime=None):
        self.intime = intime
        self.outtime = outtime
    def diff_seconds(self):
        if self.outtime:
            return (self.outtime - self.intime).total_seconds()
        return (datetime.datetime.now() - self.intime).total_seconds()
    def is_rent(self): #대여중입니까?
        #대여중이면 yes, 대여중이 아니면 no
        if not self.outtime:
            return True
        return False

def select():
    print("#"*40)
    print("A. 기존자료복원")
    print("B. 강의실 대여")
    print("C. 강의실 반납")
    print("D. 전체조회")
    print("Q. 종료 및 저장")
    print("#"*40)
    print(">", end=" ")
    user = input().strip().upper()
    return user

def rent():
    while True:
        number = input("강의실 번호 : ").strip()
        if not number:
            print("강의실 번호는 필수입니다.")
            continue
        break
    flag = 0
    room1 = None
    for room in mlt:
        if room.number == number:
            flag = 1
            if room.history[-1].is_rent():
                print("해당 강의실은 대여중입니다. ")
                return
            else:
                room1 = room
    if flag == 0:     
        room1 = Room(number)
        mlt.append(room1)
        
    while True:
        intime = input("대여 시작 시간 : ").strip()
        if not intime:
            #auto_gen()
            break
        try:
            intime = datetime.datetime.strptime(intime, dFormat)
        except:
            print("올바른 형식이 아닙니다.")
            continue
        break
    room1.add_timestamp(intime,None)
    print("정상 대여 처리되었습니다.")

def rent_over():
    if not mlt:
        print("대여 기록이 존재하지 않습니다.")
        return
    number = input("강의실 번호 : ").strip()
    for room in mlt:
        if room.number == number:
            if room.history[-1].is_rent(): # 대여중이라면 반납이 가능하니까.
                while True:
                    outtime = input("반납 시간 : ").strip()
                    if not outtime:
                        outtime = datetime.datetime.now().replace(microsecond=0)
                        break
                    else:
                        try:
                            outtime = datetime.datetime.strptime(outtime, dFormat)
                        except:
                            print("올바른 형식이 아닙니다.")
                            continue
                        break
                room.history[-1].outtime = outtime
                print("반납 처리 되었습니다.")
                return
            else:
                print("해당 강의실은 대여중이 아닙니다.")
                return
    print("해당 강의실의 대여 기록이 없습니다.")

def view_room():
    if not mlt:
        print("기존 데이터가 존재하지 않습니다.")
        return
    for room in mlt:
        print(f"[{room.number}호 대여기록]")
        for i, history in enumerate(room.history):
            print(f"    [{i+1}] 대여시작 : {history.intime} 대여종료 : {history.outtime} 대여기간(일) : {int(history.diff_seconds()/60/60/24)}")
        print()

def write_file():
    if not os.path.isdir(mypath):
        os.mkdir(mypath)
        
    if not mlt:
        print("기존 데이터가 존재하지 않습니다.")
        return
    cnt = 0
    for room in mlt:
        with open(os.path.join(mypath, room.number+".txt"), "w", encoding="utf-8") as f:
            number = room.number
            for history in room.history:
                intime = history.intime.strftime(dFormat)
                if not history.outtime:
                    f.write(f"{intime}")
                    cnt += 1
                else:
                    outtime = history.outtime.strftime(dFormat)
                    f.write(f"{intime}|{outtime}\n")
                    cnt += 1
    print(f"{cnt}건의 데이터를 저장했습니다.")

def read_file():
    if not os.path.isdir(mypath):
        os.mkdir(mypath)
    files = os.listdir(mypath)
    if len(files) == 0:
        print("복원할 데이터가 없습니다.")
        return
    if mlt:
        print("기존 자료와의 충돌이 발생할 수 있으므로 복원 불가")
        return
    numbers = [number for number in files if os.path.splitext(number)[-1] == ".txt" and len(number.split(".")) == 2]
    cnt = 0
    for number in numbers:
        room1 = Room(number.split(".")[0])
        mlt.append(room1)
        with open(os.path.join(mypath, number), "r", encoding="utf-8") as f:
            while line:= f.readline():
                splits = line.strip().split("|")
                if len(splits) == 2:
                    intime = datetime.datetime.strptime(splits[0], dFormat)
                    outtime = datetime.datetime.strptime(splits[1], dFormat)
                    room1.add_timestamp(intime, outtime)
                    cnt +=1 
                elif len(splits) == 1:
                    intime = datetime.datetime.strptime(splits[0], dFormat)
                    outtime = None
                    room1.add_timestamp(intime, outtime)
                    cnt += 1
                else:
                    print("잘못된 데이터가 포함되어 있습니다.")
                    return
    print(f"{cnt}건의 데이터를 복원했습니다.")
if __name__ == "__main__":
    
    while True:
        sel = select()

        if sel == "A":
            read_file()
        elif sel == "B":
            rent()
        elif sel == "C":
            rent_over()
        elif sel == "D":
            view_room()
        elif sel == "Q":
            write_file()
            break
        else:
            print("잘못 선택하셨습니다.")

    print("프로그램을 종료합니다.")
