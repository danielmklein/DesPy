'''
Daniel Klein
2.22.2014

The unit tests for my DES implementation.
'''

import unittest
from despy import DESpy

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
		c_blocks = ([
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
		d_blocks = ([
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
		expected = c_blocks
		actual = self.despy.create_shifted_blocks(c_zero)
		self.assertEqual(expected, actual)
		print "Created C blocks match expected."

		expected = d_blocks
		actual = self.despy.create_shifted_blocks(d_zero)
		self.assertEqual(expected, actual)
		print "Created D blocks match expected."
		print "**Finished testing creation of shifted key blocks...**"


if __name__ == '__main__':
    unittest.main()