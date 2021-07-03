li = [1,2,3,4,5,1,1,1]
from math import modf


from os import name



#Number 2 is at index 1
print(li.index(2, 0, 2)) #Start looking from index=0 & ends at index=2

#Find whether the value is there in list or not
print(1 in li)
print(6 in li)
print('d' in 'dhruvin')

#How many times 1 occure in list
print(li.count(1))

li1 = ['a', 'q', 'h']
li1.sort() #Modify the existing list
print(li1)

print(sorted(li1)) #Creates new copy of list 
print(li1)

li1.reverse()
print(li1)

range(1,100)
print(list(range(1,100)))

s = ' '
new_s = s.join(['hi', 'my', 'name', 'is', 'Dhruvin'])
print(new_s)

mod_s = ' '.join(['hi', 'my', 'name', 'is', 'Dhruvin'])
print(mod_s)

a,b,c, *other = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)