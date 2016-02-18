import sys

try:
    with open(sys.argv[1]) as f:
        bestResult = 0
        bestStudent = "me"
        for line in f.readlines():
            parts = line.split()
            if int(parts[0]) > bestResult:
                bestResult = int(parts[0])
                bestStudent = parts[1:]

        output = "Best student:"
        for p in bestStudent:
            output += " " + p
        print(output)
        print("Best mark: " + str(bestResult))
except:
    print("The file " + sys.argv[1] + " could not be opened.")
