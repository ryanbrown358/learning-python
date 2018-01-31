#string functions

myStr = "hello World"

#capitalize 
print(myStr.capitalize())

#swap case
print(myStr.swapcase())

#get the length
print(len(myStr))

#replace 
print(myStr.replace("World", "Everyone"))

#count the specific characters in a string
sub = "l"
print(myStr.count(sub))

#starts with and ends with 
print(myStr.startswith("hello"))

print(myStr.endswith("World"))

#split to list
print(myStr.split())

#find 
print(myStr.find("o"))

#Index
print(myStr.index("l"))

#is all alphnumeric 
print(myStr.isalnum())

#is all alphabetic 
print(myStr.isalpha())

#is all numeric 
print(myStr.isnumeric())

