import unittest
from unittest.mock import Mock, patch
import solution

class StudentTestSuite(unittest.TestCase):
	def testExample1(self):
		self.assertEqual(solution.minTeilsumme([2,-1,0,-6,-2,2,7]),-9)

	def testExample2(self):
		self.assertEqual(solution.minTeilsumme([-1,4,2,-3,7,-3,0,-2,8]),-5)

	def testExample3(self):
		self.assertEqual(solution.minTeilsumme([3,2,1,5,1]),1)

	def testExample4(self):
		self.assertEqual(solution.minTeilsumme([-10,27,-50,28,-15,-26,-10,20,-6,-17,7,-2,6,-30,17,-18]),-96)

	def testInterfaceFunctions(self):
		# Hier wird geprüft, ob alle Schnittstellenfunktionen korrekt benutzt werden

		# Die Funktion "minTeilsumme" soll "minTeilsumme_TeileUndHerrsche" aufrufen und damit den Teile-und-Herrsche-Algorithmus starten.
		with patch("solution.minTeilsumme_TeileUndHerrsche", Mock()):
			solution.minTeilsumme([2,-1,0,-6,-2,2,7])
			solution.minTeilsumme_TeileUndHerrsche.assert_called_once_with([2,-1,0,-6,-2,2,7], 0, 6) 

		# Das Ergebnis von minTeilsumme_TeileUndHerrsche soll alleinig den Rückgabewert von minTeilsumme bestimmen.
		with patch("solution.minTeilsumme_TeileUndHerrsche", Mock(return_value=True)):
			self.assertTrue(solution.minTeilsumme([1,2,3,4])) 

		# Das Ergebnis von minTeilsumme_TeileUndHerrsche soll alleinig den Rückgabewert von minTeilsumme bestimmen.
		with patch("solution.minTeilsumme_TeileUndHerrsche", Mock(return_value=False)):
			self.assertFalse(solution.minTeilsumme([1,2,3,4])) 

	def testTeileUndHerrsche(self):
		# Hier wird geprüft, ob die Funktion nach dem Teile-und-Herrsche-Paradigma implementiert wurde

		# Die Funktion "minTeilsumme_TeileUndHerrsche" soll sich rekursiv selbst aufrufen
		with patch("solution.minTeilsumme_TeileUndHerrsche", Mock(side_effect=solution.minTeilsumme_TeileUndHerrsche)):
			solution.minTeilsumme([2,-1,0,-6,-2,2,7])
			self.assertTrue(solution.minTeilsumme_TeileUndHerrsche.call_count > 0) 