import sys
from math import pi

start = float(sys.argv[1])
step = float(sys.argv[2])
end = float(sys.argv[3])

print("Radius (m)      Area (m^2)    Volume (m^3)")
print("----------      ----------    ------------")

r = start
while r <= end:
	area = 4*pi*r*r
	volume = (4/3)*pi*r*r*r
	print("{:>10.1f}      {:>10.2f}   {:>13.2f}".format(r, area, volume))
	r += step
