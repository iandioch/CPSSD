import sys, re

s = [] 
for line in sys.stdin.readlines():
    s.extend([re.sub('[^a-z0-9]', '', d.lower()) for d in line.split()])

print(len(set([d for d in s if len(d) > 0])))
