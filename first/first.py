# Filter Even number

def filter_even(_num):
	for n in _num:
		if n%2!=0:
			_num.pop(_num.index(n))
	return _num

num=[1,2,3,4,5,6,7,8,9]
print(filter_even(num))