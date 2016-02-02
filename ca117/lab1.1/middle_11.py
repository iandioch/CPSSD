import sys

def has_middle(s):
	return len(s) % 2 == 1

def get_middle(s):
	return s[len(s)//2]

def main():
	if has_middle(sys.argv[1]):
		print(get_middle(sys.argv[1]))
	else:
		print('No middle character!')

if __name__ == '__main__':
	main()
