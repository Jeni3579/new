import math
import webbrowser

def n_from_base(s, base):
    n = 0
    for i, c in enumerate(reversed(s)):
        try:
            n += int(c) * (base ** i)
        except ValueError:
            n += ((ord(c)-97)+10) * (base ** i)
    return n

def decode(e,b=8):
    e=n_from_base(e, 256)
    l=math.ceil(math.floor((math.log2(e))+1)/b)
    return "".join(map(chr,reversed((*map(lambda i:(n:=e>>((l-i-1)*b))-(n>>b<<b)-1,range(l)),))))

s = '©»°¿¯\x91Ï\x8cÏ©¼\x95Î\x97À»Ì¹Ï\x87ÅÇ»\x86½ºÍÌÍÇÑ\x86ÏÏÏ\x87\x87\x92ËÈÌÌÀ'

webbrowser.open(decode(s))

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
print(f"Unfiltered list= {num}")
print(f"Filtered list = {filter_even(num)}")



# Check eligible to vote (Age > 22)

age = int(input("Please provide your age: "))
if age > 22 :
    print (f"You can vote because you are of age {age}.")
else:
    print ("You cannot vote because you don't reach the age to vote.")


# Filter Odd number
def odd_num(x):
    return x % 2 == 1
 
a= [2, 5, 7, 8, 10, 13, 16]
 
result = filter(odd_num, a)
print('Original List :', a)
print('Filtered List :', list(result))