# week11_05.py

class In:
    def test(self):
        print("In.test()")

class Out:
    def test(self):
        print("Out.test()")

#test()
        
#In.test() #실행가능 In().test()
#Out.test() #실행가능 Out().test()

i = In()
o = Out()

#1
In.test(i)
Out.test(o)

#2
i.test()
o.test()

#잘 안씀.
In.test(o)
Out.test(i)
