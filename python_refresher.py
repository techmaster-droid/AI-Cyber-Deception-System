number = 10
print(f"integer: {number}, Type: {type(number)}")
float = 3.12
print(f"Float: {float}, Type: {type(float)}")

my_string = "Hello"
print(f"String: {my_string}, Type: {type(my_string)}")

print(f"Uppercase: {my_string.upper()}")

# Booleans
is_active = True
print(f"Bolean: {is_active}, Type: {type(is_active)}")

# Lists
my_list = [1, 2, "three", 4.44]
print(f"List: {my_list}, First element: {my_list[0]}")
my_list.append("five")
print(f"New list: {my_list}")

# Dictionary
my_dict = {"name": "Tanzeel", "age": 30, "city": "Thalassery"}
print(f"Dictionary: {my_dict}, Name: {my_dict['name']}")
my_dict["age"]= 24
print(f"Updated age: {my_dict['age']}")

# Arithmetic
result = 15 / 4
print(f"15 / 4 : {result}")

# Comparison
is_equal = (5 == 5)
is_greater = (5 > 3)
print(f"5 == 5 : {is_equal}")
print(f"5 > 3 : {is_greater}")

# Logical
condition1 = True
condition2 = False
print(f"condition1 and condition2 is {condition1 and condition2}")
print(f"not condition2 is {not condition2}")

# If-elif-else
temperature = 25
if temperature > 30:
    print("it's hot")
elif temperature > 20:
    print("it is cooling down")
else:
    print("it is coold")

# For loop
print("\nThis is for loop")
fruits = ["Banana", "Apple", "Mango"]
for fruit in fruits:
    print(f"I like {fruit}")

for i in range(4):
    print(f"number: {i}")

# While loop
print("\nThis is while loop")
count = 0
while count < 3:
    print(f"number: {count}")
    count+=1

# Function
def greet(name):
    return f"Hello, {name}"
print("\nThis is function")
message = greet('Tanzeel')
print(f"\n{message}")

def add_numbers(a, b):
    return a + b

adding = add_numbers(4, 10)
print(f"\n {adding}")

# OOP
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"My car is {self.make} {self.model}"

print("\n This is OOP")
my_car = Car("Suzuki", "Alto")
print(my_car.display_info())