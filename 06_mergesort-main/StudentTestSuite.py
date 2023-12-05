import unittest
import solution
from unittest.mock import Mock, patch

class StudentTestSuite(unittest.TestCase):
	def testEmpty(self):
		self.assertEqual(solution.mergesort([]), [])

	def testExample1(self):
		actual = solution.mergesort([("movie1", 20), ("movie2", 40), ("movie3", 2), ("movie4", 32), ("movie5", 100), ("movie6", 78), ("movie7", 13), ("movie8", 85)])
		expected = [('movie5', 100), ('movie8', 85), ('movie6', 78), ('movie2', 40), ('movie4', 32), ('movie1', 20), ('movie7', 13), ('movie3', 2)]
		self.assertEqual(actual, expected)

	def testExample2(self):
		actual = solution.mergesort([("James Bond", 76), ("Inception", 40), ("The Wolf of Wall Street", 2), ("La La Land", 32), ("Joker", 100), ("Ziemlich beste Freunde", 78), ("Interstellar", 13), ("Herr der Ringe", 85)])
		expected = [('Joker', 100), ('Herr der Ringe', 85), ('Ziemlich beste Freunde', 78), ('James Bond', 76), ('Inception', 40), ('La La Land', 32), ('Interstellar', 13), ('The Wolf of Wall Street', 2)]
		self.assertEqual(actual, expected)

	def testExample3(self):
		actual = solution.mergesort([("Interstellar", 13), ("James Bond", 76), ("La La Land", 77), ("Ziemlich beste Freunde", 78), ("Inception", 40), ("Herr der Ringe", 85)])
		expected = [('Herr der Ringe', 85), ('Ziemlich beste Freunde', 78), ('La La Land', 77), ('James Bond', 76), ('Inception', 40), ('Interstellar', 13)]
		self.assertEqual(actual, expected)
		
	def testMergeFunction1(self):
		self.assertEqual(solution.merge([('movie2', 40), ('movie1', 20)], [('movie4', 32), ('movie3', 2)]), [('movie2', 40), ('movie4', 32), ('movie1', 20), ('movie3', 2)])
	
	def testMergeFunction2(self):
		self.assertEqual(solution.merge([('Ziemlich beste Freunde', 78)], [('Herr der Ringe', 85), ('Inception', 40)]), [('Herr der Ringe', 85), ('Ziemlich beste Freunde', 78), ('Inception', 40)])
		
	def testMergeFunction3(self):	
		self.assertEqual(solution.merge([('James Bond', 76)], [('Inception', 40)]), [('James Bond', 76), ('Inception', 40)])

	def testTeileUndHerrsche(self):
		# Hier wird geprüft, ob Sie Ihre Funktion nach dem Teile-und-Herrsche-Paradigma implementiert haben

		# Die Funktion "merge" soll sich rekursiv selbst aufrufen
		with patch("solution.merge", Mock(side_effect=solution.merge)):
			solution.mergesort([("movie1", 20), ("movie2", 40), ("movie3", 2), ("movie4", 32), ("movie5", 100), ("movie6", 78), ("movie7", 13), ("movie8", 85)])
			self.assertTrue(solution.merge.call_count > 0)