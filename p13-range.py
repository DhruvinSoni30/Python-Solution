num = input("Enter the number:")
previousNum = 0


for i in range(num):
 sum = previousNum + i
 print ("Current Number", i, "Previous Number", previousNum, "Sum", sum)
 previousNum = i


