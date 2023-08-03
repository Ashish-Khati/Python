# List in python denoted by []
name=['Ashish','Ayush','Shubhika','Anirudh']
print(name)
value=[24,3,22,1,55,77,66,33,76]
print(value)
listOfList=[name,value]
print(listOfList)

# some operation on List
name.append('Avika')  # append is used to add data at the end
name.insert(4,'Shobhit') # insert is used to add data at any specific postion
name.remove('Avika') # remove is used to remove element from list based on its value
name.pop(2) # remove element based on its index if no index is given it will remove the last element of list
del value[2:5] # used to remove multiple values from any specific range of index
value.extend([111,321,234,543,544,567,886,453]) # used to add multiple values in a list
print(min(value)) # find the minimum from the list
print(max(name)) # find maximum from the list
print(sum(value)) # sum of values
value.sort(); # sort the list
print(name)
print(value)