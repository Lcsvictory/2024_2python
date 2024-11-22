
import datetime

#dFormat = "%Y-%m-%d %H:%M:%S.%f"
dFormat = "%Y-%m-%d %H:%M:%S"

room_datas = []
while True:
    temp = {}
    room_number = input("강의실 호수:").strip()
    if not room_number:
        break
    start = input("시작시간:").strip()
    end = input("종료시간:").strip()
    start = datetime.datetime.strptime(start, dFormat)
    end = datetime.datetime.strptime(end, dFormat)
    
    temp['room_number'] = room_number
    temp['start'] = start
    temp['end'] = end
    room_datas.append(temp)


for room_data in room_datas:
    print(room_data['room_number'], room_data['start'], room_data['end'])
