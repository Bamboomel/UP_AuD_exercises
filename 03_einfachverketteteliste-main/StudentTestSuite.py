import unittest
import solution

#Hinweis: Das Anfangsszenario in der Methode setUp wird vor jedem neuen Testbeispiel vorab ausgeführt und stellt somit die Ausgangssituation wieder her

class StudentTestSuite(unittest.TestCase):
    def setUp(self):
        self.os1 = solution.OperatingSystem("BSD", 1977)
        self.os2 = solution.OperatingSystem("Apple DOS 3.1", 1978)
        self.os3 = solution.OperatingSystem("Ms Dos", 1981)
        self.os4 = solution.OperatingSystem("Linux", 1991)
        self.os5 = solution.OperatingSystem("Solaris", 1992)
        self.os6 = solution.OperatingSystem("Windows 95", 1995)
        self.os8 = solution.OperatingSystem("Mac OS X", 2000)
        
        self.timeline = solution.OSTimeline()
        self.timeline.head = self.os1
        self.timeline.head.next = self.os2
        self.os2.next = self.os3
        self.os3.next = self.os4
        self.os4.next = self.os5
        self.os5.next = self.os6
        self.os6.next = self.os8

    def testExample1(self):
        self.assertFalse(self.timeline.insert("Red Hat Linux 6.2E", 2000))

    def testExample2(self):
        self.assertTrue(self.timeline.remove(1977))
        self.assertEqual(self.timeline.traverse(), [('Apple DOS 3.1', 1978), ('Ms Dos', 1981), ('Linux', 1991), ('Solaris', 1992), ('Windows 95', 1995), ('Mac OS X', 2000)])

    def testExample3(self):
        self.assertFalse(self.timeline.remove(1994))

    def testExample4(self):
        self.assertTrue(self.timeline.insert("Unix", 1969))
        self.assertEqual(self.timeline.traverse(), [('Unix', 1969), ("BSD", 1977), ('Apple DOS 3.1', 1978), ('Ms Dos', 1981), ('Linux', 1991), ('Solaris', 1992), ('Windows 95', 1995), ('Mac OS X', 2000)])

    def testExample5(self):
        self.assertTrue(self.timeline.remove(1981))
        self.assertEqual(self.timeline.traverse(), [("BSD", 1977), ('Apple DOS 3.1', 1978), ('Linux', 1991), ('Solaris', 1992), ('Windows 95', 1995), ('Mac OS X', 2000)])

    def testExample6(self):
        self.assertTrue(self.timeline.insert("Mac OS X 10.4", 2005))
        self.assertEqual(self.timeline.traverse(), [("BSD", 1977), ('Apple DOS 3.1', 1978), ("Ms Dos", 1981), ('Linux', 1991), ('Solaris', 1992), ('Windows 95', 1995), ('Mac OS X', 2000), ('Mac OS X 10.4', 2005)])
    
    def testExample7(self):
        self.assertTrue(self.timeline.insert("Mac OS X 10.4", 2005))
        self.assertTrue(self.timeline.remove(2005))
        self.assertEqual(self.timeline.traverse(), [("BSD", 1977), ('Apple DOS 3.1', 1978), ("Ms Dos", 1981), ('Linux', 1991), ('Solaris', 1992), ('Windows 95', 1995), ('Mac OS X', 2000)])
    
    def testExample8(self):
        self.assertTrue(self.timeline.insert("macOS Catalina", 2019))
        self.assertEqual(self.timeline.traverse(), [("BSD", 1977), ('Apple DOS 3.1', 1978), ("Ms Dos", 1981), ('Linux', 1991), ('Solaris', 1992), ('Windows 95', 1995), ('Mac OS X', 2000), ('macOS Catalina', 2019)])
    
    def testExample9(self):
        self.assertTrue(self.timeline.remove(1995))
        self.assertEqual(self.timeline.traverse(), [("BSD", 1977), ('Apple DOS 3.1', 1978), ("Ms Dos", 1981), ('Linux', 1991), ('Solaris', 1992), ('Mac OS X', 2000)])
    
    def testExample10(self):
        self.assertTrue(self.timeline.remove(1977))
        self.assertTrue(self.timeline.insert("Unix", 1969))
        self.assertTrue(self.timeline.remove(1981))
        self.assertTrue(self.timeline.insert("Mac OS X 10.4", 2005))
        self.assertTrue(self.timeline.remove(2005))
        self.assertTrue(self.timeline.insert("macOS Catalina", 2019))
        self.assertTrue(self.timeline.remove(1995))
        self.assertTrue(self.timeline.insert("Windows 98", 1998))
        self.assertEqual(self.timeline.traverse(), [('Unix', 1969), ('Apple DOS 3.1', 1978), ('Linux', 1991), ('Solaris', 1992), ('Windows 98', 1998), ('Mac OS X', 2000), ('macOS Catalina', 2019)])