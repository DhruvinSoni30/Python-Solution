num = input("Enter the Number:")

if (num >= 0 and num <= 10):
  print ("Small")
elif (num >=10 and num <= 100):
  print ("Medium")
elif (num >= 100 and num <= 1000):
  print ("Large")
else:
  print ("Invalid")