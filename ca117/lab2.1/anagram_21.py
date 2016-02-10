import sys

for line in sys.stdin.readlines():
    words = line.split()
    if len(words) != 2:
        break
    print(sorted(words[0]) == sorted(words[1]))
