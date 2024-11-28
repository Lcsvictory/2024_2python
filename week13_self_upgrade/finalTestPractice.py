import datetime
import os
import room

dFormat = "%Y-%m-%d %H:%M:%S"
mypath  = "c:\\room3_202001098"
room_datas = []

def select():
    print("#"*40)
    print("A. 파일 읽기")
    print("B. 대여 가능 목록 보기")
    print("C. 대여하기")
    print("D. 반납하기")
    print("E. 강의실 대여 기록 보기")
    print("Q. 저장 및 종료")
    print("#"*40)
    user_select = input(">> : ").strip().upper()
    return user_select


def rent_room():
    flag = 0
    number = input("강의실 번호 : ").strip()
    if room_datas: # 대여 기록이 있다면
        for room_data in room_datas:
            if room_data.number == number: #방번호 있다면
                flag = 1
                if not room_data.history[-1].is_rent():#is_rent? 즉 대여불가능일때 이 if문이 참이 되야함.
                    print("해당 강의실은 현재 대여중입니다.")
                    return
                else: # 방번호는 있는데 대여중이 아니야.
                    room1 = room_data
        if flag == 0: # 방 번호가 없어.
            room1 = room.Room(number)
            room_datas.append(room1)
    else:
        room1 = room.Room(number)
        room_datas.append(room1)
    while True:
        intime = input("대여 시작 시간 : ").strip()
        if intime:
            try:
                intime = datetime.datetime.strptime(intime, dFormat)
            except:
                print("잘못된 시간 형식입니다. 올바른 시간 형식 2001-01-01 09:00:00")
                continue
            break
        else:
            #자동완성
            print("대여 시작 시간은 반드시 입력해야 합니다.")
            continue
    while True:
        print("7일뒤 반납 : A\n반납 시간 미정 : B")
        aorb = input(">> : ").strip().upper()
        if aorb == "A":
            outtime = intime + datetime.timedelta(days=7)
            break
        elif aorb == "B":
            outtime = None
            break
        else:
            print("잘못된 값입니다.")
            continue
    room1.add_timestamp(intime, outtime)
    print("강의실 대여가 완료되었습니다.")
    return

def return_room():
    if not room_datas:
        print("대여 기록이 존재하지 않습니다.")
        return
    number = input("강의실 번호 : ").strip()
    for room_data in room_datas:
        if room_data.number == number: # 반납하려는 강의실의 대여 기록이 존재함.
            if room_data.history[-1].outtime == None or room_data.history[-1].outtime > datetime.datetime.now():
                room_data.history[-1].outtime = datetime.datetime.now().replace(microsecond=0)
                print("현 시간부로 반납처리 되었습니다.")
                return
            else:
                print("이미 반납 되었습니다.")
                return
    print("해당 강의실은 대여중이지 않습니다.") 


def possible_rent_list():
    # 강의실중에 history[-1].outtime이 현재 시간보다 작거나같으면 가능.
    if room_datas:
        print("[대여 가능 강의실]", " ", "[대여 불가능 강의실]")
        for room_data in room_datas:
            if room_data.history[-1].is_rent():
                print(f"{room_data.number}")
            else:
                print(f"{' '*20}{room_data.number}")
    else:
        print("대여 기록이 존재하지 않습니다.")

def rent_history():
    if room_datas:
        for room_data in room_datas:
            print(room_data.number)
            for i, history in enumerate(room_data.history): 
                print(f"[{i+1}] 시작 : {history.intime} 종료 : {history.outtime} 빌린 날짜 : {int(history.diff_seconds()/60/60/24)}일")
    else:
        print("대여 기록이 존재하지 않습니다.")

def write_file():
    cnt = 0
    if not os.path.isdir(mypath):
        os.mkdir(mypath)
    if room_datas:
        for room_data in room_datas:
            with open(os.path.join(mypath, room_data.number+".txt"),"w", encoding='utf-8') as f:
                for history in room_data.history:
                    intime = history.intime.strftime(dFormat)
                    if history.outtime:
                        outtime = history.outtime.strftime(dFormat)
                        f.write(f"{intime}|{outtime}\n")
                        cnt += 1
                    else:
                        outtime = ""
                        f.write(f"{intime}")
                        cnt += 1
        print(f"{cnt}건의 데이터를 저장했습니다.")
        return
    else:
        print(f"{cnt}건의 데이터를 저장했습니다.")
        return

def read_file():
    if not os.path.isdir(mypath):
        os.mkdir(mypath)
    file_list = os.listdir(mypath)
    txt_files = [txt for txt in file_list if ".txt" in txt]
    numbers = [os.path.splitext(number)[0] for number in txt_files if len(os.path.splitext(number)) == 2]
    if numbers:
        cnt = 0
        for number in numbers:
            room1 = room.Room(number)
            room_datas.append(room1)
            with open(os.path.join(mypath, number+".txt"), "r", encoding="utf-8") as f:
                while line := f.readline():
                    split_datas = line.strip().split("|")
                    if len(split_datas) == 2:
                        outtime = datetime.datetime.strptime(split_datas[1], dFormat)
                    elif len(split_datas) == 1:
                        outtime = None
                    intime = datetime.datetime.strptime(split_datas[0], dFormat)
                    room1.add_timestamp(intime, outtime)
                    cnt += 1
        print(f"{cnt}건의 데이터를 복원했습니다.")
    elif room_datas:
        print("기존에 저장된 데이터 이외의 데이터가 존재합니다. 프로그램을 재시작 해주세요.")
    else:
        print("저장된 데이터가 존재하지 않습니다.")


if __name__ == "__main__":
    while True:
        sel = select()

        if sel == "A":
            read_file()
        elif sel == "B":
            possible_rent_list()
        elif sel == "C":
            rent_room()
        elif sel == "D":
            return_room()
        elif sel == "E":
            rent_history()
        elif sel == "Q":
            write_file()
            break

    print("프로그램을 종료합니다.")


