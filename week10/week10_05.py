# week10_05.py
import os

myPath = "C:\\A202001098"
myFile = "leechungseong_02.txt"

#fullPath = os.path.join(myPath, myFile)
#C:\A202001098\leechungseong_02.txt

fullPath = myPath + "\\" + myFile
#C:\\A202001098\\leechungseong_02.txt

if not os.path.exists(myPath):
    os.mkdir(myPath)
if os.path.exists(fullPath):
    with open(fullPath, 'r') as f:
        lines = f.readlines()

        score_list = []
        for line in lines:
            sub_score_list = line.strip().split('|')
            dict_scores = {}
            for sub_score in sub_score_list:
                score = sub_score.split(",")
                dict_scores[score[0]] = int(score[1])

            if dict_scores:
                score_list.append(dict_scores)

    print(score_list)
