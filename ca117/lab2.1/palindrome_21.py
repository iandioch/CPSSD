import sys, re

s = re.sub('[^a-z]', '', sys.argv[1].lower())

print(s == s[::-1])
