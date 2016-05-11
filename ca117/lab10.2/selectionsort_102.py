def selectionsort(a):
	for done in range(len(a)-1):
		min_value = a[done]
		min_index = done
		for i in range(done+1, len(a)):
			if a[i] < min_value:
				min_value = a[i]
				min_index = i

		a[min_index], a[done] = a[done], a[min_index]
