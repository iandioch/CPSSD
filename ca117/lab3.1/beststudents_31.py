import sys

try:
    with open(sys.argv[1]) as f:
        bestResult = 0
        bestStudents = ["me"]
        for line in f.readlines():
            parts = line.split()
            try:
                r = int(parts[0])
                if r == bestResult:
                    bestStudents.append(' '.join(parts[1:]))
                elif r > bestResult:
                    bestStudents = [' '.join(parts[1:])]
                    bestResult = r
            except:
                print("Invalid mark %s encountered. Skipping." % parts[0])
                continue

        output = "Best student(s): " + bestStudents[0]
        for p in bestStudents[1:]:
            output += ", " + p
        print(output)
        print("Best mark: " + str(bestResult))
except:
    print("The file " + sys.argv[1] + " could not be opened.")
