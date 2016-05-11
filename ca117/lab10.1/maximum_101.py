def maximum(a):
	if len(a) == 1:
		return a[0]
	if len(a) == 2:
		return a[0] if a[0] > a[1] else a[1]
	return maximum([maximum(a[:len(a)//2]), maximum(a[len(a)//2:])])
