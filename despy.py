'''
Daniel Klein
2.22.2014

So, on a whim I've decided to take a shot at implementing the DES encryption 
algorithm in highly readable Python, without a ton of design forethought.
Here goes.
'''


class DESpy():
	def __init__(self):
		pass


	def XOR(self, bitsA, bitsB):
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
	# end XOR()


	def left_shift(self, bits, num_shifts=1):
		
		oldBits = list(bits)
		newBits =  [None]*len(bits)

		for i in range(num_shifts):
			newBits = [None]*len(bits)
			for j in range(len(oldBits)):
				newBits[j-1] = oldBits[j]
			oldBits = newBits

		newString = "".join(newBits)
		return newString
	# end left_shift()


	def encrypt(self, plain_text, key):
		'''
		step 1: create 16 subkeys, each 48 bits long
			(i) permute key using PC-1 table (to 56 bit key)
			(ii) split into left and right halves (C0 and D0, 28 bits each)
			(iii) from C0 and D0, create 16 blocks from each using left shifts table
			(iv) from each CnDn form key Kn by using PC-2 table (48 bits)
		step 2: encode each 64-bit block of data
			(i) apply initial permutation by using IP table on 64-bit data
			(ii) divide IP block into L0 and R0 halves, 32 bits each
			(iii) iterate 16 times on:
				Ln = Rn-1
				Rn = Ln-1 XOR f(Rn-1,Kn)
				using f function
			(iv) apply final permutation IP^-1
		'''
		pass
	# end encrypt()

# end DESpy class
