num = []

for i in range(19):
    num.append(i)

#creating another array to store the odd numbers
odd = []

#processing the numbers to distinguish the even numbers
for i in range(len(num)):
    if num[i] % 2 != 0:
        # element = num[i]
        odd.append(num[i])
#printing the array
for i in range(len(odd)):
    print(odd[i])
    
    
