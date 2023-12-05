# TODO: Implementieren Sie die Funktion wie in der Aufgabenstellung beschrieben!

def packing(G, g, v):
    n = len(v)
    #Randfälle beachten
    if G <= 0 or n == 0 or len(g) != n:
        return 0

    #Erstellen der Tabelle mit verketterer for Schleife
    T = [[0 for weight in range(G+1)] for value in range(n)]

    #Befüllen mit Nullen (i = 0 Bedingung)
    for j in range(0, n):
        T[j][0] = 0

    #Betrachtung eines Wertes - falls Gewicht kleiner als max Gewicht: "einpacken"
    #(i > 0 and h < gi Bedingung)
    for i in range(0, G+1):
        if g[0] <= i:
            T[0][i] = v[0]

    #max wert, SONST Bedingung beachten
    for i in range(1, n):
        for j in range(1, G+1):
            val_1, val_2 = 0, 0
            if g[i] <= j:
                val_1 = v[i] + T[i-1][j-g[i]]
            val_2 = T[i-1][j]
            T[i][j] = max(val_1, val_2)
            #variablen vorher definiert um Übersichtlichkeit zu gewärleisten

    #Ausgabe des max values und der letzten Zeile
    return (T[n-1][G], T[n-1])

