import random

#task 1: Step 1 & 2
word_list  = ['apple', 'banana', 'orange', 'strawberry', 'watermelon']

#task 1: Step 3
print(word_list)

#task 2: Step 3 & 4 
word = random.choice(word_list)

#task 2: Step 5
print(word)

#task 3: Step 1 & 2
guess = input("pleaase enter a single letter: ")

# task 4: Step 1, 2, and 3
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

