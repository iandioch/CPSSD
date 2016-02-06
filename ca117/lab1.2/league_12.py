import sys

h1 = 'POS'
h2 = 'CLUB'
h3 = 'P'
h4 = 'W'
h5 = 'D'
h6 = 'L'
h7 = 'GF'
h8 = 'GA'
h9 = 'GD'
h10 = 'PTS'

print('{:>3s} {:20s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(h1, h2, h3, h4, h5, h6, h7, h8, h9, h10))

for line in sys.stdin:
	s = line.split()
	name = s[1]
	for i in range(2, len(s)-8):
		name += ' ' + s[i]
	print('{:>3s} {:20s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(s[0], name, s[-8], s[-7], s[-6], s[-5], s[-4], s[-3], s[-2], s[-1]))