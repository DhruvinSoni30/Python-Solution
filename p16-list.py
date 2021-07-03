from os import O_LARGEFILE
from typing import NewType


li = [1,2,3,4,5]
li1 = ["a","b",1,2,]
li2 = [1,2,"a", True]
string = "Hello"
print(li)
print(li1)
print(li2)

print (li[1])
print (li1[2])
print (li2[3])

print(string[0:2:1])

cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

print(cart)
print(cart[0::2])

cart[0] = 'laptop'
print(cart)
print(cart[0:3])

new_cart = cart
new_cart[0] = "Gum"

print(new_cart)

#Copying the list
new_list = old_list[:]

#Mofifying the list
new_list = old_list