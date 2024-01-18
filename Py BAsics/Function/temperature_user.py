def c_to_f(celsius):
    return celsius * 9/5 + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert():
    signal = (input("To convert C to F, enter 1; else 0: "))

    if signal == '1':
        c = int(input("Enter the value of C: "))
        f = c_to_f(c)
        print(f"The value of {c}C in Fahrenheit is {f}F")

    else:
        f = int(input("Enter the value of F: "))
        c = f_to_c(f)
        print(f"The value of {f}F in Celsius is {c}C")

convert()
