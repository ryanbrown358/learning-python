#functions 


#create a function 
def sayHello(name = "John"):
    print("Hello", name)

sayHello()

# return a value 
def getSum(num1, num2):
    total = num1 + num2
    return total

numSum = getSum(1,2)
print(numSum)

def addOneTwoNum(num):
    num = num + 1
    print("Value inside function", num)
    return 

num = 5
addOneTwoNum(num)
print("Value outside function", num)

def addOneToList(myList):
    myList.append(4)
    print('Value inside function: ', myList)

myList = [1,2,3]
addOneToList(myList)
print('Value outside of function: ', myList)