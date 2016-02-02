import sys

def count_letters(s):
        ans = {}
        for c in s:
                if c in ans:
                        ans[c] += 1
                else:
                        ans[c] = 1
        return ans

def main():
        first_letters = count_letters(sys.argv[1])
        second_letters = count_letters(sys.argv[2])
        
        valid = True
        for c in first_letters:
                if c not in second_letters:
                    valid = False
                    break
                
                if first_letters[c] > second_letters[c]:
                        valid = False
                        break

        print(valid)
#        print(count_letters(sys.argv[1]))

if __name__ == '__main__':
        main()
