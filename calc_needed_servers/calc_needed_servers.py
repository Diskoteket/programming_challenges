import sys
import time

def listToString(s):  
    str1 = ""  

    for c in s:  
        str1 += c 

    return str1  

entryList = []
rangesList =[]

neededServers = 1
var0 = '0'

entryList = sys.stdin.read().splitlines()

pop = entryList.pop(0)
maxRequests = (str(pop).split(" "))[1]

length = (len(entryList))
x = 0
while x < length:
    if len(entryList[x]) <= 3:
        byCharacter = list(entryList[x])
        while len(byCharacter) <= 5:
            byCharacter.insert(0,var0)
        startranges = (listToString(byCharacter))

        rangeFrom = '000000'
        rangeTo = '000999'
        rangeEntry = "".join([rangeFrom,  rangeTo])
        rangesList.append(rangeEntry)
        x += 1

    elif len(entryList[x]) == 4:
        byCharacter = list(entryList[x])
        while len(byCharacter) <= 5:
            byCharacter.insert(0,var0)
        startranges = (listToString(byCharacter))

        rangeFrom = "".join(['00', str(int(entryList[x][0])), '000'])
        rangeTo = "".join(['00', str(int(entryList[x][0])), '999'])
        rangeEntry = "".join([rangeFrom,  rangeTo])
        rangesList.append(rangeEntry)
        x += 1

    elif len(entryList[x]) == 5:
        byCharacter = list(entryList[x])
        while len(byCharacter) <= 5:
            byCharacter.insert(0,var0)
        startranges = (listToString(byCharacter))

        rangeFrom = "".join(['0', str(int(entryList[x][0])), str(int(entryList[x][1])),'000'])
        rangeTo = "".join(['0', str(int(entryList[x][0])), str(int(entryList[x][1])),'999'])
        rangeEntry = "".join([rangeFrom,  rangeTo])
        rangesList.append(rangeEntry)
        x += 1

    elif len(entryList[x]) == 6:
        byCharacter = list(entryList[x])
        while len(byCharacter) <= 5:
            byCharacter.insert(0,var0)
        startranges = (listToString(byCharacter))

        rangeFrom = "".join([str(int(entryList[x][0])), str(int(entryList[x][1])), str(int(entryList[x][2])), '000'])
        rangeTo = "".join([str(int(entryList[x][0])), str(int(entryList[x][1])), str(int(entryList[x][2])), '999'])
        rangeEntry = "".join([rangeFrom,  rangeTo])
        rangesList.append(rangeEntry)
        x += 1

rangesDict = {i:rangesList.count(i) for i in rangesList}

for key in rangesDict:
    if rangesDict[key] <= int(maxRequests):
        pass
    elif rangesDict[key] > int(maxRequests):
        needed = (-(-rangesDict[key] // int(maxRequests)))
        neededServers = neededServers + needed -1
sys.stdout.write(str(neededServers))