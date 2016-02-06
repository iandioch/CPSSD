import sys, re

def pluralise(s):
	changeToES = ['ch', 'sh', 'x', 's', 'z', 'o']

	for end in changeToES:
		if(re.match('.*' + end + '$', s)):
			return s + 'es'

	#consonant + y -> drop y and add 'ies'
	if re.match('.*[^aeiou]y', s):
		return s[:-1] + 'ies'

	#f or fe -> drop f or fe and add ves
	if s[-1] == 'f':
		return s[:-1] + "ves"
	if s[-2::] == 'fe':
		return s[:-2] + "ves"
	return s + 's'

if __name__ == '__main__':
	print(pluralise(sys.argv[1]))
