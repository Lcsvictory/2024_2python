

myFile = "C:/A202001098/leechungseong_02.txt"

f = open(myFile, 'r')

# type1
#d = f.read()
#print(d)

# type2
#while True:
#    d = f.readline()
#    if not d:
#        break
#    print(d.strip())

#type3
d = f.readlines()
for line in d:
    print(line.strip())

f.close()
