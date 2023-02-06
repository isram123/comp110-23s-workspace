"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730463838"
five_letter_word_1: str = input("Enter a 5-character word: ")
if (len(five_letter_word_1) != 5):
    print('Error: Word must contain 5 characters')
    exit()
single_letter_1: str = input("Enter a single character: ")
if (len(single_letter_1) != 1):
    print('Error: Character must be a single character.')
if (len(single_letter_1) != 1):
    exit()
else:
    print('Searching for ' + single_letter_1 + ' in ' + five_letter_word_1)

count: int = 0

if (five_letter_word_1[0] == single_letter_1):
    print(single_letter_1 + ' found at index 0')
    count = count + 1
if (five_letter_word_1[1] == single_letter_1):
    print(single_letter_1 + ' found at index 1')
    count = count + 1
if (five_letter_word_1[2] == single_letter_1):
    print(single_letter_1 + ' found at index 2')
    count = count + 1
if (five_letter_word_1[3] == single_letter_1):
    print(single_letter_1 + ' found at index 3')
    count = count + 1
if (five_letter_word_1[4] == single_letter_1):
    print(single_letter_1 + ' found at index 4')
    count = count + 1
if (count == 0):
    print('No instances of ' + single_letter_1 + ' found in ' + five_letter_word_1)
if (count == 1):
    print('1 instance of ' + single_letter_1 + ' found in ' + five_letter_word_1)
if (count >= 2):
    print(str(count) + ' instances of ' + single_letter_1 + ' found in ' + five_)