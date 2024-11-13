# week12_02.py
PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r**2)

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

if __name__ == "__main__":
    print(type(Math()))
    print(add(1,2))
    print(sub(1,2))
