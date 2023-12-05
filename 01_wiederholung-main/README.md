# 1. Programmieraufgabe: Wiederholung

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

Schreiben Sie eine Funktion `main` in Python, wobei die Funktion als Eingabe immer eine natürliche Zahl `n` $\in \mathbb{N}$, im Intervall [15,50], ist. Die Funktion verwendet die übergebene Zahl `n`, um die folgenden Aufgaben zu erledigen. Speichern Sie die 3 Ergebnisse der Aufgaben 2-4 als Elemente in eine Liste (vgl. Beispiele am Ende des Dokuments):

1.  Erstellen Sie eine Liste mit Schrittweite 1 im Intervall [20,2n] und verringern Sie anschließend jedes Element um 5. Übergeben Sie die erzeugte Liste sowie die Zahl n an die Funktion `func`.
2. Die Funktion `func` soll die ersten 5 ungeraden Nachfolger von `n` in einer Liste an die aufgerufene Funktion zurückgeben. 
3. Berechnen Sie die Summe aller Zahlen in der von `func` zurückgegebenen Liste und geben Sie `True` zurück, falls die Summe > 200 beträgt, sonst `False`.
4. Konvertieren Sie die Zahl `n` in eine Hexadezimalzahl.
5. Konvertieren Sie in einem letzten Schritt Ihre Liste mit den Ergebnissen der einzelnen Aufgaben in einen String und geben Sie diesen zurück. 

**Wichtig:** Die Reihenfolge der Listenelemente muss mit der Reihenfolge der Aufgaben übereinstimmen (vgl. Beispiele). 

&nbsp;

## Beispiele

| Mustereingabe | Erwarteter Rückgabewert der Funktion `main` |
| --- | --- |
| `15` | `'[17, 19, 21, 23, 25]False0xf'` |
| `50` | `'[51, 53, 55, 57, 59]True0x32'` |
| `27` | `'[29, 31, 33, 35, 37]False0x1b'` |


