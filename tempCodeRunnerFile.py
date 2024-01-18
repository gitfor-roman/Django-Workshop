n = int(input("Enter the number"))

userArray=[]

for i in range(n):
    element=int (input("Enter the element:"))
    userArray.append(element)
    for i in range(n):
        print(userArray[i])