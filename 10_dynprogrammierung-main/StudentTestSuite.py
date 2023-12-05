import unittest
import solution

class StudentTestSuite(unittest.TestCase):
	def testExample1(self):
		self.assertEqual(solution.packing(5, [1,2,3], [6,10,12]), (22, [0,6,10,16,18,22]))

	def testExample2(self):
		self.assertEqual(solution.packing(5, [2,3,4,5], [3,4,5,6]), (7, [0,0,3,4,5,7]))

	def testExample3(self):
		self.assertEqual(solution.packing(10, [5,4,6,3], [10,40,30,50]), (90, [0,0,0,50,50,50,50,90,90,90,90]))