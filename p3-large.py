num = input("Enter the First Number:")
num1 = input("Enter the Second Number:")
num2 = input("Enter the Third Number:")

if (num > num1 and num > num2):
  print ("Greater is:", num)
elif (num1 > num and num1 > num2):
    print ("Greater is:", num1)
else:
    print ("Greater is:", num2)