import unittest
import solution

class StudentTestSuite(unittest.TestCase):
	def testExample1(self):
		adjL = [[(1,1),(2,3)], [(3,6),(4,7)], [(3,2),(5,9)], [], [(5,4),(6,10)], [(6,8)], []]
		startNode = 0
		self.assertEqual(solution.greedy(adjL,startNode), (10,47))

	def testExample2(self):
		adjL = [[(1,20),(6,30)], [(0,20),(3,40),(7,35)], [(4,40),(7,60)], [(2,70),(5,65)], [(5,10)], [(4,10)], [(2,30)], [(1,35)]]
		startNode = 0
		self.assertEqual(solution.greedy(adjL,startNode), (18,435))

	def testExample3(self):
		adjL=[[(1,4),(2,100)], [(3,3)], [(3,3)], [(2,10),(1,3)], []]
		startNode = 2
		self.assertEqual(solution.greedy(adjL,startNode), (2,9))