string = ["ram", "peter", "john", "james", "johanes"]
print(len(string))

even = []

for i in range(0, len(string)):
    if i % 2 == 0:
        even.append(string[i])

for i in range(len(even)):
    print(even[i])
