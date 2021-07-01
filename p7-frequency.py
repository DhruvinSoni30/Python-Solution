name = raw_input("Enter the name:")
char = raw_input("Enter a character whose frequency you wants to find:")
count=0

for i in range(len(name)):
  if (name[i] == char):
    count = count + 1
print ("Frequency is of " + char + " is:", count)
