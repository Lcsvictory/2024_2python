
import datetime


def diff_seconds(start, end):
    if not end:
        end = datetime.datetime.now()
    temp = end - start
    return temp.total_seconds()
#print(diff_seconds(datetime.datetime.now(), datetime.datetime(2024,10,10, 10, 5, 10)))


#dFormat = "%Y-%m-%d %H:%M:%S.%f"
dFormat = "%Y-%m-%d %H:%M:%S"

room_datas = []
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
        elif end: #종료시간이 있다.
            try:
                end = datetime.datetime.strptime(end, dFormat)
            except:
                #비 정상적인 출차시간 일때.
                continue
            break
        
    temp['room_number'] = room_number
    temp['start'] = start
    temp['end'] = end
    room_datas.append(temp)


for room_data in room_datas:
    print(room_data['room_number'], room_data['start'], room_data['end'])
    print(diff_seconds(room_data['start'], room_data['end']))



    
