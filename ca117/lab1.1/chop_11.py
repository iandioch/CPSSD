import sys

def chop(s):
	return s[1:-1]

def main():
	ans = chop(sys.argv[1])
	if ans:
		print(ans)

if __name__ == '__main__':
	main()
