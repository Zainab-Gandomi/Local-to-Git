nterm = int(input("please enter the number of term? "))

# initial condition
n1 , n2 = 0 , 1 
count = 0 

if nterm <= 0 :
    print(" please enter positive number.")
elif nterm == 1 :
    print("Fibonacci sequence of", nterm , "is:")
    print(n1)
else:
    print("fibonacci sequence:")
    while count < nterm :
        print(n1)
        nth = n1 + n2
        # update value by
        n1 = n2
        n2 = nth
        count += 1