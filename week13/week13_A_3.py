# week13_A_3.py
# id:202001098
# name:Lee chungseong

room_datas = []
while True:
    temp = {}
    room_number = input("강의실 호수:").strip()
    if not room_number:
        break
    start = input("시작시간:")
    end = input("종료시간:")
    temp['room_number'] = room_number
    temp['start'] = start
    temp['end'] = end
    room_datas.append(temp)

for room_data in room_datas:
    print("강의실 호수 : " + room_data['room_number'], "시작시간 : " + room_data['start'], "종료시간 : " + room_data['end'])
