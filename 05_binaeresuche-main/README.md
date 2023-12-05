# 5. Programmieraufgabe: Binäre Suche

## Allgemeine Hinweise

Bitte lesen Sie die folgenden Hinweise genau durch!

* Sie haben max. drei Versuche, eine korrekte Lösung einzureichen.
* Bitte verwenden Sie die `solution.py` als Basis. Beachten Sie dabei:
    - Behalten Sie die *Schnittstellen* der zu implementierenden Funktionen genau bei.
    - Fügen Sie *keinen* unnötigen *Code außerhalb der Funktionen* ein, d.h. *vermeiden* Sie auch die Verwendung von *globalen Variablen*.
    - Verwenden Sie *keine `input`- oder `import`-Anweisungen*.
* Testen Sie Ihren Code selbst mit den von uns zur Verfügung gestellten Tests, bevor Sie ihn einreichen! Sie können auch weitere Testfälle hinzufügen, die Sie sich selbst ausdenken! Wir testen Ihren Code ebenfalls noch mit zusätzlichen Eingaben.
* Die Abgabe erfolgt individuell. Kopieren von Code von anderen Studierenden ist verboten und wird als Betrugsversuch interpretiert.
* Verwenden Sie *Python 3* (nicht 2).

&nbsp;

**Für diese Aufgabe wird ingesamt 1 Punkt vergeben.**

&nbsp;

## Aufgabenstellung

Schreiben Sie eine Funktion `isSubset` in Python, die überprüft, ob die Menge B eine Teilmenge der Menge A ist. Benutzen Sie dabei den in der Vorlesung vorgestellten Algorithmus *binSearch*. 

Die Funktion `isSubset` erhält als Eingabe zwei endliche Mengen `A,B` $\subset \mathbb{Z}$, in Form von Listen. Zur Vereinfachung dürfen Sie annehmen, dass alle gegebenen Mengen sortiert sind. Die Funktion soll mittels binärer Suche prüfen, ob $B \subseteq A$ gilt. 

Dazu ruft sie eine rekursive Funktion `binSearch` auf, die Sie ebenfalls schreiben sollen. Als Eingabe erhält diese Funktion eine Liste `L`, ein zu suchendes Element `k` sowie die Indexpositionen `startIndex` und `endIndex`. 
Falls $B \subseteq A$ gilt, soll die Funktion `isSubset` `True` zurückgeben, ansonsten `False`.  

**Wichtig:** Es werden nur Lösungen akzeptiert, die den Algorithmus *binSearch* verwenden und diesen rekursiv implementieren. Verwenden Sie nicht **any(), all(), in-Operator, filter()** oder ähnliche in Python eingebaute Funktionen.  

&nbsp;

## Beispiele

| Mustereingabe | Erwarteter Rückgabewert der Funktion `isSubset` |
| --- | --- |
| `[], []` | `True` |
| `[0,1,4,8,12,56,100,500], [0,1,12,56,500]` | `True` |
| `[0,1,4,8,56,100,500], [0,1,12,56,500]` | `False` |
| `[0,1,4,8,12,56,100,500], [0,1,12,20,56,500]` | `False` |
| `[0,4,12,56,100,500], [0,4,12,56,100,500]` | `True` |