# 주차장 관리 프로그램의 기본 반복문
import datetime
import os
import random


cars = []
dFormat = "%Y-%m-%d %H:%M"
mypath = "c:\\주차장관리프로그램"

class Vehicle:
    def __init__(self, number:str, car_type:str, intime:datetime.datetime, outtime=None):
        self.number = number
        self.car_type = car_type
        self.intime = intime
        self.outtime = outtime

    def calculate_cost(self) -> int:
        if self.outtime:
            return int((self.outtime - self.intime).total_seconds()/60/60) * 1000
        return int((datetime.datetime.now() - self.intime).total_seconds()/60/60) * 1000

def auto_gen(what_time):
    if what_time == "in":
        h = random.randint(1, 72)
        m = random.randint(0, 60)
        return datetime.datetime.now() - datetime.timedelta(hours=h, minutes=m)
    elif what_time == "out":
        h = random.randint(1, 72)
        m = random.randint(0, 60)
        return datetime.datetime.now() + datetime.timedelta(hours=h, minutes=m)
    return datetime.datetime.now()

def read_file():
    if not os.path.isdir(mypath):
        os.mkdir(mypath)
    if not os.path.isfile(os.path.join(mypath, "parking_records.txt")):
        print("기존에 저장된 파일이 존재하지 않습니다. 새로 데이터를 입력해주세요.")
        return
    try:
        with open(os.path.join(mypath, "parking_records.txt"), "r", encoding="utf-8") as f:
            while line := f.readline():
                splits = line.strip().split("|")
                if len(splits) == 4:
                    number = splits[0]
                    car_type = splits[1]
                    intime = datetime.datetime.strptime(splits[2], dFormat)
                    if splits[3]:
                        outtime = datetime.datetime.strptime(splits[3], dFormat)
                    else:
                        outtime = None
                    cars.append(Vehicle(number, car_type, intime, outtime))
    except Exception as e:
        print(e)
        print("파일을 읽어오는데 문제가 발생했습니다.")

def register_vehicle():
    number = input("차량번호를 입력하세요 : ").strip()
    
    flag = 0
    for car in cars:
        if car.number == number:
            print("해당 차량은 이미 주차되어 있습니다.")
            flag = 1
            break
    if flag == 0:
        while True:
            car_type = input("차종을 입력하세요 : ").strip()
            if not car_type:
                print("차종은 필수입니다.")
                continue
            break
        while True:
            intime = input("입차시간을 입력하세요 : ").strip()
            if intime:
                try:
                    intime = datetime.datetime.strptime(intime, dFormat)
                except:
                    print("양식이 올바르지 않습니다.")
                    continue
                break
            else:
                intime = auto_gen("in")
                break

        while True:
            outtime = input("출차시간을 입력하세요 : ").strip()
            if outtime:
                try:
                    outtime = datetime.datetime.strptime(outtime, dFormat)
                except:
                    print("양식이 올바르지 않습니다.")
                    continue
                break
            else:
                outtime = None
                break
        cars.append(Vehicle(number, car_type, intime, outtime))
        print("정상 등록 되었습니다.")

def modify_vehicle_info():
    print("차량 정보 수정 기능 실행 중...")
    if not cars:
        print("등록된 차량 정보가 없습니다.")
        return
    number = input("차량 번호를 입력하세요 : ").strip()
    for car in cars:
        if car.number == number:
            print(f"현재 차종 : {car.car_type}")
            car_type = input("수정할 차종 : ").strip()
            if car_type:
                car.car_type = car_type
            print(f"입차시간 : {car.intime}")
            while True:
                intime = input("입차시간 수정 : ").strip()
                if intime:
                    try:
                        car.intime = datetime.datetime.strptime(intime, dFormat)
                    except:
                        print("양식이 올바르지 않습니다.")
                        continue
                    break
                else:
                    break
            print("차량 정보 수정이 정상적으로 처리되었습니다.")
            return      
    print("해당 차량이 존재하지 않습니다.")
    return

def view_all_vehicles():
    print("전체 차량 조회 기능 실행 중...")
    if not cars:
        print("차량 데이터가 존재하지 않습니다.")
        return
    print(f"차량은 총 {len(cars)}대 주차되어 있습니다.")
    for i, car in enumerate(cars):
        print(f"입차순서 : {i+1} | 차량번호 : {car.number} | 차종 : {car.car_type} | 입차시간 : {car.intime} | 출차시간 : {car.outtime}")
        

def checkout_vehicle():
    print("차량 출차 기능 실행 중...")
    if not cars:
        print("차량 데이터가 존재하지 않습니다.")
        return
    number = input("차량 번호를 입력하세요 : ").strip()
    for car in cars:
        if car.number == number:
            while True:
                outtime = input("출차 시간을 입력하세요 : ").strip()
                if outtime:
                    try:
                        car.outtime = datetime.datetime.strptime(outtime, dFormat)
                    except:
                        print("양식이 올바르지 않습니다.")
                        continue
                    break
                else:
                    car.outtime = auto_gen("out")
                    break
            cars.remove(car)
            print(f"주차 요금은 {car.calculate_cost()}원 입니다.")
            print("안녕히 가십시오.")            
            return
    print("해당 차량이 존재하지 않습니다.")
    return

def save_and_exit():
    print("정보를 파일에 저장 중...")
    cnt = 0
    if not os.path.isdir(mypath):
        os.mkdir(mypath)
    if not cars:
        print("차량 데이터가 존재하지 않습니다.")
        return
    with open(os.path.join(mypath, "parking_records.txt"), "w", encoding="utf-8") as f:
        for car in cars:
            number = car.number
            car_type = car.car_type
            intime = car.intime.strftime(dFormat)
            if car.outtime:
                outtime = car.outtime.strftime(dFormat)
            else:
                outtime = ""
            f.write(f"{number}|{car_type}|{intime}|{outtime}\n")
            cnt += 1
    print(f"총 {cnt}건의 데이터를 저장했습니다.")
# 프로그램 실행
if __name__ == "__main__":
    read_file()
    while True:
        print("\n=== 주차장 관리 프로그램 ===")
        print("A: 차량 등록")
        print("B: 차량 정보 수정")
        print("C: 전체 차량 조회")
        print("D: 차량 출차")
        print("Q: 프로그램 종료")
        choice = input("메뉴를 선택하세요: ").strip().upper()

        if choice == "A":
            register_vehicle()
        elif choice == "B":
            modify_vehicle_info()
        elif choice == "C":
            view_all_vehicles()
        elif choice == "D":
            checkout_vehicle()
        elif choice == "Q":
            save_and_exit()
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택하세요.")

