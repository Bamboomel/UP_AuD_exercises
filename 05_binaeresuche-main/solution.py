# TODO: Implementieren Sie die beiden Funktionen wie in der Aufgabenstellung beschrieben! 

def binSearch(L, n, start, end):
    if end >= start:
        m = (start + end) // 2
        if (L[m] == n):
            return True
        if (L[m] > n and m > start):
            return binSearch(L,n,start,m-1)
        if (L[m] < n and m < end):
            return binSearch(L,n,m+1,end)
        else:
            return False
    else:
        return False

def isSubset(A, B):
    if (len(A) == 0 and len(B) == 0):
        return True
    if (len(A) == 0 and len(B) != 0):
        return False
    else:
        for i in range(len(B)):
            val = binSearch(A,B[i],0,len(A)-1)
            if (val == False):
                return False
        return True
