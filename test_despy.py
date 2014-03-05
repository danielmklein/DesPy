'''
Daniel Klein
2.22.2014

The unit tests for my DES implementation.
'''

import unittest
from despy import DESpy
C_BLOCKS = ([
			"1110000110011001010101011111",
			"1100001100110010101010111111",
			"0000110011001010101011111111",
			"0011001100101010101111111100",
			"1100110010101010111111110000",
			"0011001010101011111111000011",
			"1100101010101111111100001100",
			"0010101010111111110000110011",
			"0101010101111111100001100110",
			"0101010111111110000110011001",
			"0101011111111000011001100101",
			"0101111111100001100110010101",
			"0111111110000110011001010101",
			"1111111000011001100101010101",
			"1111100001100110010101010111",
			"1111000011001100101010101111"
			])
D_BLOCKS = ([
			"1010101011001100111100011110",
			"0101010110011001111000111101",
			"0101011001100111100011110101",
			"0101100110011110001111010101",
			"0110011001111000111101010101",
			"1001100111100011110101010101",
			"0110011110001111010101010110",
			"1001111000111101010101011001",
			"0011110001111010101010110011",
			"1111000111101010101011001100",
			"1100011110101010101100110011",
			"0001111010101010110011001111",
			"0111101010101011001100111100",
			"1110101010101100110011110001",
			"1010101010110011001111000111",
			"0101010101100110011110001111"
			])

