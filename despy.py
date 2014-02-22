'''
Daniel Klein
2.22.2014

So, on a whim I've decided to take a shot at implementing the DES encryption 
algorithm in highly readable Python, without a ton of design forethought.
Here goes.
'''


def XOR(bitsA, bitsB):
	'''
	Return the exclusive-OR'ed result of two binary strings (1's and 0's).
	'''
	if len(bitsA) != len(bitsB):
		return None

	newBits = ["1"]*len(bitsA)
	for i in range(len(bitsA)):
		if bitsA[i] == bitsB[i]:
			newBits[i] = "0"
	return "".join(newBits)


def left_shift(bits, num_shifts=1):
	
	oldBits = list(bits)
	newBits =  [None]*len(bits)

	for i in range(num_shifts):
		newBits = [None]*len(bits)
		for j in range(len(oldBits)):
			newBits[j-1] = oldBits[j]
		oldBits = newBits

	newString = "".join(newBits)
	return newString


test1 = "00001111"
test2 = "11110000"
test3 = "10101010"
test4 = "11111111"
test5 = "1111"
test6 = "000"
print "{0} XOR {1} is: {2}".format(test1, test2, XOR(test1, test2)) 

print "{0} XOR {1} is: {2}".format(test2, test1, XOR(test2, test1)) 

print "{0} XOR {1} is: {2}".format(test3, test4, XOR(test3, test4)) 

print "{0} XOR {1} is: {2}".format(test5, test6, XOR(test5, test6)) 

print "{0} left shifted one is: {1}".format(test1, left_shift(test1))

print "{0} left shifted two is: {1}".format(test1, left_shift(test1,2))

print "{0} left shifted 3 is: {1}".format(test1, left_shift(test1,3))

print "{0} left shifted 4 is: {1}".format(test1, left_shift(test1,4))

print "{0} left shifted 5 is: {1}".format(test1, left_shift(test1,5))

print "{0} left shifted 6 is: {1}".format(test1, left_shift(test1,6))

print "{0} left shifted 7 is: {1}".format(test1, left_shift(test1,7))

print "{0} left shifted eight is: {1}".format(test1, left_shift(test1,8))