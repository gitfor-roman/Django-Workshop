string = ["ram", "peter", "john", "james", "johanes"]


#destructuring gareko index,value 
for index, value in enumerate(string):
    # for i in range(len(string)):
    if (index%2 ==0):
        print(f"This is {index} index and value is {value}")