# TODO: Implementieren Sie die Funktion wie in der Aufgabenstellung beschrieben! 
# Nur rekursive Lösungen werden akzeptiert!

def transformToUppercase(s):
	if type(s) != str:
		return

	if len(s) == 0:
		return ''

	upper = transformToUppercase(s[1:])
	upper = s[0].upper() + upper

	return upper