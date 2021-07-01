num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
ope = raw_input("Enter the operation:")

if (ope == "+"):
  ans = num1 + num2
  print(ans)
elif (ope == "-"):
  ans = num1 - num2
  print(ans)
elif (ope == "*"):
  ans = num1 * num2
  print(ans)
elif (ope == "/"):
  ans = num1 / num2
  print(ans)
else: 
  print ("Wrong Input")
