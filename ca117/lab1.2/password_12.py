import sys, re

def has_digits(s):
	return len(re.findall(".*[0-9].*", s))

def has_uppercase(s):
	return len(re.findall(".*[A-Z].*", s))

def has_lowercase(s):
	return len(re.findall(".*[a-z].*", s))

def has_special(s):
	return len(re.findall(".*[^a-zA-Z0-9].*", s))
result = has_digits(sys.argv[1]) + has_uppercase(sys.argv[1]) + has_lowercase(sys.argv[1]) + has_special(sys.argv[1])

print(result)
