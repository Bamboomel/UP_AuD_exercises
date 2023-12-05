# TODO: Implementieren Sie die Funktion wie in der Aufgabenstellung beschrieben!

def createHashTable(L):
    hashTable = {0:None, 1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 10:None, 11:None, 12:None}

    for idx, name in enumerate(L):
        key = 0
        PRIME = 31
        for j in range(0,min(len(name),20)):
            char = name[j]
            val = ord(char) - 96
            key = (key * PRIME + val) % 13
        while (hashTable[key] is not None):
            key = (key + 1) % 13
        hashTable.update({key:name})
    return hashTable



