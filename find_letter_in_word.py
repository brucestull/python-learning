# Third edit: done at github.com.
# First edit.
# Ask the user for a word. Add .lower() to the input return so it's easier to compare the letters. This method removes case sensitivity.
word = input("Enter a word: ").lower()

# Ask the user for a letter. Add .lower() to the input return so it's easier to compare the letters. This method removes case sensitivity.
letter = input("Enter a letter: ").lower()

# Use the keyword 'in' to determine if the letter is in the word.
# Tell the user if the letter is in the word. Display the letter in uppercase.

# When letter is in word.
if letter in word:

    # count the occurances of the letter in the word
    letter_count = word.count(letter)
    # Set value of the message.
    message = f'The word "{word}" contains the letter "{letter}" {letter_count} times.'

# When letter is not in word.
else:
    # Set value of message.
    message = f'The letter "{letter}" is not in the word {word}.'

# Print the message which was set in the 'if' or 'else' block.
print(message)
