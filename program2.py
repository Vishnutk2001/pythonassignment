def findlen(str):
    counter = 0
    for i in str:
        counter = counter + 1
    return counter
a = input("enter a string")
print(findlen(a))
file = open("data.txt","w")
data = file.write("I am from madurai")