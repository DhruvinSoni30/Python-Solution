li = [1,2,3,4,5]

print(len(li))

#Append at the end
li.append(7)

print(li)
print(len(li))

#Not working
new_li = li.append(100)
print(new_li)

#Working
li.append(101)
new_li = li
print(new_li)

#0 =  Index
li.insert(0,102)
print(li)

li.extend([15,16])
print(li)

#Removed the ending number
li.pop()
print(li)

#Removed from index
li.pop(0)
print(li)

#Remove the value
li.remove(2)
print(li)
