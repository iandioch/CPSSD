import sys

def get_line(curr, n):
        num_spaces = n - curr
        return (num_spaces*' ') + (curr*"* ")

def main():
        n = int(sys.argv[1])
        for i in range(1, n):
                print(get_line(i, n))
        
        for i in range(n, 0, -1):
                print(get_line(i, n))
                
        #`print('') #newline at end

if __name__ == '__main__':
        main()