class TestDespy(unittest.TestCase):
	def setUp(self):
		self.despy = DESpy()

		self.test1 = "00001111"
		self.test2 = "11110000"
		self.test3 = "10101010"
		self.test4 = "11111111"
		self.test5 = "1111"
		self.test6 = "000"

	
	def tearDown(self):
		del self.despy


	def test_XOR(self):
		print "**Testing XOR function...**"
		expected = "11111111"
		actual = self.despy.XOR(self.test1, self.test2)
		print "{0} XOR {1} is: {2}".format(self.test1, self.test2, actual) 
		self.assertEqual(expected, actual)

		expected = "11111111"
		actual = self.despy.XOR(self.test2, self.test1)
		print "{0} XOR {1} is: {2}".format(self.test2, self.test1, actual) 
		self.assertEqual(expected, actual)

		expected = "01010101"
		actual = self.despy.XOR(self.test3, self.test4)
		print "{0} XOR {1} is: {2}".format(self.test3, self.test4, actual) 
		self.assertEqual(expected, actual)

		self.assertRaises(Exception, self.despy.XOR, self.test5, self.test6)
		print "Finished testing XOR function."


	def test_left_shift(self):
		print "**Testing left-shift function...**"
		expected = "00011110"
		actual = self.despy.left_shift(self.test1,1)
		print "{0} left shifted 1 is: {1}".format(self.test1, actual)
		self.assertEqual(expected, actual)

		expected = "00111100"
		actual = self.despy.left_shift(self.test1,2)
		print "{0} left shifted 2 is: {1}".format(self.test1, actual)
		self.assertEqual(expected, actual)		

		expected = "01111000"
		actual = self.despy.left_shift(self.test1,3)
		print "{0} left shifted 3 is: {1}".format(self.test1, actual)
		self.assertEqual(expected, actual)		

		expected = "11110000"
		actual = self.despy.left_shift(self.test1,4)
		print "{0} left shifted 4 is: {1}".format(self.test1, actual)
		self.assertEqual(expected, actual)		

		expected = "11100001"
		actual = self.despy.left_shift(self.test1,5)
		print "{0} left shifted 5 is: {1}".format(self.test1, actual)
		self.assertEqual(expected, actual)		

		expected = "11000011"
		actual = self.despy.left_shift(self.test1,6)
		print "{0} left shifted 6 is: {1}".format(self.test1, actual)
		self.assertEqual(expected, actual)		

		expected = "10000111"
		actual = self.despy.left_shift(self.test1,7)
		print "{0} left shifted 7 is: {1}".format(self.test1, actual)
		self.assertEqual(expected, actual)		

		expected = "00001111"
		actual = self.despy.left_shift(self.test1,8)
		print "{0} left shifted 8 is: {1}".format(self.test1, actual)
		self.assertEqual(expected, actual)
		print "**Finished testing left-shift function.**"


	def test_permute_key_with_pc1(self):
		print "**Testing PC1 key permutation...**"
		self.assertRaises(Exception, self.despy.permute_key_with_pc1, "01010101")
		self.assertRaises(Exception, self.despy.permute_key_with_pc1, "01010101010101010101010101010101010101010101010101010101ABCDEFGH")
 
		test_key = "0001001100110100010101110111100110011011101111001101111111110001"
		expected = "11110000110011001010101011110101010101100110011110001111"
		actual = self.despy.permute_key_with_pc1(test_key)
		print "Key before permutation: {0}".format(test_key)
		print "Expected permuted key:  {0}".format(expected)
		print "Actual permuted key:    {0}".format(actual)
		self.assertEqual(expected, actual) 
		print "**Finished testing PC1 key permutation.**"


	def test_create_shifted_blocks(self):
		print "**Testing creation of shifted key blocks...**"
		c_zero = "1111000011001100101010101111"
		d_zero = "0101010101100110011110001111"

		expected = C_BLOCKS
		actual = self.despy.create_shifted_blocks(c_zero)
		self.assertEqual(expected, actual)
		print "Created C blocks match expected."

		expected = D_BLOCKS
		actual = self.despy.create_shifted_blocks(d_zero)
		self.assertEqual(expected, actual)
		print "Created D blocks match expected."
		print "**Finished testing creation of shifted key blocks...**"


	def test_permute_key_with_pc2(self):
		print "**Finished testing key permutation with PC-2 table...**"
		K1 = "000110110000001011101111111111000111000001110010"
		K2 = "011110011010111011011001110110111100100111100101"
		K3 = "010101011111110010001010010000101100111110011001"
		K4 = "011100101010110111010110110110110011010100011101"
		K5 = "011111001110110000000111111010110101001110101000"
		K6 = "011000111010010100111110010100000111101100101111"
		K7 = "111011001000010010110111111101100001100010111100"
		K8 = "111101111000101000111010110000010011101111111011"
		K9 = "111000001101101111101011111011011110011110000001"
		K10 = "101100011111001101000111101110100100011001001111"
		K11 = "001000010101111111010011110111101101001110000110"
		K12 = "011101010111000111110101100101000110011111101001"
		K13 = "100101111100010111010001111110101011101001000001"
		K14 = "010111110100001110110111111100101110011100111010"
		K15 = "101111111001000110001101001111010011111100001010"
		K16 = "110010110011110110001011000011100001011111110101"

		expected_keys = ([K1, K2, K3, K4, K5, K6, K7, K8,
						K9, K10, K11, K12, K13, K14, K15, K16])
		for i in range(len(C_BLOCKS)):
			pair = C_BLOCKS[i] + D_BLOCKS[i]
			expected = expected_keys[i]
			actual = self.despy.permute_key_with_pc2(pair)
			print "Expected permuted key: {0}".format(expected)
			print "Actual permuted key: {0}".format(actual)
			self.assertEqual(expected, actual)
		print "**Finished testing key permutation with PC-2 table...**"


	def test_initial_permutation(self):
		print "**Testing initial permutation of message.**"
		message = "0000000100100011010001010110011110001001101010111100110111101111"
		expected = "1100110000000000110011001111111111110000101010101111000010101010"
		actual = self.despy.initial_permutation(message)
		print "Expected initial permutation: {0}".format(expected)
		print "Actual initial permutation: {0}".format(actual)
		self.assertEqual(expected, actual)
		print "**Finished testing initial permutation of message.**"


	def test_e_bit_selection(self):
		print "**Testing E-bit selection permutation.**"
		right_block = "11110000101010101111000010101010"
		expected =  "011110100001010101010101011110100001010101010101"
		actual = self.despy.e_bit_selection(right_block)
		print "Expected E-bit permutation: {0}".format(expected)
		print "Actual E-bit permutation {0}".format(actual)
		self.assertEqual(expected, actual)
		print "**Finished testing E-bit selection permutation.**"


	def test_feistel(self):
		print "**Testing Feistel function.**"
		data = "11110000101010101111000010101010"
		key = "000110110000001011101111111111000111000001110010"
		expected = "0010001101001010101010011011"
		actual = self.despy.feistel(data, key)
		print "Expected feistel output: {0}".format(expected)
		print "Actual feistel output: {0}".format(actual)
		self.assertEqual(expected, actual)
		print "**Finished testing Feistel function.**"


	def test_s_box_selection(self):
		print "**Testing S box selection.**"
		inputs = \
			([ 
			"011000",
		 	"010001",
		 	"011110",
		 	"111010",
		 	"100001",
		 	"100110", 
		 	"010100",
		 	"100111"
		 	])
		outputs = \
			([
			"0101", 
			"1100", 
			"1000", 
			"0010", 
			"1011", 
			"0101", 
			"1001", 
			"0111"
			])
		for i in range(len(inputs)):
			expected = outputs[i]
			actual = self.despy.s_box_selection(inputs[i], i+1)
			print "Expected S bit selection: {0}".format(expected)
			print "Actual S bit selection: {0}".format(actual)
			self.assertEqual(expected, actual)
		print "**Finished testing S box selection.**"


	def test_build_s_box_output(self):
		print "**Testing the building of S box output.**"
		input = "011000010001011110111010100001100110010100100111"
		expected = "01011100100000101011010110010111"
		actual = self.despy.build_s_box_output(input)
		print "Expected S box output: {0}".format(expected)
		print "Actual S box output: {0}".format(actual)
		self.assertEqual(expected, actual)
		print "**Finished testing building of S box output.**"


if __name__ == '__main__':
    unittest.main()