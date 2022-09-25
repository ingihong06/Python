import csv
harm = {}
date = '20140101'
with open("D:\자료\국민건강보험공단 실제진료정보(20191219)\시군구 지역코드", "r") as k:
    stateReader = csv.reader(k)
    with open("D:\자료\국민건강보험공단 실제진료정보(20191219)\실제진료정보_감기_시군구.csv", "r") as f:
        harmReader = csv.reader(f)
        for row in harmReader:
            print('\'' + row[1]+ '\': [\'' + row[0] + '\' \'' + row[2] + '\']')
            break
        for row in harmReader:
            if row[0] == date:
                harm[row[1]] = [row[0], row[2]]
b = str(harm)
c = b.split(',')
for i in range(len(c)):
    print(c[i], end = '\n')
