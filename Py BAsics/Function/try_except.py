a= int(input("ENter the first number"))
b= int(input("Enter the second numbe"))


#taking multiple inputs
# int_container= input("Enter the number")
# a,b,c,d,e,f,g = map(int, int_container.split())

def divisionFunc(a,b):
    try:
        result= int(a+b)
        return result
    except ZeroDivisionError: 
        print("Error: Zero Value Error")
    except Exception as e:
        print(f"This is an error: {e}")


print(divisionFunc(a,b))