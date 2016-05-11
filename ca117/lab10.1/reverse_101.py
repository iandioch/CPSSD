def reverse_list(a):
	if len(a) <= 1:
		return a
	return reverse_list(a[1:]) + [a[0]]
