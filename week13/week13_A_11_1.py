# week13_A_11_1.py
# id:202001098
# name:Lee chungseong

import datetime
import os
import room

dFormat = "%Y-%m-%d %H:%M:%S"

mypath = "c:\\room1_202001098"
myfile = "list.txt"
fullfile = os.path.join(mypath, myfile)


def diff_seconds(start, end):
    if not end:
        end = datetime.datetime.now()
    temp = end - start
    return temp.total_seconds()


if __name__ == "__main__":
    if not os.path.isdir(mypath):
        os.mkdir(mypath)

    room_datas = []
    
    #파일이 있으면 기존 내용에 추가해야하니까. 
    
    def read_file(fullfile, room_datas):
        try:
            with open(fullfile, "r", encoding="utf-8") as f:
                while line := f.readline():
                    temp = line.strip().split("|")
                    temp[1] = datetime.datetime.strptime(temp[1],dFormat)
                    if temp[2]:
                        temp[2] = datetime.datetime.strptime(temp[2], dFormat)
                    else:
                        temp[2] = None
                    room_instance = room.Room1(temp[0], temp[1], temp[2])
                    room_datas.append(room_instance)
        except Exception as e:
            print(e)
            print("기존 데이터가 존재하지 않습니다.")
            
            
    read_file(fullfile, room_datas)
    print("복구한 정보입니다.")
    for room_data in room_datas:
        print(room_data.room_number, room_data.start, room_data.end)
        
    
    while True:
        room_number = input("강의실 호수:").strip()
        if not room_number:
            break
        
        while True:
            start = input("시작시간:").strip() 
            if start: #시작시간이 있다. 없으면 다시.
                try:
                    start = datetime.datetime.strptime(start, dFormat)
                except:
                    #비 정상적인 시작시간 일때.
                    continue
                break
        
        while True:
            end = input("종료시간:").strip()
            if not end:#종료시간이 비어있다.
                end = None
                break
            elif end: #종료시간이 있다.
                try:
                    end = datetime.datetime.strptime(end, dFormat)
                except:
                    #비 정상적인 출차시간 일때.
                    continue
                break
        room_instance = room.Room1(room_number, start, end)
        room_datas.append(room_instance)


    for room_data in room_datas:
        print(room_data.room_number, room_data.start, room_data.end)
        print(room_data.diff_seconds())

    with open(fullfile, "w", encoding="utf-8") as f:
        #파일에 정보를 기록해라.
        for room_data in room_datas:
            room_number = room_data.room_number
            start = room_data.start.strftime(dFormat) #datetime -> str
            if end := room_data.end: # 있으면
                end = end.strftime(dFormat) #datetime -> str
            else: #없으면 (None이면)
                end = ""
            f.write(f"{room_number}|{start}|{end}\n")

    
