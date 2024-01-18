#creating an object
a = [ { 'name': 'Ram', "id": 21, 'Course': 'Science'},{ 'name': 'Ramesh', "id": 2, 'Course': 'Management'},{ 'name': 'Ramyu', "id": 1, 'Course': 'IT'},{ 'name': 'Ramyu', "id": 1, 'Course': 'IT'}]

for x in a:
    #popping elemnents from an array
    a.pop(2)
    
    #removing the elements from the array
    a.remove({ 'name': 'Ram', "id": 21, 'Course': 'Science'})
    
    # Appending in the last element
    a.append({ 'name': 'Saurab', "id": 31, 'Course': 'ENglish'})
    
    #inserting the elements in the array
    a.insert(1,{ 'name': 'Ram', "id": 21, 'Course': 'Science'} )
    
    #to avoid infinite loop
    break
#printing the elements of the array
for i in range(len(a)):
    print(a[i])


#Boolean 
print(len(a)>6)

