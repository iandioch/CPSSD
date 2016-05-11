def partition(a, p, r):
	# p is the starting index
	# r is the pivot index, and the last index
	q = j = p
	# j is the index of the most recent index processed
	# q is the index of the final number less than the pivot
	while j < r:
		if a[j] < a[r]:
			a[q], a[j] = a[j], a[q]
			q += 1
		j += 1

	a[q], a[r] = a[r], a[q]

	#return the pivot index
	return q	

def quicksort(a, p, r):
	# p is the start of the range to be sorted
	# r is the end of the range

	if r <= p:
		return
	
	q = partition(a, p, r)

	quicksort(a, p, q-1)
	quicksort(a, q+1, r)
	
