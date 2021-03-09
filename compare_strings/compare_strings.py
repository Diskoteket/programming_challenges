# Initialize variables and import sys library
import sys

splitbychartemp1 = []
difference = ''

# Define function for splitting strings into seperate characters in list
def split(string):
    return [char for char in string] 

# Read the contents of stdin
content = []
while True:
    try:
        line = input()
    except EOFError:
        break
    content.append(line)

# Remove the first element
by = int(content.pop(0))
n = 2

# Divide list into groups
splitlist = [content[i * n:(i + 1) * n] for i in range((len(content) + n - 1) // n )]

# Start looping through list
for i in range(len(splitlist)): 
    sys.stdout.write('\n')

# Start second loop for elements/groups
    for j in range(len(splitlist[i])):
        sys.stdout.write(splitlist[i][j] + '\n')
        splitbychar = (split(splitlist[i][j]))

# Save some results for temporary usage later
        splitbychartemp2 = splitbychartemp1
        splitbychartemp1 = splitbychar

# Start loop for measuring of temporary list-variables that are populated by characters from original string
    for c in range(len(splitbychar)): 
        if splitbychar[c] == splitbychartemp2[c]:  
          difference = difference + '.'  
        else:  
           difference = difference + '*'

# Print results and flush variable for new loop
    sys.stdout.write(difference + '\n')
    difference = ''