class OperatingSystem:
    # Konstruktor
    def __init__(self, name=None, date=None):
        self.name = name
        self.releaseDate = date
        self.left = None
        self.right = None
        self.balance = None

    # Destruktor
    def __del__(self):
        return 0

    # Methode, die die Timeline durchläuft (preorder) und eine Liste der enthaltenen Betriebssysteme zurückgibt
    def traverse(self, L=None):
        if L == None:
            L = []

        L.append((self.name, self.releaseDate))
        if self.left:
            self.left.traverse(L)
        if self.right:
            self.right.traverse(L)
            
        return L

	# Der Einfachheit halber nehmen wir an, dass die Betriebssysteme in der richtigen Reihenfolge hinzugefügt werden.
	# ACHTUNG: Ändern Sie diese Methode nicht, da Ihnen die Student-Test-Suite ansonsten ein falsches Ergebnis liefern kann!
    def addOS(self, os):
        if os.releaseDate < self.releaseDate:
            if self.left:
                return self.left.addOS(os)
            else:
                self.left = os
        else:
            if self.right:
                return self.right.addOS(os)
            else:
                self.right = os


    def determineBalanceFactors(self, balanceFactors=None):
        # TODO: Implementieren Sie die Funktion wie in der Aufgabenstellung beschrieben!
        if balanceFactors == None:
            balanceFactors = []

        left = None
        left_val = 0
        right_val = 0
        right = None

        if self.left:
            self.left.determineBalanceFactors(balanceFactors)
            left = self.left.traverse()
            left_val = len(left)

        if self.right:
            self.right.determineBalanceFactors(balanceFactors)
            right = self.right.traverse()
            right_val = len(right)

        self.balance = left_val - right_val
        balanceFactors.append((self.name, self.balance))
        return balanceFactors

    