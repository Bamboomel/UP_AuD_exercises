import unittest
import solution

class StudentTestSuite(unittest.TestCase):
	def testEmpty(self):
		self.assertEqual(solution.transformToUppercase(''), '')

	def testWithCapitalLetters(self):
		self.assertEqual(solution.transformToUppercase("Hello World"), "HELLO WORLD")

	def testString(self):
		self.assertEqual(solution.transformToUppercase("hello world"), "HELLO WORLD")

	def testStringWithSymbols(self):
		self.assertEqual(solution.transformToUppercase("#Algorithmen & Datenstrukturen123!"), "#ALGORITHMEN & DATENSTRUKTUREN123!")