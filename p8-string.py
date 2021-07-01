name = raw_input("Enter the name:")
count = 0

for i in name:
    count = count + 1
newname =  name[:2] + name[count - 2:count]
print(name)
print(newname)