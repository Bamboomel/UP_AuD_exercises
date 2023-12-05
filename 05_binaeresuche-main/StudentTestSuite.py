import unittest
from unittest.mock import Mock, patch
import solution

class StudentTestSuite(unittest.TestCase):
	def testEmpty(self):
		self.assertTrue(solution.isSubset([],[]))

	def testExample1(self):
		self.assertTrue(solution.isSubset([0,1,4,8,12,56,100,500], [0,1,12,56,500]))

	def testExample2(self):
		self.assertFalse(solution.isSubset([0,1,4,8,56,100,500], [0,1,12,56,500]))

	def testExample3(self):
		self.assertFalse(solution.isSubset([0,1,4,8,12,56,100,500], [0,1,12,20,56,500]))
	
	def testExample4(self):
		self.assertTrue(solution.isSubset([0,4,12,56,100,500], [0,4,12,56,100,500]))

	def testInterfaceFunctions(self):
		# Hier wird geprüft, ob alle Schnittstellenfunktionen korrekt benutzt werden

		# Die Funktion "merge" soll im Laufe des Programms mit bestimmten Parameterwerten aufgerufen werden
		mockRecursiveCall = Mock()
		with patch("solution.binSearch", mockRecursiveCall):
			solution.isSubset([0,1,4,8,56,100,500], [0,1,12,56,500])
			mockRecursiveCall.assert_called_with([0,1,4,8,56,100,500], 500, 0, 6)

		# Das Ergebnis von binSearch soll alleinig den Rückgabewert von isSubset bestimmen.
		with patch("solution.binSearch", Mock(return_value=True)):
			self.assertTrue(solution.isSubset([0,1,4,8,56,100,500], [0,1,12,56,500])) 

		# Das Ergebnis von binSearch soll alleinig den Rückgabewert von isSubset bestimmen.
		with patch("solution.binSearch", Mock(return_value=False)):
			self.assertFalse(solution.isSubset([0,1,4,8,56,100,500], [0,1,12,56,500])) 

	def testBinSearchFunction1(self):
		self.assertTrue(solution.binSearch([0,1,4,8,56,100,500], 4, 0, 6))

	def testBinSearchFunction2(self):
		self.assertFalse(solution.binSearch([0,1,4,8,56,100,500], 12, 0, 6))

	def testTeileUndHerrsche(self):
		# Hier wird geprüft, ob Sie Ihre Funktion nach dem Teile-und-Herrsche-Paradigma implementiert haben

		# Die Funktion "binSearch" soll sich rekursiv selbst aufrufen
		with patch("solution.binSearch", Mock(side_effect=solution.binSearch)):
			solution.isSubset([0,1,4,8,56,100,500], [0,1,12,56,500])
			self.assertTrue(solution.binSearch.call_count > 0) 