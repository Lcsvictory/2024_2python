# week13_A_9_2.py
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
    members = os.listdir(mypath)
    for member in members:
        member_fullname = os.path.join(mypath, member)
        if os.path.isfile(member_fullname):
            file_ext = os.path.splitext(member) # 확장자 기준으로 나눔. [111.cs, .txt]
            if len(file_ext) == 2 and file_ext[-1] == ".txt" :
                number = file_ext[0].strip()
                rooms[number] = []
                with open(member_fullname, 'r', encoding = 'utf-8') as f:
                    for line in f:
                        split_data = line.strip().split("|")
                        if len(split_data) == 2:
                            intime = dt.strptime(split_datas[0].strip(), timeformat)
                            if split_datas[1]:
                                outtime = dt.strptime(split_datas[1].strip(), timeformat)
                            else:
                                outtime = None
                            rooms[number].append({'in':intime, 'out':outtime})
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

    
