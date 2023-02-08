def descending_order(num):
	num_list = [int(x) for x in str(num)]
	num_list.sort(reverse = True)
	return int("".join(map(str, num_list)))