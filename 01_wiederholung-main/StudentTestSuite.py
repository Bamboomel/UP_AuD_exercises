import unittest
import solution

class StudentTestSuite(unittest.TestCase):
	def testMainFunction1(self):
		self.assertEqual(solution.main(15), "[17, 19, 21, 23, 25]False0xf")
	
	def testMainFunction2(self):
		self.assertEqual(solution.main(50), "[51, 53, 55, 57, 59]True0x32")

	def testMainFunction3(self):
		self.assertEqual(solution.main(27), "[29, 31, 33, 35, 37]False0x1b")
		
	def testFuncFunction1(self):
		L = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
		self.assertEqual(solution.func(L, 15), [17, 19, 21, 23, 25])

	def testFuncFunction2(self):
		L = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]
		self.assertEqual(solution.func(L, 50), [51, 53, 55, 57, 59])

	def testFuncFunction3(self):
		L = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
		self.assertEqual(solution.func(L, 27), [29, 31, 33, 35, 37])