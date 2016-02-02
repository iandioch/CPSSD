import sys

def capitalise(s):
	return s[0].upper() + s[1:-1] + s[-1].upper()

def main():
	if(len(sys.argv[1]) >= 2):
		print(capitalise(sys.argv[1]))

if __name__ == '__main__':
	main()
