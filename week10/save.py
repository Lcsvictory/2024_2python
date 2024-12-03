
def add_func(a,b):
    return a+b

#add_lambda = lambda a,b: return a+b return 에러 발생
add_lambda = lambda a,b: a+b
print(add_func(1,6))
print(add_lambda(1,6))



s1 = {1,2,3,3,4,'1'}
s2 = set("1123a")
print(s1, s2, sep="\n")
print("+"*40)
print(s1 & s2) # 교집합 intersection
print(s1 | s2) # 합집합 union
print(s1 - s2) # 차집합 difference

s1.add("a") # 단일값
print(s1)

s1.update(["a", 10]) # 다중값
print(s1)

s1.remove("a") # 다중값
print(s1)



data1 = [1,2,3,4]

summary = sum(data1)
maximum = max(data1)
minimum = min(data1)
average = int(sum(data1) / len(data1))

print(summary, maximum, minimum, average, sep="\n")

print("-"*30)

for i in data1:
    print(i)

print("-"*30)

for i in range(len(data1)):
    print(i)

print("-"*30)

for i in range(len(data1)):
    print(f"data1[{i}]:{data1[i]}")

print("-"*30)

for v in enumerate(data1):
    print(f"data1[{v[0]}]:{v[1]}")

print("-"*30)

for k, v in enumerate(data1):
    print(f"data1[{k}]:{v}")



data2 = [
    [1,2,3],
    [10,20],
    [11,12,13,14]
    ]

print("-"*30)
for i in data2:
    print(i)

print("-"*30)
for i in data2:
    print('sum', sum(i))
    print('max', max(i))
    print('min', min(i))
    print('avg', int(sum(i) / len(i)))




print("-"*30)
for k,v in enumerate(data2):
    print(f"{k+1}번째 : {v}")
    print('sum', sum(v))
    print('max', max(v))
    print('min', min(v))
    print('avg', int(sum(v) / len(v)))




print("최종-"*30)
for k,v in enumerate(data2):
    print(f"{k+1}번째 :", end="")
    for i in range(len(v)):
        print(f"[{i}]{v[i]} ", end="")
    print()
    print('sum', sum(v))
    print('max', max(v))
    print('min', min(v))
    print('avg', int(sum(v) / len(v)))
    

data3 = {
    "김인하" : [1,2],
    "이인하" : [10,20,30,40,50,60,70],
    "송인하" : [11,12,13,14]
    }


print("최종-"*30)

for k in data3.keys(): # k == "김인하","이인하"....
    print(f"{k} :", end="")
    for i in range(len(data3[k])): # data3["김인하"] == [1,2]
        print(f"[{i}]{data3[k][i]} ", end="")
    print()
    print('sum', sum(data3[k])) 
    print('max', max(data3[k]))
    print('min', min(data3[k]))
    print('avg', sum(data3[k]) / len(data3[k]))

'''
data3 = {
    "김인하" : [1,2],
    "이인하" : [10,20,30,40,50,60,70],
    "송인하" : [11,12,13,14]
    }
'''


    











































