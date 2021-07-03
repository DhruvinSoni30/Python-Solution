from abc import ABCMeta


amount = input("Enter the amount:")

print("Required notes of 2000 is", amount/2000)
print("Required notes of 500 is", (amount % 2000) / 500)
print("Required notes of 100 is", (amount % 2000) % 500 / 100)
print ("Amount still remaining is : " , (((amount % 100) % 50) % 10))

