#Conditionals 

x = 7

#basic if 
if x < 6:
    print('this is true')

#if else 
if x < 6:
    print("this is true")
else: 
    print("This is false")

#Elif
color = "Red"

if color == "Red":
    print("color is red")
elif color == "blue":
    print("color is blue")
else: 
    print("color is not red or blue")

#Nested if
if color == "Red":
    if x < 10:
        print("Color is Red and x is less than 10")

#logical operators 
if color == "Red" and x < 10:
    print("Color is red and x is less than 10")