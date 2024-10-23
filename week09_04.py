
data2 = [
    [1,2,3],
    [10,20],
    [11,12,13,14]
    ]

data3 = {
    "김인하" : [1,2],
    "이인하" : [10,20,30,40,50,60,70],
    "송인하" : [11,12,13,14]
    }

def analyze_list(datas):
    for k,v in enumerate(datas):
        print(f"{k+1}번째 :", end="")
        for i in range(len(v)):
            print(f"[{i}]{v[i]} ", end="")
        print()
        print('sum', sum(v))
        print('max', max(v))
        print('min', min(v))
        print('avg', int(sum(v) / len(v)))
    
    
def analyze_dict(datas):
    for k in datas.keys(): # k == "김인하","이인하"....
        print(f"{k} :", end="")
        for i in range(len(datas[k])): # data3["김인하"] == [1,2]
            print(f"[{i}]{data3[k][i]} ", end="")
        print()
        print('sum', sum(datas[k])) 
        print('max', max(datas[k]))
        print('min', min(datas[k]))
        print('avg', sum(datas[k]) / len(datas[k]))

def analyze_score(datas):
    if isinstance(datas, list):
        analyze_list(datas)
    elif isinstance(data, dict):
        analyze_dict(datas)
    else:
        print("판독불가")

        
analyze_list(data2)
analyze_dict(data3)
analyze_score(data2)
















    











































