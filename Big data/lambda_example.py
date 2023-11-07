
#A lambda function that takes in a number and returns that number squared
squared_num = lambda x : x ** 2

y = squared_num(8)
print(y)


#A lambda function that takes in a number and returns that number cubed

cube_num = lambda x : x ** 3

y  = cube_num(3)
print(y)

#A lambda function that takes two numbers and returns the sum of those numbers

sum_num = lambda x, y : x + y

z =sum_num( 3, 9)
print(z)

#A lambda function that takes two numbers and returns the product of those numbers

multiple_num = lambda x , y : x * y 

z = multiple_num(5, 7)
print(z)


#Create a list with 5 tuples, where each tuple contains a name and a number. Then, using the sort function, 
# create a lambda function for each of the following bullet points:

name_list = [("zizi", 1), ("ali", 7), ("asal", 4), ("qazal", 9), ("marbar", 34)]

#Sort the list by the number in each tuple

sorted_by_num = sorted(name_list, key = lambda x : x[1] )
print(sorted_by_num)

#Sort the list by the name in each tuple

sorted_by_name = sorted( name_list, key = lambda x : x[0])
print(sorted_by_name)


#Sort the list by the length of the name in each tuple

sorted_by_name_len = sorted( name_list, key = lambda x : len(x[0]))
print(sorted_by_name_len)

#Sort the list by the length of the name in each tuple, but in reverse order

sorted_by_name_len_reverse = sorted( name_list, key = lambda x : len(x[0]), reverse= True)
print(sorted_by_name_len_reverse)


#Create a list of 5 numbers and then create the following lambda functions:

list_num = [33,7,98,65,4]

#A lambda function that squares a number. Then use map to square each number in the list

squared_num_1 = map(lambda  element : element ** 2, list_num)
print(list(squared_num_1))


#A lambda function that cubes a number. Then use map to cube each number in the list

cube_num_1 = map(lambda element : element ** 3, list_num)
print(list(cube_num_1))


#A lambda function that takes in a number and returns that number squared if it is even, and cubed if it is odd. 
# Then use map to apply the function to each number in the list.

squared_even_cube_odd = list(map(lambda x : x ** 2 if x % 2 == 0 else x ** 3 ,list_num ))
print(squared_even_cube_odd)


#Create a list of 10 strings then create the following lambda functions:

string_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Kiwi", "Lemon"]


#A lambda function that takes in a string and returns True if the string is longer than 5 characters, and False if it is not. 
# Then use filter and the lambda function to filter out all strings that are longer than 5 characters.

len_checker = list(map( lambda char : True if len(char) > 5 else False, string_list))
print(len_checker)

len_longer_5 = list(filter(lambda char : len(char) > 5 , string_list))
print(len_longer_5)




#A lambda function that takes in a string and returns True if the string is longer than 5 characters and starts with a vowel, and False if it is not. 
# Then use filter and the lambda function to filter out all strings that are longer than 5 characters and start with a vowel.















