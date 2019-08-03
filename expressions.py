a = "hello"
b = "world"
c = "again"

myList = [1,2,5,4,5]

for i in myList:
    print(i)

def myPrint(words):
    print(words, ", ok.")

def myFunction(vList):
    for i in vList: 
        print(i)

myPrint("are you")



def myRecursiveFunction(vList):
    if len(vList) > 0: 
        print(vList.pop())
        myRecursiveFunction(vList)

myRecursiveFunction(["hello", 1, True, 3.14159])

x = 15

while(x > 0):
	print(x)
	x = x - 1

def myFunction2(vList, step):
    for i in range(0, len(vList), step):
        print(vList(i))

myFunction2(["hello",1, True, 3.14159], 2)


