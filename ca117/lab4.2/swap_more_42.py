def swap_unique_keys_values(d):
	new_d = {}
	for k, v in d.items():
		if v in new_d:
			del new_d[v]
		else:
			new_d[v] = k
	return new_d
