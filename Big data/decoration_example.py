#Create a decorator that prints start and end at the start and end of a function call.

def start_end_func (func):
    print("Start")
    func()
    print("End.")


def hello_hi():
    print("Heloooooo \nThis is my function!!!")


print_hello_func = start_end_func(hello_hi)   
print(print_hello_func)


#Create a decorator to time how long a function takes to run and print the duration.

add = lambda x, y: x + y
print(add(2, 3))















