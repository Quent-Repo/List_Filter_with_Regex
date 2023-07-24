## 
import os 
import re

#Get everything in the location of the python file and placing it into "l"
l = os.listdir()

#Sets up what needs to be filtered into the "xs"
xs =re.compile(".*.py")

#Set a new list with the names of the files that need to be removed into variable "newList"
newlist = list(filter(xs.match,l))

#Shows the items that are in the "newlist"
print(newlist)


#A loop that removes the items from the main list in this case "l"
for i in range(len(newlist)):
    l.remove(newlist[i])

#prints out the new main list
print(l)
