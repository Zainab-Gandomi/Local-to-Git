#Create a generator that infinitely cycles through a list of items in order.


def list_item_generator (list_item):
    
    for i in list_item:
        yield i
        print (i)



string_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Kiwi", "Lemon"]


cycle_generator = list(list_item_generator(string_list))


#Create a generator that yields random numbers.

import random

def random_num_gen():
    while True:
        yield random.random()

# create random number generator 

random_number_gen = random_num_gen()  

for i in range(8):
    print(next(random_number_gen))


#Create a generator that takes in two numbers and yields all multiples of 3 between the two of them.

def multiples_of_three(start, end):
    # Ensure start is a multiple of 3 or the next multiple of 3
    start = start + (3 - (start % 3)) 

    # Generate multiples of 3 between start and end
    current = start
    while current < end:
        yield current
        current += 3

# Example usage
start_number = 10
end_number = 30

# Create the generator and print multiples of 3 between start_number and end_number
for multiple in multiples_of_three(start_number, end_number):
    print(multiple)


















