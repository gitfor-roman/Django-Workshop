# c= ((f-32)/9)*5


def askfunc():
    c= int(input("Enter the value of c"))
    getfunc(c)
    
def getfunc(c):
    f = (9*c)/5 +32
    displayFunc(f)

def displayFunc(f):
    print(f"The value of F is {f}")


askfunc()
# getfunc()
# displayFunc()



