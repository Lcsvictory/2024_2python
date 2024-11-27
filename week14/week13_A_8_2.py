# week13_A_8_2.py
# id:20240000
# name:jang eunmee
import datetime as dt
import os


timeformat = "%Y-%m-%d %H:%M:%S"

mypath = "c:\\room2_2400001"


def diff_seconds(intime, outtime):
    if not outtime:
        outtime = dt.datetime.now()
    return (outtime - intime).total_seconds()


if __name__ == "__main__":
    if not os.path.isdir(mypath):
        os.mkdir(mypath)

    rooms = {}

    # 파일이 있으면 읽어서 rooms에 복구한다.
    

    while True:
        room = input("강의실 호수:").strip()
        if not room:
            break

        if not room in rooms.keys():
            rooms[room] = []
        else:
            for history in rooms[room]:
                if history['out'] == None:
                    #반납 코드 
                    print("대여중입니다.")
                    continue

                
        while True:
            try:
                starttime = input("시작시간:").strip()
                if starttime:
                    starttime = dt.datetime.strptime(starttime, timeformat)
                    break
            except:
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
        rent_info = {"in": starttime, "out": stoptime}
        rooms[room].append(rent_info)

        fullfile = os.path.join(mypath, room+".txt")
        
        with open(fullfile, "a", encoding='utf-8') as f:
            intime = dt.strftime(starttime, timeformat)
            if stoptime != None:
                outtime = dt.strftime(stoptime, timeformat)
                f.write(f"{intime}|{outtime}\n")
            else:
                f.write(f"{intime}|")
    for room, historys in rooms.items():
        print(room)
        for history in historys:
            print(history["in"], history["out"])
            print(diff_seconds(history["in"], history["out"]))

    
