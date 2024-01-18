#craeting an array
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#creating another array to store the even numbers
even = []

#processing the numbers to distinguish the even numbers
for i in range(len(num)):
    if num[i] % 2 == 0:
        # element = num[i]
        even.append(num[i])
#printing the array
for i in range(len(even)):
    print(even[i])
    
    
