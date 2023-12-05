# TODO: Implementieren Sie die beiden Funktionen wie in der Aufgabenstellung beschrieben!

def func(L, x):
	rückgabe_liste = []
	for i in range(len(L)):
		if (L[i] > x) and (L[i]%2 != 0):
			rückgabe_liste.append(L[i])

	if len(rückgabe_liste) >= 5:
		return rückgabe_liste[:5]
	return rückgabe_liste




		
def main(n):
	L = []
	for i in range(20, 2 * n + 1, 1):
		L.append(i)
	L = [x - 5 for x in L]

	# ungeraden Werte durch Function erhalten
	rückgabe_liste = func(L,n)

	# erstellen einer Liste für die spätere Ausgabe
	ausgabe_liste = []
	# ungeraden Werte in der Liste speichern
	ausgabe_liste.append(rückgabe_liste)

	# Ermitteln der Summe aller Werte aus der von func übergebenen Liste
	a = 0
	for i in range(len(rückgabe_liste)):
		a = a + rückgabe_liste[i]
	# Bedingungen aufstellen und entweder True oder False in Liste speichern
	if a > 200:
		ausgabe_liste.append(True)
	else:
		ausgabe_liste.append(False)

	# n als Hexadecimal in Liste hinzufügen
	ausgabe_liste.append(hex(n))

	# Liste in String umwandeln
	ausgabe_string = f'[{", ".join(str(x) for x in ausgabe_liste[0])}]{str(ausgabe_liste[1])}{ausgabe_liste[2]}'

	return ausgabe_string






