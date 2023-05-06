# 1).

z = 1

for i in range(z+1):
    x = input("Input *,/,+,-,: ")
    a = int(input("a:"))
    b = int(input("b:"))

    if x == "*":
        print(a*b)
    if x == "/":
        if b == 0:
            print("You cant split on 0")
    if x == "+":
        print(a+b)
    if x == "-":
        print(a-b)

    k = input("do you wanna continue of no(Yes or Not): ")
    if k.lower() == "yes":
        z+=1

# 2).
# _ => True
# x => True
# get_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False

import keyword
import string

print(keyword.kwlist)
print(list(string.punctuation))

x = input("Input word: ")
z=1

for i in keyword.kwlist:
    if i == x:
        z = "False"
for i in list(string.punctuation):
    if i == x:
        z = "False"
for i in x:
    if i == i.title():
        z = "False"
if x[0].isdigit():
    z = "False"

if z == "False":
    print("False")
else:
    print("True")

