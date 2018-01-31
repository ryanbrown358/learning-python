#open a file
fo = open("text.txt", "w")

#get some info 
print("Name: ", fo.name)

#see if the file is closed or not
print("Is closed: ", fo.close)

#mode of file
print("Opening Mode:", fo.mode)

#write to a file
fo.write("I love python")
fo.write(" And C#")
fo.close()

#open to append to a file
fo = open("text.txt", "a")
fo.write(" And aslo JavaScript")
fo.close()

#read from file
fo = open("text.txt", "r+")
text = fo.read()
print(text)
fo.close()

#creat files
fo = open("test2.txt", "w+")
fo.write("This is my new file")