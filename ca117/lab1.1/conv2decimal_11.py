import sys

def main():
        input_str = sys.argv[1]
        base = int(sys.argv[2])
        power = 0
        ans = 0
        for c in input_str[::-1]:
                n = int(c)
                ans += n*(base**power)
                #print(str(n) + " " + str(ans))
                power += 1
        print(ans)

if __name__ == '__main__':
        main()
