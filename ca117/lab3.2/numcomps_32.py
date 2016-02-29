import sys

mult3s = [x for x in range(3, 31, 3)]
print("Multiples of 3: " + str(mult3s))
print("Multiples of 3 squared: " + str([x*x for x in mult3s]))
mult4s = [x for x in range(4, 57, 4)]
print("Multiples of 4 doubled: " + str([2*x for x in mult4s if 2*x < 57]))
print("Multiples of 3 or 4: " + str(sorted(set(mult3s + [x for x in mult4s if x < 30]))))
print("Multiples of 3 and 4: " + str([x for x in range(30) if (x in mult3s and x in mult4s)]))
print("Multiples of 3 replaced: " + str([('X' if (x % 3 == 0) else x) for x in range(1, 31)]))
