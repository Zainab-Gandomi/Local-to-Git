"""
Define a Cylinder class, its constructor (__init__) should take two arguments:

height
radius, which has a default value of 1
The class has four attributes:

height
radius
surface_area, initialised as None
volume, initialised as None
It should also have two methods:

get_surface_area: This method updates the attribute surface_area, and it returns the value rounded to 2dp.
get_volume: This method updates the attribute volume, and it returns the value rounded to 2dp.
Use Google to find the formulae for surface area and volume of a cylinder. Use the formulae to create method definitions for these.

Now, instead of initialising surface_area and volume to None, initialise them to the value returned by get_surface_area and get_volume respectively.
"""

import math

class Cylinder:
    def __init__(self, height, radius=1):
        self.height = height
        self.radius = radius
        self.surface_area = self.get_surface_area()
        self.volume = self.get_volume()

    def get_surface_area(self):
        self.surface_area = round(2 * math.pi * self.radius * (self.radius + self.height), 2)
        return self.surface_area

    def get_volume(self):
        self.volume = round(math.pi * self.radius**2 * self.height, 2)
        return self.volume

# Example usage
cylinder = Cylinder(5, 2)  # Height: 5, Radius: 2
print("Surface Area:", cylinder.surface_area)  # Output: Surface Area: 94.25
print("Volume:", cylinder.volume)  # Output: Volume: 62.83

     
"""
Create a Car class
Define the constructor for the class:
It takes in two arguments (other than self), and assign their values as attributes of the instance:
One called model (e.g. Tesla), which has no default
One called year, which is an integer, which defaults to the current year (just hard code the current year in)
It also defines a new attribute (remember that is not passed as an argument):
One called miles_driven, which is set to zero
Create a method called drive
It prints "vroom" and increment the instance's miles_driven attribute by 1
Create a method called info
It prints the number of miles driven, the model name and the year
Initialiase the class
Call all the methods
   
"""
import datetime

class Car:
    def __init__(self,model, year = datetime.datetime.now().year):
        self.model = model
        self.year = year
        self.miles_driven = 0

    def drive(self):
        print("vroom")
        self.miles_driven += 1    

    def info(self):
        print("miles driven is: ", self.miles_driven)  
        print("car model is: ", self.model) 
        print("year of production is; ", self.year) 


# Initialize the Car instance
car = Car(model="Tesla")

# Call the drive method multiple times
car.drive()
car.drive()
car.drive()

# Call the info method
car.info()


"""
Create a Phone class
The class takes two arguments:
One called number (e.g. 07777777777), which has no default. This is the phone number of the phone and will be used as an attribute
One called balance, which is an integer, which defaults to 20. This is the balance of the phone and will be used as an attribute
Create a method called make_call
It takes two arguments:
One called number (e.g. 07777777777), which has no default. This is the phone number of the person being called
One called duration, which is an integer, which defaults to 1. This is the duration of the call in minutes
Inside the method, check if the balance is greater than or equal to the duration of the call. If it is, then:
Print "Calling {number} for {duration} minutes"
Subtract the duration from the balance
If the balance is not greater than or equal to the duration of the call, then:
Print "Insufficient balance"
Create a method called info
It prints the phone number and the balance
"""

class Phone:
    def __init__(self, number, balance = 20):
        self.number = number
        self.balance = balance

    def make_call(self, number, duration=1):
        if self.balance >= duration:
            print(f"Calling {number} for {duration} minutes")
            self.balance -= duration
        else:
            print("Insufficient balance")

    def info(self):
        print("Phone Number:", self.number)
        print("Balance:", self.balance)

# Example usage
phone = Phone("07777777777")

# Making calls
phone.make_call("08888888888", 5)  # Insufficient balance
phone.make_call("09999999999", 3)  # Calling 09999999999 for 3 minutes

# Displaying phone information
phone.info()

"""
Create a Class called Vector
Define its initialiser so that it takes in a list of numbers as an argument
Create an instance of the vector
Define the __repr__ magic method to define what is printed when we print the object. It's up to you what this should look like.
Define how you add two vector objects together. Again, your choice whether to add them element-wise or concatenate them.
Define how you index an item in a vector

"""


class Vector:
    def __init__(self, numbers):
        self.numbers = numbers

    def __repr__(self):
        return f"Vector({self.numbers})"

    def __add__(self, other):
        if len(self.numbers) != len(other.numbers):
            raise ValueError("Vectors must have the same length for addition.")
        
        # Element-wise addition
        result_numbers = [x + y for x, y in zip(self.numbers, other.numbers)]
        return Vector(result_numbers)

    def __getitem__(self, index):
        return self.numbers[index]

# Create an instance of the Vector
vector1 = Vector([1, 2, 3])
vector2 = Vector([4, 5, 6])

# Print the Vector objects
print("Vector 1:", vector1)  # Output: Vector([1, 2, 3])
print("Vector 2:", vector2)  # Output: Vector([4, 5, 6])

# Add two Vector objects
sum_vector = vector1 + vector2
print("Sum of vectors:", sum_vector)  # Output: Vector([5, 7, 9])

# Access an item in a vector
print("Element at index 1:", vector1[1])  # Output: Element at index 1: 2


"""
Create a class called Person
Define its initialiser
It must take in a name, a date_of_birth in ISO format (YYYY-MM-DD), and a list of friends
It should initialise attributes for each of those. Be careful, don't use a default value for friends! 
This will cause problems whenever you initialise a new instance of the class. To know more about, take a look at this link 
Instantiate your class and test that it works before continuing - do this for every section going forward
Define the __str__ magic method which returns a string representation of the person, detailing their name, DOB and number of friends
Define the __gt__ magic method that defines how to use the greater than sign to compare the age of two people (hint: 
Compare the DOB of the two people)
Create a method called add_friend, which takes in another instance of the person class and adds it to this instance's friends attribute. 
Assume that every relationship goes both ways:
this method should append each friend to the other's list, in just one call

"""


class Person:
    def __init__(self, name, date_of_birth, friends):
        self.name = name
        self.date_of_birth = date_of_birth
        self.friends = friends

    def __str__(self):
        return f"Name: {self.name}, DOB: {self.date_of_birth}, Number of friends: {len(self.friends)}"

    def __gt__(self, other):
        return self.date_of_birth > other.date_of_birth

    def add_friend(self, friend):
        self.friends.append(friend)
        friend.friends.append(self)

# Instantiate the class and test
person1 = Person("Alice", "1990-05-15", [])
person2 = Person("Bob", "1985-08-22", [])

print("Person 1:", person1)  # Output: Person 1: Name: Alice, DOB: 1990-05-15, Number of friends: 0
print("Person 2:", person2)  # Output: Person 2: Name: Bob, DOB: 1985-08-22, Number of friends: 0

# Test __gt__ magic method
print("Is Person 1 older than Person 2?", person1 > person2)  # Output: True

# Test add_friend method
person1.add_friend(person2)
print("Person 1's friends after adding Person 2:", [friend.name for friend in person1.friends])  
print("Person 2's friends after adding Person 1:", [friend.name for friend in person2.friends])  










