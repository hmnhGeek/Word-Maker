# Word-Maker

## Introduction
This project is built to find the possible words one can make out of given letters. The project
was made so as to crack android word games like word brain, word track and word cookies and many other
such games. This script can be used for other purposes also.

## Functions
	
	1. makewords(data, start):
		data is the string of letters and start is an integer.
		For example: makewords('htae', 2) --> at, hat, ate, hate
		makewords('htae', 3) --> hat, ate, hate

	2. wordoflength(data, length):
		Returns all possible words of length 'length' that can be made from data.

	3. complementary(data, number):
		Returns key, value pairs where key is a word of length 'number' and value is the list
		of words of length 'len(data) - number' or 'number - len(data)'.

	4. prettify(data):
		Here data is not the data above. data here refers to the list or dictionary that the above
		three functions return. This function just prints everything in a good presentation on the terminal or interpreter.

		example: prettify(complementary(data, number))

## Terminal Tool
	
		usage: tool.py [-h] [--all] [--comp] [--len] alphabets integer

		positional arguments:
		  alphabets   Find all possible words
		  integer     Find all possible words

		optional arguments:
		  -h, --help  show this help message and exit
		  --all       Find all possible words
		  --comp      Find all complementary words
		  --len       Find all possible words of a given length

	So, --all is equivalent to makewords().
	--comp is equivalent to complementary()
	and --len is equivalent to wordoflength().
