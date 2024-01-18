class Robot: 
    new_var = "this is a robot"
    
robot = Robot()
print(robot.new_var)

#constructor function
class Fruit:
    def __init__(self, name:str ,price: int):        #type pani haalna milcha        #magic words = str, init 
        self.name = name
        self.price = price
    def __str__(self) -> str:                        #value aafaile herna milne 
        return f"this fruit is {self.name} and price {self.price}"
    
    def getValue(self):
        return f"this fruit is {self.name} and price {self.price}"
        
fruit= Fruit("apple", 255)
fruit= Fruit("orange", 205)
print(fruit)
print(fruit.getValue())