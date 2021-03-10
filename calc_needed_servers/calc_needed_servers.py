import sys

# Initiate variables
entryList = []
rangesList =[]
neededServers = 1

# Read input
entryList = sys.stdin.read().splitlines()

# Pop the first entry in list and determine threshold of max requests per milisecond
pop = entryList.pop(0)
maxRequests = int((str(pop).split(" "))[1])

# Variables for looping through input
length = (len(entryList))
x = 0

# Start parsing data
while x < length:
    # Class entries matching range 000000 - 000999
    if len(entryList[x]) <= 3:
        # Read the length of the string, and insert 0 at position 0 of the list until it matches pattern
        byCharacter = list(entryList[x])
        while len(byCharacter) <= 5:
            byCharacter.insert(0,'0')
        # Determine range of entry and append to list of x ranges
        rangeFrom = '000000'
        rangeTo = '000999'
        rangeEntry = "".join([rangeFrom,  rangeTo])
        rangesList.append(rangeEntry)
        x += 1

    # Class entries matching range 00x000 - 00x999
    elif len(entryList[x]) == 4:
        byCharacter = list(entryList[x])
        # Read the length of the string, and insert 0 at position 0 of the list until it matches pattern
        while len(byCharacter) <= 5:
            byCharacter.insert(0,'0')
        # Determine range of entry and append to list of x ranges
        rangeFrom = "".join(['00', str(int(entryList[x][0])), '000'])
        rangeTo = "".join(['00', str(int(entryList[x][0])), '999'])
        rangeEntry = "".join([rangeFrom,  rangeTo])
        rangesList.append(rangeEntry)
        x += 1

    # Class entries matching range 0yx000 - 0yx999
    elif len(entryList[x]) == 5:
        byCharacter = list(entryList[x])
        # Read the length of the string, and insert 0 at position 0 of the list until it matches pattern
        while len(byCharacter) <= 5:
            byCharacter.insert(0,'0')
        # Determine range of entry and append to list of x ranges
        rangeFrom = "".join(['0', str(int(entryList[x][0])), str(int(entryList[x][1])),'000'])
        rangeTo = "".join(['0', str(int(entryList[x][0])), str(int(entryList[x][1])),'999'])
        rangeEntry = "".join([rangeFrom,  rangeTo])
        rangesList.append(rangeEntry)
        x += 1

    # Class entries matching range zyx000 - zyx999
    elif len(entryList[x]) == 6:
        byCharacter = list(entryList[x])
        # Read the length of the string, and insert 0 at position 0 of the list until it matches pattern
        while len(byCharacter) <= 5:
            byCharacter.insert(0,'0')
        # Determine range of entry and append to list of x ranges
        rangeFrom = "".join([str(int(entryList[x][0])), str(int(entryList[x][1])), str(int(entryList[x][2])), '000'])
        rangeTo = "".join([str(int(entryList[x][0])), str(int(entryList[x][1])), str(int(entryList[x][2])), '999'])
        rangeEntry = "".join([rangeFrom,  rangeTo])
        rangesList.append(rangeEntry)
        x += 1

# Create a dictionary to count all of ranges
rangesDict = {i:rangesList.count(i) for i in rangesList}

# Determine how many servers are needed by asking dictionary and calculate
for key in rangesDict:
    if rangesDict[key] <= maxRequests:
        pass
    elif rangesDict[key] > maxRequests:
        needed = (-(-rangesDict[key] // maxRequests))
        neededServers = neededServers + needed -1

# Output servers needed
sys.stdout.write(str(neededServers))