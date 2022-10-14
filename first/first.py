# exaple of loop

i = 0

while i<10:
    print(f"The number is: {i}")
    i = i+1
    
# Filter Even number

def filter_even(_num):
	for n in _num:
		if n%2!=0:
			_num.pop(_num.index(n))
	return _num

num=[1,2,3,4,5,6,7,8,9]
print(filter_even(num))
