'''
Quiz: Password Generator
Write a function called password_generator that selects three random words from a provided file of
words and concatenates them into a single string. The code to read in the data from the file is
already in the starter code, you will need to build a password out of these parts.
# Use an import statement at the top

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function here
# It should return a string consisting of three random words 
# concatenated together without spaces
'''
import random

word_file = "words.txt"
word_list = []
# fill up the word_list
with open(word_file, 'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)


def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

print(generate_password())
'''
Quiz Solution: Password Generator
To create random passwords we used import random. The function definition was simply:

def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
Alternatively, you could use the random.sample function and .join method for strings:

def generate_password():
    return str().join(random.sample(word_list,3))
'''
