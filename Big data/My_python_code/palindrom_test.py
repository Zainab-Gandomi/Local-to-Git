word = input("what is your word? ")
word = word.casefold()
rev_word = reversed(word)

if list(word) == list(rev_word):
    print("This word is palindrom.")
else:
    print("This word is not palindrom.")