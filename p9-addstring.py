name = raw_input("Enter the name:")

if (name == "ing"):
  newname = name + "ly"
  print(newname)

elif(len(name) < 3):
  print (name)
  
else:
  newname = name + "ing"
  print(name)
  print(newname)