# week13_A_11_4.py
# id:20240000
# name:jang eunmee

#TimeStamp만 사용하는 코드 해보기 .
import datetime as dt
import os
from week13_A_room import Room2 as Room
from week13_A_room import TimeStamp
import random

timeformat = "%Y-%m-%d %H:%M:%S"
mypath = "c:\\room2_2400001"

# A1_10~A1_99
# S2_10~S2_99

def gen_room_number() -> str:
    room_type = ['A', 'S']
    room_level = f"{random.randint(1, 8)}"
    #room_level = str(random.randint(1, 8)) # 1 ~ 8
    room_num = f"{random.randrange(10, 100, 1)}" # 10 ~ 99
    room_choice_type = random.choice(room_type)
    return f"{room_choice_type}{room_level}_{room_num}"

def gen_intime():
    h = random.randint(0,8)
    m = random.randint(0,60)
    return dt.datetime.now() - dt.timedelta(hours=h, minutes=m)

def gen_outtime():
    h = random.randint(0,8)
    m = random.randint(0,60)
    return dt.datetime.now() + dt.timedelta(hours=h, minutes=m)


if __name__ == "__main__":
    if not os.path.isdir(mypath):
        os.mkdir(mypath)

    rooms = []

    # 파일이 있으면 읽어서 rooms에 복구한다.
    members = os.listdir(mypath)
    for member in members:
        member_fullname = os.path.join(mypath, member)
        if os.path.isfile(member_fullname):
            file_ext = os.path.splitext(member) # 확장자 기준으로 나눔. [111.cs, .txt]
            if len(file_ext) == 2 and file_ext[-1] == ".txt" :
                number = file_ext[0].strip()
                #rooms[number] = []
                room = Room(number)
                rooms.append(room)
                with open(member_fullname, 'r', encoding = 'utf-8') as f:
                    for line in f:
                        split_data = line.strip().split("|")
                        if len(split_data) == 2:
                            intime = dt.datetime.strptime(split_data[0].strip(), timeformat)
                            if split_data[1]:
                                outtime = dt.datetime.strptime(split_data[1].strip(), timeformat)
                            else:
                                outtime = None
                            room.add_timestamp(intime, outtime)

    while True:
        room = input("대여 여부(y):").strip()
        if not room:
            break
        room = gen_room_number()
        saerch_room = [room_info for room_info in rooms if room_info.number == room]

        
        if not saerch_room:
            room_info = Room(room)
            rooms.append(room_info)
        else:
            room_info = saerch_room[0]
            #if room_info.history[-1].is_rent():
            for timestamp in room_info.history:
                if timestamp.is_rent():
                    #반납 코드 
                    print("대여중입니다.")
                    continue

                
        while True:
            try:
                starttime = input("시작시간:").strip()
                if starttime:
                    starttime = dt.datetime.strptime(starttime, timeformat)
                    break
                else:
                    starttime = gen_intime()
                    break
            except:
                starttime = gen_intime()
                break
                pass

        while True:
            try:
                stoptime = input("종료시간:").strip()
                if not stoptime:
                    stoptime = None
                else:
                    stoptime = dt.datetime.strptime(stoptime, timeformat)
                break
            except:
                pass
        
        #room_info = {"num": room, "in": starttime, "out": stoptime}
        #rooms.append(room_info)
        room_info.add_timestamp(starttime, stoptime)

        fullfile = os.path.join(mypath, room+".txt")
        
        with open(fullfile, "a", encoding='utf-8') as f:
            intime = starttime.strftime(timeformat)
            if stoptime != None:
                outtime = stoptime.strftime(timeformat)
                f.write(f"{intime}|{outtime}\n")
            else:
                f.write(f"{intime}|")
    for room_info in rooms:
        print(room_info.number)
        for timestamp in room_info.history:
            print(timestamp.intime, timestamp.outtime)
            print(timestamp.diff_seconds())

    
