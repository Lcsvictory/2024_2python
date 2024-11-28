import userinfo
import os

mlt = []

def select():
    print("#"*30)
    print("A. 기존자료복원")
    print("B. 회원등록")
    print("C. 정보수정")
    print("D. 전체조회")
    print("Q. 종료 및 회원정보 저장")
    print("#"*30)
    user_sel = input().strip().upper()
    return user_sel


def weight_height(how:str, morkg:str):
    try:
        w_h = float(input(f"{how}({morkg}):").strip())
    except Exception as e:
        print(f"{how} 입력이 잘못되었습니다.")
        return 
    return w_h

def create_user():
    print("[회원 정보 등록]")
    uid = input("아이디:").strip()
    for i in mlt:
        if i.uid == uid:
            print("동일한 아이디가 있습니다.")
            return
        
    sex = input("성별 (M:남자 F:여자):").strip().upper()
    if sex not in ['M','F']:
        print("성별이 잘못 입력되었습니다.")
        return

    height = weight_height("신장", "m")
    if not height:
        return
    
    weight = weight_height("체중", "kg")
    if not weight:
        return
        
    user1 = userinfo.UserInfo(uid, sex, height, weight)
    mlt.append(user1)
    print(f"입력한 정보를 바탕으로 계산한 BMI 수치 : {user1.cal_bmi()}")


def update_user():
    if mlt:
        print("[회원 정보 등록]")
        uid = input("아이디:").strip()
        flag = 0
        for user1 in mlt:
            if user1.uid == uid:
                flag = 1
                print(f"현재 신장 : {user1.height}")
                up_height = input("수정 신장(m):").strip()
                if up_height:
                    try:
                        up_height = float(up_height)
                    except:
                        print("수정 신장 입력이 잘못되었습니다.")
                        return
                    user1.height = up_height
                
                print(f"현재 체중 : {user1.weight}")
                up_weight = input("수정 체중(kg):").strip()
                if up_weight:
                    try:
                        up_weight = float(up_weight)
                    except:
                        print("수정 신장 입력이 잘못되었습니다.")
                        return
                    user1.weight = up_weight
                print(f"입력한 정보를 바탕으로 계산한 BMI 수치 : {user1.cal_bmi()}")
                return
        if flag == 0:
            print("회원정보가 없습니다.")
            return

    else:
        print("수정할 회원이 없습니다")
        return

def user_info_view():
    if mlt:
        print("[전체 상태 조회]")
        print("="*50)
        mlt_male = [male for male in mlt if male.sex == "M"]
        mlt_female = [male for male in mlt if male.sex == "F"]
        print("[남성]")
        for i, male in enumerate(mlt_male):
            print(f"{[i+1]} 아이디:{male.uid} 신장:{male.height:.2f} 체중:{male.weight:.2f} BMI:{male.cal_bmi()}")
            print(f"도표:", "*"*int(float(male.cal_bmi())) )
            print()

        print()
        print("[여성]")
        for i, male in enumerate(mlt_female):
            print(f"{[i+1]} 아이디:{male.uid} 신장:{male.height} 체중:{male.weight} BMI:{male.cal_bmi()}")
            print(f"도표:", "*"*int(float(male.cal_bmi())) )
            print()
        print("="*50)
        print(f"총 {len(mlt)}명의 정보입니다.")
        
    else:
        print("상태를 보여줄 회원이 없습니다.")


def file_path():
    mypath = "c:\\2020000"
    if not os.path.isdir(mypath):
        os.mkdir(mypath)
    return f"{os.path.join(mypath, 'bmilist.txt')}"

def write_file():
    if mlt:
        with open(file_path(), "w", encoding="utf-8") as f:
            for user in mlt:
                f.write(f"{user.uid}|{user.sex}|{user.height}|{user.weight}\n")
        print(f"{len(mlt)}건의 데이터를 저장했습니다.")
    else:
        print("저장할 자료가 없습니다.")

def read_file():
    if os.path.isfile(file_path()):
        if len(mlt) == 0:
            with open(file_path(), "r", encoding="utf-8") as f:
                while line := f.readline():
                    user_data = line.strip().split("|")
                    if len(user_data) == 4:
                        user = userinfo.UserInfo(user_data[0], user_data[1], float(user_data[2]), float(user_data[3]))
                        mlt.append(user)
            print(f"{len(mlt)}건의 데이터를 복원했습니다.")
            return
        else:
            print("기존 자료와의 충돌이 발생할 수 있으므로 복원할 수 없습니다.")
            return
    else:
        print("복원할 데이터가 없습니다.")
        return
if __name__ == "__main__" :
    while True:
        sel = select()

        if sel == "A":
            read_file()
        elif sel == "B":
            create_user()
        elif sel == "C":
            update_user()
        elif sel == "D":
            user_info_view()
        elif sel == "Q":
            write_file()
            break

    print("프로그램을 종료합니다.")
