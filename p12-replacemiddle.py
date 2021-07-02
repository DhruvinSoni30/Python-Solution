string = raw_input("Enter the name:")
char = raw_input("Tyep the charecter you wants to insert:")

length = len(string)

middle = length // 2

print ("The middle string is:", string[middle])

if (length % 2 !=0):
    newstring = string.replace(string[middle], char)
    print ("The new string:", newstring)
else:
    newstring = string[:middle] + char + string[middle:]
    print ("The new string:", newstring)

