class OperatingSystem:
	# Konstruktor
	def __init__(self, name=None, date=None):
		self.name = name
		self.releaseDate = date
		self.next = None

class OSTimeline:
	# Konstruktor
	def __init__(self):
		self.head = None

	# Methode, die die Timeline durchläuft und eine Liste der enthaltenen Betriebssysteme zurückgibt
	# ACHTUNG: Ändern Sie diese Methode nicht, da Ihnen die Student-Test-Suite ansonsten ein falsches Ergebnis liefern kann!
	def traverse(self):
		L = []
		currentNode = self.head
		while currentNode is not None:
			L.append((currentNode.name, currentNode.releaseDate))
			currentNode = currentNode.next
		return L

	# Methode, die ein neues Element in die Timeline einfügt
	def insert(self, name, releaseDate):
		newOS = OperatingSystem(name, releaseDate)
		currentNode = self.head														


		# Compare if list is empty
		if (currentNode is None):
			self.head = newOS
			print('inserted')
			return True #'inserted'

		# Compare for position 0
		if (newOS.releaseDate <= currentNode.releaseDate):
			newOS.next = currentNode
			self.head = newOS
			print('inserted')
			return True #'inserted'

		while(currentNode.next is not None): #while(currentNode is not None):
			if(newOS.releaseDate <= currentNode.next.releaseDate):
				if(newOS.releaseDate == currentNode.next.releaseDate): #actualNode.next.releaseDate):
					print('invalid year')
					return False #'invalid year' # False
				newOS.next = currentNode.next
				currentNode.next = newOS
				print('inserted')
				return True #'inserted' #True
			currentNode = currentNode.next									

		# If newOS is last element in list add it to the end
		currentNode.next = newOS
		print('inserted')
		return True #'inserted' #True

	# Methode, die das übergebene Element in der Timeline löscht
	def remove(self, yearToRemove):
		currentNode = self.head

		while (currentNode is not None):
			if (currentNode.releaseDate > yearToRemove):
				# if currentNode release date is larger than year to remove, we do not need to continue
				print('invalid year')
				return False #'invalid year' #False
			elif currentNode.releaseDate < yearToRemove:
				currentNode = currentNode.next
			elif currentNode.releaseDate == yearToRemove:
				if currentNode == self.head:
					if currentNode.next is not None:
						self.head = currentNode.next
					else:
						self.head = None
					print('removed')
					return True #'removed' #True
				if currentNode != self.head and currentNode.next is None:
					tmp_node = self.head
					while (tmp_node.next != currentNode):
						tmp_node = tmp_node.next
					tmp_node.next = None
					#currentNode = None
					print('removed')
					return True #'removed' #True
				if currentNode != self.head and currentNode.next is not None:
					tmp_node = self.head
					while (tmp_node.next != currentNode):
						tmp_node = tmp_node.next
					tmp_node.next = currentNode.next
					print('removed')
					return True #'removed' #True

		print('invalid year')
		return False #'invalid year' #False
	

# Hinweis: Der nachfolgende Code implementiert die Beispiel-Routine, wie im Aufgabenblatt dargestellt. 
# Sie können damit ihre Änderungen testen. Sie dürfen den Code beliebig anpassen, um weitere Fälle zu testen.
# Der Code zum Testen für die StudentTestSuite wird davon nicht beeinflusst. 

# os1  = OperatingSystem("BSD", 1977)
# os2  = OperatingSystem("Apple DOS 3.1", 1978)
# os3  = OperatingSystem("Ms Dos", 1981)
# os4  = OperatingSystem("Linux", 1991)
# os5  = OperatingSystem("Solaris", 1992)
# os6  = OperatingSystem("Windows 95", 1995)
# os7  = OperatingSystem("Mac OS X", 2000)
#
#
# timeline = OSTimeline()
# timeline.head = os1
# timeline.head.next = os2
# os2.next = os3
# os3.next = os4
# os4.next = os5
# os5.next = os6
# os6.next = os7
#
# # routine
# timeline.insert("Red Hat Linux 6.2E", 2000);
# timeline.remove(1977);
# timeline.remove(1994);
# timeline.insert("Unix", 1969);
# timeline.remove(1981);
# timeline.insert("Mac OS X 10.4", 2005);
# timeline.remove(2005);
# timeline.insert("macOS Catalina", 2019);
# timeline.remove(1995);
# timeline.insert("Windows 98", 1998);
# print(timeline.traverse());