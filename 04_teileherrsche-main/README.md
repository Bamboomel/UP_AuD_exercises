# 4. Programmieraufgabe: Minimale Teilsumme nach Teile und Herrsche

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

Finden Sie die **minimale zusammenhängende Teilsumme** auf einer Sequenz aus ganzen Zahlen $\mathbb{Z}$. Orientieren Sie sich dabei an dem aus der Vorlesung bekannten Algorithmus zum Bestimmen der maximalen Teilsumme.

**Wichtig:** Anders als in der Vorlesung, werden negative Zahlen ganz normal betrachtet und nicht auf den Wert 0 aufgerundet (siehe Beispiele).   

Schreiben Sie eine Funktion `minTeilsumme` in Python. Diese Funktion erhält als Eingabe eine Liste `L` aus ganzen Zahlen. Sie ruft eine rekursive Funktion `minTeilsumme_TeileUndHerrsche` auf, welche als Eingabe eine Liste `L`, sowie eine untere und eine obere Indexgrenze, `low` und `high`, erwartet. Mithilfe des Paradigmas *Teile und Herrsche* soll die Funktion `minTeilsumme` am Ende, die minimal zusammenhängende Teilsumme zurückgeben.  

Sie können davon ausgehen, das die pre-Bedingungen der Funktionen, wie sie in der Vorlesung definiert wurden, eingehalten werden. 

**Wichtig:** Es werden nur Lösungen, die das Paradigma *Teile und Herrsche* verwenden, akzeptiert. 

&nbsp;

## Beispiele

| Mustereingabe | Erwarteter Rückgabewert der Funktion `minTeilsumme` |
| --- | --- |
| `[2,-1,0,-6,-2,2,7]` | `-9` |
| `[-1,4,2,-3,7,-3,0,-2,8]` | `-5` |
| `[3,2,1,5,1]` | `1` |
| `[-10,27,-50,28,-15,-26,-10,20,-6,-17,7,-2,6,-30,17,-18]` | `-96` |
