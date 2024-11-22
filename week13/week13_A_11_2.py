
import datetime
import os
import room

dFormat = "%Y-%m-%d %H:%M:%S"

mypath = "c:\\room2_202001098"
# myfile = "list.txt"
# fullfile = os.path.join(mypath, myfile)


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
    def read_file(mypath, room_number, room_datas):
        try:
            with open(os.path.join(mypath, room_number+".txt"), "r", encoding="utf-8") as f:
                while line := f.readline():
                    temp = line.strip().split("|")
                    temp[1] = datetime.datetime.strptime(temp[1],dFormat)
                    if temp[2]:
                        temp[2] = datetime.datetime.strptime(temp[2], dFormat)
                    else:
                        temp[2] = None
                    flag = 0
                    if room_datas:
                        for room_data in room_datas:
                            if room_data.room_number == room_number:
                                room_data.add_timestamp(temp[1], temp[2])
                                flag = 1
                        if not flag:
                            room_datas.append(room.Room2(room_number, [room.TimeStamp(temp[1], temp[2])]))
                    else:
                        room_datas.append(room.Room2(room_number, [room.TimeStamp(temp[1], temp[2])]))     
                    
                        
        except Exception as e:
            print(e)
            print("기존 데이터가 존재하지 않습니다.")
    
    
    room_numbers = [i.replace(".txt", "") for i in os.listdir(mypath) if ".txt" in i]
    for room_number in room_numbers:
        read_file(mypath, room_number, room_datas)
        
    print("복구한 정보입니다.")
    for room_data in room_datas:
        print(f"{room_data.room_number} 대여 기록:")
        for i in range(len(room_data.history)):
            print(f"    [{i+1}] start:{room_data.history[i].start} end:{room_data.history[i].end}", end=" ")
            print(f"diff:{room_data.history[i].diff_seconds()}")
        
        
    while True:
        temp = {}
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
        
        # 데이터를 구분하자
        flag = 0
        if room_datas:
            for room_data in room_datas:
                if room_data.room_number == room_number:
                    room_data.add_timestamp(start, end)
                    flag = 1
            if not flag:
                room_datas.append(room.Room2(room_number, [room.TimeStamp(start, end)]))
        else:
            room_datas.append(room.Room2(room_number, [room.TimeStamp(start, end)]))
        


    for room_data in room_datas:
        print(f"{room_data.room_number} 대여 기록:")
        for i in range(len(room_data.history)):
            print(f"    [{i+1}] start:{room_data.history[i].start} end:{room_data.history[i].end}", end=" ")
            print(f"diff:{room_data.history[i].diff_seconds()}")

    for room_data in room_datas:
        with open(os.path.join(mypath, room_data.room_number+".txt"), "w", encoding="utf-8") as f:
            #파일에 정보를 기록해라.
            for timestamp in room_data.history:
                start = timestamp.start.strftime(dFormat) #datetime -> str
                if end := timestamp.end: # 있으면
                    end = end.strftime(dFormat) #datetime -> str
                else: #없으면 (None이면)
                    end = ""
                f.write(f"{room_data.room_number}|{start}|{end}\n")

    
