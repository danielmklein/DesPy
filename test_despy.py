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

		expected = None
		actual = self.despy.XOR(self.test5, self.test6)
		print "{0} XOR {1} is: {2}".format(self.test5, self.test6, actual) 
		self.assertEqual(expected, actual)


	def test_left_shift(self):
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


if __name__ == '__main__':
    unittest.main()