import sys

n = sum([len(line.split()) for line in sys.stdin.readlines()])
print(n)
