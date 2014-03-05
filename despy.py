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
	# end create_shifted_blocks()


	def permute_key_with_pc2(self, key):
		if len(key) != 56:
			raise Exception("Key length must be 56 bits.")
		for char in key:
			if char != '0' and char != '1':
				raise Exception("Key must contain only 0's and 1's.")

		permuted_key = [None]*48
		for i in range(len(PC2_TABLE)):
			permuted_key[i] = key[PC2_TABLE[i] - 1]
		return ''.join(permuted_key)
	# end permute_key_with_pc2()


	def initial_permutation(self, message):
		if len(message) != 64:
			raise Exception("Message length must be 64 bits.")
		for char in message:
			if char != '0' and char != '1':
				raise Exception("Message must contain only 0's and 1's.")
		
		permuted_message = [None]*64
		for i in range(len(IP_TABLE)):
			permuted_message[i] = message[IP_TABLE[i] - 1]
		return ''.join(permuted_message)	
	# end initial_permutation()


	def e_bit_selection(self, right_block):
		if len(right_block) != 32:
			raise Exception("Block length must be 32 bits.")
		for char in right_block:
			if char != '0' and char != '1':
				raise Exception("Block must contain only 0's and 1's.")
		
		permuted_block = [None]*48
		for i in range(len(E_BIT_TABLE)):
			permuted_block[i] = right_block[E_BIT_TABLE[i] - 1]
		return ''.join(permuted_block)
	# end e_bit_selection()


	def s_box_selection(self, bits, box_num):
		if len(bits) != 6:
			raise Exception("Must use only 6 bits for S box selection.")
		for char in bits:
			if char != '0' and char != '1':
				raise Exception("Bits must contain only 0's and 1's.")
		s_box = S[box_num]
		row_bits = bits[0] + bits[5]
		row = int(row_bits, 2)
		column_bits = bits[1:5]
		column = int(column_bits, 2)

		# this is the actual index in the S table list
		index = (row*16) + (column)
		# this is cryptic -- this converts the number at the index
		# position in the given box from an int into a binary string
		# 4 bits long.
		value = "{0:04b}".format(s_box[index])
		return value


	def build_s_box_output(self, data):
		if len(data) != 48:
			raise Exception("Must use only 6 bits for S box selection.")
		for char in data:
			if char != '0' and char != '1':
				raise Exception("Data must contain only 0's and 1's.")
		pieces = []
		pieces.append(data[0:6])
		pieces.append(data[6:12])
		pieces.append(data[12:18])
		pieces.append(data[18:24])
		pieces.append(data[24:30])
		pieces.append(data[30:36])
		pieces.append(data[36:42])
		pieces.append(data[42:])

		selections = []
		for i in range(len(pieces)):
			new_selection = self.s_box_selection(pieces[i], i+1)
			selections.append(new_selection)
		return ''.join(selections)


	def feistel(self, data, key):
		'''
		(1) expand data from 32 to 48 bits using E table
		(2) calculate Kn XOR E(Rn-1) (key XOR E(data)) -- this yields
			eight groups of six bits 
		(3) each group of six bits gives us address in a different S box.
			First and last bits denote row, middle 4 bits denote column.
			Get number from that position in certain S box, convert to binary.
		(4) Finally, concat all the bits from above and perform permutation P.

		So, f(Kn, Rn-1) = P(S1(B1)S2(B2)...S8(B8))
		'''
		pass
	# end feistel


	def encrypt(self, plain_text, key):
		'''
		step 1: create 16 subkeys, each 48 bits long
			(i) permute key using PC-1 table (to 56 bit key) -- DONE
			(ii) split into left and right halves (C0 and D0, 28 bits each) -- DONE
			(iii) from C0 and D0, create 16 blocks from each using left shifts table
			(iv) from each CnDn form key Kn by using PC-2 table (48 bits)
		TODO: step 2: encode each 64-bit block of data
			(i) apply initial permutation by using IP table on 64-bit data
			(ii) divide IP block into L0 and R0 halves, 32 bits each
			TODO: (iii) iterate 16 times on:
				Ln = Rn-1
				Rn = Ln-1 XOR f(Rn-1,Kn)
				using f function
			TODO: (iv) apply final permutation IP^-1
		'''
		#######################################################################
		# step 1: create 16 subkeys, each 48 bits long
		#######################################################################
		# (i) permute key using PC-1 table (to 56 bit key)
		permuted_key = permute_key_with_pc1(key)
		if len(permuted_key) != 56:
			raise Exception("Length of permuted key should be 56 bits.")

		# (ii) split into left and right halves (C0 and D0, 28 bits each)
		c_zero = permuted_key[0:28]
		d_zero = permuted_key[28:]

		# (iii) from C0 and D0, create 16 blocks from each using left shifts table
		c_blocks = self.create_shifted_blocks(c_zero)
		d_blocks = self.create_shifted_blocks(d_zero)

		# (iv) from each CnDn form key Kn by using PC-2 table (48 bits)
		keys = []
		for i in range(len(c_blocks)):
			pair = c_blocks[i] + d_blocks[i]
			new_key = self.permute_key_with_pc2(pair)
			keys.append(new_key)
		#######################################################################
		# end of step 1
		#######################################################################

		#######################################################################
		# step 2: encode each 64-bit block of data
		#######################################################################
		# (i) apply initial permutation by using IP table on 64-bit data
		initial_permutation = self.initial_permutation(plain_text)

		# (ii) divide IP block into L0 and R0 halves, 32 bits each
		L_zero = initial_permutation[0:28]
		R_zero = initial_permutation[28:0]

		######################################################################
		# end of step 2
		#######################################################################
	# end encrypt()

# end DESpy class
