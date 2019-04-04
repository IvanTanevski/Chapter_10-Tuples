# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day 
# for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then 
# splitting the string a second time using a colon.
# "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
# ______________________________________________________________________________________________________________________

# First, with while loop and try and except we assure to get the right file name avoiding Traceback
while True:
    fname = input("Enter file name: ")
    try:
        fhandle = open(fname)
        break
    except:
        print("File not found! Enter again.")
        continue

# In a blank list, with a for loop we append only the first number(hour) of the clock, first by splitting the line by spaces, then
# the secong list item from behind in the new 'words' list we split by ':' and we added on the 0th list item(the hour) in the blank list.
hoursList = list()
for line in fhandle:
    if not line.startswith("From ") : continue
    words = line.split()
    time = words[-2].split(":")
    hoursList.append(time[0])

# Creating a dictionary and put the hour items, with their count in it.
hourPairs = dict()
for hour in hoursList:
    hourPairs[hour] = hourPairs.get(hour, 0) + 1

# Creating a list, and putting the dictionary items as tuples in the list, then we sort the list
lst = list()
for k, v in hourPairs.items():
    newTup = (k, v)
    lst.append(newTup)
lst = sorted(lst)

# Print the items from the sorted list ascending by hour
for k, v in lst:
    print(k, v)