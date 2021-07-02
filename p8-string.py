name = raw_input("Enter the name:")
count = 0

for i in name:
    if(len(name)) == 2:
      print("Empty String")
    else:
      count = count + 1
      newname =  name[:2] + name[count - 2:count]
      print(name)
      print(newname)