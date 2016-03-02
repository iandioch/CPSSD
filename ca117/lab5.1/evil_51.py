import sys

words = sys.stdin.readlines()

for orig_word in words:
	word = ""
	for letter in orig_word.lower():
		if letter in ['e', 'v', 'i', 'l']:
			word += letter

	if word == "evil":
		print(orig_word[:-1])

	
