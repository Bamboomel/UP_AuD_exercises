import unittest
import solution

class StudentTestSuite(unittest.TestCase):
	def testExample1(self):
		self.assertEqual(solution.createHashTable(['Laura', 'Max', 'Andreas', 'Lisa', 'Xavier', 'Markus']), {0: None, 1: None, 2: 'Xavier', 3: None, 4: None, 5: 'Lisa', 6: 'Laura', 7: 'Markus', 8: 'Andreas', 9: 'Max', 10: None, 11: None, 12: None})

	def testExample2(self):
		self.assertEqual(solution.createHashTable(['Max', 'Maximilian', 'Simone', 'Klaus', 'Richard', 'Sina', 'Maximiliane', 'Jutta', 'Andreas', 'Armin', 'Sebastian', 'Lisa', 'Anne']), {0: 'Maximiliane', 1: 'Sebastian', 2: 'Anne', 3: 'Klaus', 4: 'Simone', 5: 'Armin', 6: 'Jutta', 7: 'Lisa', 8: 'Andreas', 9: 'Max', 10: 'Maximilian', 11: 'Richard', 12: 'Sina'})

	def testExample3(self):
		self.assertEqual(solution.createHashTable([]), {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None, 11: None, 12: None})