import datetime
import os
import room

dFormat = "%Y-%m-%d %H:%M:%S"
folder = "C:\\room3"



def diff_seconds(start, end):
    if not end:
        return (datetime.datetime.now() - start).total_seconds()
    return (end - start).total_seconds()

if __name__ == "__main__" :
    
    
    if not os.path.isdir(folder):
        os.mkdir(folder)
        
    def read_file(folder, number):
        try:
            print(f"{number} 대여 기록")
            with open(os.path.join(folder, number+".txt"), "r", encoding="utf-8") as f:
                while line := f.readline():
                    temp = line.strip().split("|")
                    rnumber = temp[0]
                    start = datetime.datetime.strptime(temp[1], dFormat)
                    if not temp[2]:
                        end = None
                    else:
                        end = datetime.datetime.strptime(temp[2], dFormat)
                    
                    print(f"{rnumber} {start} {end}", end=" ")
                    print(diff_seconds(start, end))
        except:
            print(f"{number} 강의실의 대여 기록이 존재하지 않습니다.")
                
    room_numbers = [i.replace(".txt", "") for i in os.listdir(folder) if ".txt" in i]
    for room_number in room_numbers:
        read_file(folder, room_number)
        
    rooms = []
    while True:
        number = input("강의실 호수 : ").strip()
        if not number:
            break
        
        while True:
            start = input("시작 시간 : ").strip()
            if not start: #대여 시간이 비어있다.
                continue
            try:
                start = datetime.datetime.strptime(start, dFormat)
            except:
                print("올바른 시간 형식으로 입력해주세요. ex)2024-01-01 23:59:02")
                continue
            break # try문을 정상 통과 했다. 종료.
        
        while True:
            end = input("종료 시간 : ").strip()
            if not end:
                end = None
                break
            try:
                end = datetime.datetime.strptime(end, dFormat)
            except:
                print("올바른 시간 형식으로 입력해주세요. ex)2024-01-01 23:59:02")
                continue
            break

        flag = 0
        if rooms:
            for room1 in rooms:
                if room1.number == number:
                    room1.add_timestamp(start, end)
                    flag = 1
                    break
        if flag == 0:# rooms리스트에 동일한 roomnumber가 없을때
            rooms.append(room.Room(number, [room.TimeStamp(start, end)]))

    for room1 in rooms:
        for history in room1.history:
            print(f"{room1.number} {history.start} {history.end}", end=" ")
            print(history.diff_seconds())

    
    for room1 in rooms:
        with open(os.path.join(folder, room1.number+".txt"),"a",encoding="utf-8") as f:
            number = room1.number
            for history in room1.history:
                start = history.start.strftime(dFormat)
                if not history.end:
                    end = ""
                else:
                    end = history.end.strftime(dFormat)
                f.write(f"{number}|{start}|{end}\n")
