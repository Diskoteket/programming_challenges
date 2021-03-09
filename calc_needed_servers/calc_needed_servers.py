import sys
import time
# Define function for converting lists to strings
def listToString(s):  
    str1 = ""  

    for c in s:  
        str1 += c 

    return str1  
# Initiate variables
entryList = []
rangesList =[]

neededServers = 1
var0 = '0'
# Read input
entryList = sys.stdin.read().splitlines()
# Pop the first entry in list
pop = entryList.pop(0)
maxRequests = (str(pop).split(" "))[1]

length = (len(entryList))
x = 0
# Start parsing data
while x < length:
    # Class entries matching range 000000 - 999999
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

    # Class entries matching range 00x000 - 00x999
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

    # Class entries matching range 0yx000 - 0yx999
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

    # Class entries matching range zyx000 - zyx999
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

# Create a dictionary to count all entries matching range
rangesDict = {i:rangesList.count(i) for i in rangesList}

# Determine how many servers are needed by asking dictionary
for key in rangesDict:
    if rangesDict[key] <= int(maxRequests):
        pass
    elif rangesDict[key] > int(maxRequests):
        needed = (-(-rangesDict[key] // int(maxRequests)))
        neededServers = neededServers + needed -1
sys.stdout.write(str(neededServers))
