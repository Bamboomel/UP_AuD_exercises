# TODO: Implementieren Sie die Funktionen wie in der Aufgabenstellung beschrieben! 
# Verändern Sie die gegebenen Funktionsschnittstellen nicht und definieren Sie keine weiteren Funktionen

def lRandmin(L, low, high):
    mini = L[low]
    sum = 0
    for k in range(low, high+1):
        sum += L[k]
        if (sum < mini):
            mini = sum
    return mini

def rRandmin(L, low, high):
    mini = L[high]
    sum = 0
    for k in range(high, low-1, -1):
        sum += L[k]
        if (sum < mini):
            mini = sum
    return mini

def minTeilsumme_TeileUndHerrsche(L, low, high):
    if (low == high):
        #if L[low] < 0:
        return L[low]
        #else:
        #    return 0
    else:
        m = (low + high)//2
        minLinks = minTeilsumme_TeileUndHerrsche(L, low, m)
        minRechts = minTeilsumme_TeileUndHerrsche(L, m+1, high)
        minMisch = rRandmin(L, low, m) + lRandmin(L, m+1, high)
        return min(minLinks, minRechts, minMisch)

def minTeilsumme(L):
    return minTeilsumme_TeileUndHerrsche(L, 0, len(L)-1)
