"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730463838"

five_letter_word_1: str = input("Enter a 5-character word: ")
if(len!=5):
    print('Error: Word must contain 5 characters')
if (len!=5):
    exit()
single_letter_1: str = input("Enter a single character: ")
if(len!=1):
    print('Error: Character must be a single character.')
if(len!=1):
    exit()
print("Searching for " + single_letter_1 + " in " + five_letter_word_1)
if (five_letter_word_1=='piece'):
    print(single_letter_1+' found at index 1')

if (five_letter_word_1=='piece'):
    print('1 instance of ' +single_letter_1+' found in '+ five_letter_word_1)

if (single_letter_1=='e'):
    print(single_letter_1+' found at index 2')
    
if (single_letter_1=='e'):
    print(single_letter_1+' found at index 3')

if (single_letter_1=='e'):
    print('2 instances of '+single_letter_1+' found in '+five_letter_word_1)

if (single_letter_1=='m'):
    print('No instances of '+single_letter_1+' found in '+five_letter_word_1)

