
## function to make a items in list double

x = [1,2,3,4,5,6,7,8,9]

def double (a):
    y =[]
    for i in a :
        y.append(i*2)
    return y

print("y list is: ", double(x))


z = list (map (lambda a : a * 2, x))
print("z list is: ", z)


## write function to print even number in list

def even_number (e):
    even_list = []
    for i in e :
        if i % 2 == 0:
            even_list.append(i)
    return even_list


print(even_number(x))       


even_no = list (filter (lambda a : a % 2 == 0 , x))

print (even_no)

from functools import reduce
 
sum = reduce(lambda a,b : a + b , x)
print(sum)

maximum = reduce(lambda a, b : a if a > b else b, x)
print(maximum)