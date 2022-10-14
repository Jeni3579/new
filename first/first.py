"""

# Example of loop

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

"""

# Check eligible to vote (Age > 22)

age = int(input("Please provide your age: "))
if age > 22 :
    print (f"You can vote because you are of age {age}.")
else:
    print ("You cannot vote because you don't reach the age to vote.")
