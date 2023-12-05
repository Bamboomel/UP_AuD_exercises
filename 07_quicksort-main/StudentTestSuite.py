import unittest
from unittest.mock import patch, Mock
import solution

class StudentTestSuite(unittest.TestCase):
	def testEmpty(self):
		self.assertEqual(solution.start([]), [])

	def testExample1(self):
		self.assertEqual(solution.start(["Java", "Shell", "CSS"]), ['Java', 'CSS', 'Shell'])

	def testExample2(self):
		self.assertEqual(solution.start(["C++", "Python", "JavaScript", "Ruby", "PHP"]), ["JavaScript", "Python", "PHP", "Ruby", "C++"])

	def testExample3(self):
		self.assertEqual(solution.start(["Ruby", "C#", "C#", "Python"]), ["Python", "Ruby", "C#", "C#"])

	def testExample4(self):
		self.assertEqual(solution.start(["Java", "Java", "PHP", "Shell"]), ["Java", "Java", "PHP", "Shell"])
        
	def testTeileFunction(self):
		self.assertEqual(solution.teile(['Ruby', 'Python', 'C#', 'C#'], 0, 1), (1, 0))

	def testInterfaceFunctions(self):
		# Hier wird geprüft, ob die Funktion start direkt quicksort aufruft
		with patch("solution.quicksort", Mock()):
			solution.start(["Ruby","C#","C#","Python"])
			solution.quicksort.assert_called_once_with(["Ruby","C#","C#","Python"], 0, 3) 
			
	def testRecursion(self):
	# Hier wird geprüft, ob sich die Funktion selbst aufuft
		with patch("solution.quicksort", Mock(side_effect=solution.quicksort)):
			solution.start(["Java","Java","PHP","Shell"])
			self.assertTrue(solution.quicksort.call_count > 1) 
        
# die Lösung soll die "languagePopularity"-Datenstruktur nutzen, um die Liste zu sortieren
class StudentTestSuite2(unittest.TestCase):
	def testAnotherRanking(self):
		solution.languagePopularity= { "JavaScript": 1, "Java": 2, "Python": 4, "PHP": 6, "Ruby": 8, "C++": 5, "C": 9, "Shell": 10, "C#": 7, "Go": 3 }
		self.assertEqual(solution.start(["C++", "Python", "JavaScript", "Ruby", "PHP", "C#", "Go", "Java", "Shell", "C"]), ["JavaScript", "Java", "Go", "Python", "C++", "PHP", "C#", "Ruby", "C", "Shell"]) 