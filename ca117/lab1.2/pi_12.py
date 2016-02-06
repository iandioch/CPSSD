from math import pi
import sys

n = int(sys.argv[1])
last = str(pi)[n+1]
if str(pi)[n+2] >= '5':
	last = str(int(last) + 1)
print(str(pi)[:n+1] + last)
