'''
Daniel Klein
2.22.2014

So, on a whim I've decided to take a shot at implementing the DES encryption 
algorithm in highly readable Python, without a ton of design forethought.
Here goes.

Reference: http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
'''
from tables import *


class DESpy():
	def __init__(self):
		pass


	def XOR(self, bitsA, bitsB):
		'''
		Return the exclusive-OR'ed result of two binary strings (1's and 0's).
		'''
		if len(bitsA) != len(bitsB):
			raise Exception("Strings must be same length in order to XOR")

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


	def permute_key_with_pc1(self, key):
		if len(key) != 64:
			raise Exception("Key length must be 64 bits.")
		for char in key:
			if char != '0' and char != '1':
				raise Exception("Key must contain only 0's and 1's.")
		
		permuted_key = [None]*56
		for i in range(len(PC1_TABLE)):
			permuted_key[i] = key[PC1_TABLE[i] - 1]
		return ''.join(permuted_key)
	# end permute_key_with_pc1()


	def create_shifted_blocks(self, init_block):
		blocks = []
		cur_block = init_block
		for num_shifts in SHIFT_TABLE:
			next_block = self.left_shift(cur_block, num_shifts)
			blocks.append(next_block)
			cur_block = next_block
		return blocks


	def encrypt(self, plain_text, key):
		'''
		TODO: step 1: create 16 subkeys, each 48 bits long
			(i) permute key using PC-1 table (to 56 bit key) -- DONE
			(ii) split into left and right halves (C0 and D0, 28 bits each) -- DONE
			TODO: (iii) from C0 and D0, create 16 blocks from each using left shifts table
			TODO: (iv) from each CnDn form key Kn by using PC-2 table (48 bits)
		TODO: step 2: encode each 64-bit block of data
			TODO: (i) apply initial permutation by using IP table on 64-bit data
			TODO: (ii) divide IP block into L0 and R0 halves, 32 bits each
			TODO: (iii) iterate 16 times on:
				Ln = Rn-1
				Rn = Ln-1 XOR f(Rn-1,Kn)
				using f function
			TODO: (iv) apply final permutation IP^-1
		'''
		# (i) permute key using PC-1 table (to 56 bit key)
		permuted_key = permute_key_with_pc1(key)
		if len(permuted_key) != 56:
			raise Exception("Length of permuted key should be 56 bits.")

		# (ii) split into left and right halves (C0 and D0, 28 bits each)
		c_zero = permuted_key[0:28]
		d_zero = permuted_key[28:]

		pass
	# end encrypt()

# end DESpy class
