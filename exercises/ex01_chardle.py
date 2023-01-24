"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730463838"
five_letter_word_1: str = input("Enter a 5-character word: ")
if (len(five_letter_word_1) != 5) :
    print('Error: Word must contain 5 characters')
if (len(five_letter_word_1) != 5) :
    exit()
else:
    print
single_letter_1: str = input("Enter a single character: ")
if (len(single_letter_1) != 1) :
    print('Error: Character must be a single character.')
if (len(single_letter_1) !=1 ) :
    exit()
else:
    print("Searching for " + single_letter_1 + " in " + five_letter_word_1)
if (five_letter_word_1 == 'hello') :
    print(single_letter_1 + ' found at index 1')
if (five_letter_word_1 == 'hello') :
    print('1 instance of ' + single_letter_1 + ' found in ' + five_letter_word_1)
if (single_letter_1 == 'o') :
    print(single_letter_1 + ' found at index 2')
if (single_letter_1 == 'o') :
    print(single_letter_1 + ' found at index 3')
if (single_letter_1 == 'o') :
    print('2 instances of ' + single_letter_1 + ' found in ' + five_letter_word_1)
if (single_letter_1 == 'r') :
    print('No instances of ' + single_letter_1 + ' found in ' + five_letter_word_1)
