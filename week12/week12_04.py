# week12_04.py


def test():
    raise NotImplementedError("test() 미구현")

flag = True
while flag:
    try:
        dvd = int(input("분자:"))
        dvs = int(input("분모:"))
        print(dvd/dvs)
        test()
    except ValueError as e:
        print("정수 입력." + str(e))
    except ZeroDivisionError as e:
        print("분모 0" + str(e))
    except Exception as e:
        print(e)
    else:
        flag = False
    finally:
        print("마무리")

