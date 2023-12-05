# TODO: Implementieren Sie die Funktionen wie in der Aufgabenstellung beschrieben!

def merge(leftPart, rightPart):
    merged_list = [] #leere Liste erstellen in die sortierte Werter reinkommen
    i, j = 0, 0

    while i < len(leftPart) and j < len(rightPart): #Schleife läuft solange Werte in Liste enthalten
        if leftPart[i][1] >= rightPart[j][1]: #Vergleich der Wersten Werte in den Listen
            merged_list.append(leftPart[i])   #Wert wird in oben erstellten Liste hinzugefügt und in der übergebenen Liste gelöscht
            i = i + 1
        else:
            merged_list.append(rightPart[j])  #selbiges Verfahren wie oben
            j = j + 1

    while i < len(leftPart):                  #Hinzufügen des letzten Wertes in der Liste (falls dieser in leftPart)
        merged_list.append(leftPart[i])
        i = i + 1

    while j < len(rightPart):
        merged_list.append(rightPart[j])      #Hinzufügen des letzten Wertes in der Liste (falls dieser in rightPart)
        j = j + 1

    return merged_list


def split(L):
    mid = len(L)//2                           #Ermitteln der Mitte der Liste
    left = L[:mid]                            #Teilen der Liste am Mittelelement
    right = L[mid:]
    sort_left = mergesort(left)               #rekursiver Aufruf für beide Listenhälften
    sort_right = mergesort(right)
    return merge(sort_left, sort_right)

def mergesort(L):
    if len(L) <= 1:                           #falls Liste leer oder nur ein Element enthalten kann diese direkt wiedergegeben werden
        return L
    else:
        return split(L)
