def outerFunction(x):
    def innerFunction(y):
        return x + y
    return innerFunction

#outerfunction call gareko
closureFunction = outerFunction(4)

#closureFunction = innerFunction
result = closureFunction(5)   
print(result)
