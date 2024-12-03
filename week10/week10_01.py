
myFile = "C:/A202001098/leechungseong.txt" 

#열기
#f = open(myFile, "w") # 쓰기모드 = w
f = open(myFile, "a+") # 추가모드 = a

#쓰기/읽기
f.write("이충성\n")

#닫기
f.close()

f = open(myFile, "r") # 읽기모드
print(f.read())
f.close()
