name = raw_input("Enter the name:")
newname = ""
for i in range(len(name)):
  if i % 2 == 0:
    newname = newname + name[i]
print (newname)


