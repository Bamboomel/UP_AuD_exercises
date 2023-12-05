# 2. Programmieraufgabe: Rekursion

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

Schreiben Sie eine Funktion `transformToUppercase` in Python, die als Eingabe eine Zeichenkette `s` aus einzelnen Zeichen erhält und diese rekursiv in Großbuchstaben umwandelt. 

Die eingegebene Zeichenkette kann auch leer sein.

Als Ausgabe wird die Zeichenkette in Großbuchstaben erwartet. Diese soll als Rückgabewert der Funktion geliefert werden. Ausgaben auf der Konsole (mit print) werden nicht beachtet.

**Wichtig:** Es werden nur rekursive Lösungen akzeptiert. 

&nbsp;

## Beispiele

| Mustereingabe | Erwarteter Rückgabewert der Funktion `transformToUppercase` |
| --- | --- |
| `Hello World` | `HELLO WORLD` |
| `hello world` | `HELLO WORLD` |
| `#Algorithmen & Datenstrukturen123!` | `#ALGORITHMEN & DATENSTRUKTUREN123!` |
| `""`  (leerer String) | `""` (leerer String) |