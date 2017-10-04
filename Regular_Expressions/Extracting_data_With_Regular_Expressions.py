import re
num = 0
fil = open('exercise.txt')
for line in fil:
    colect = re.findall('[0-9]+',line)
    for item in colect:
        num += int(item)
print (num) 
