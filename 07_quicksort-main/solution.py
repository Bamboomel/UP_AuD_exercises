# TODO: Implementieren Sie die beiden Funktionen wie in der Aufgabenstellung beschrieben!
# Verändern Sie das Dictionary "languagePopularity" nicht!

languagePopularity = {"JavaScript": 1, "Java": 2, "Python": 3, "CSS": 4, "PHP": 5, "Ruby": 6, "C++": 7, "C": 8, "Shell": 9, "C#": 10}

# Hilfsfunktion: soll das Tupel (i,j) zurückgeben
def teile(L, low, high):
    p = (low + high)//2 # Pivotelement festlegen
    s = languagePopularity[L[p]] # dictionary Wertigkeit ermitteln
    #i = low - 1
    i = low
    j = high

    while i <= j:
       while languagePopularity[L[i]] < s:
           i += 1
       while languagePopularity[L[j]] > s:
           j -= 1
       if i <= j:
           temp = L[i]
           L[i] = L[j]
           L[j] = temp
           i += 1
           j -= 1
           return i,j

def quicksort(L, low, high):
    teilen = teile(L, low, high)
    i,j = teilen
    if low < j:
        quicksort(L, low, j)
    if i < high:
        quicksort(L, i, high)



    # if low < high:
    #     teilen = teile(L, low, high)
    #     left = quicksort(L[low:teilen[1]], low, teilen[1])
    #     right = quicksort(L[teilen[0]:high], teilen[0], high)
    #     arr = left + right
    #     return arr
    #
    # else:
    #     return L



def start(L):
    if len(L) <= 1:
        return L
    else:
        low = 0
        high = len(L)-1
        quicksort(L, low, high)
        return L

