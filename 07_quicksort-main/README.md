# 7. Programmieraufgabe: Quicksort

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

Es wird angenommen, dass die Liste der beliebtesten Programmiersprachen auf *GitHub*, sortiert nach absteigender Popularität, wie folgt aussieht:
1. JavaScript
2. Java
3. Python
4. CSS
5. PHP
6. Ruby
7. C++
8. C
9. Shell
10. C#

Implementieren Sie das bekannte Sortierverfahren *Quicksort* aus der Vorlesung in-place (nicht die Alternative aus der Übung) in Python, um eine Liste von Programmiersprachen nach ihrer Popularität **absteigend** zu sortieren. 
Sie dürfen annehmen, dass ausschließlich Programmiersprachen aus diesem Ranking in der zu sortierenden Liste enthalten sind. 

Ihre Implementierung soll mindestens drei Funktionen enthalten: `start`, `quicksort` und `teile`. 
Die Funktion `start` erhält als Parameter eine Liste `L` mit Programmiersprachen als Strings. Die Funktion soll zum Schluss die sortierte Liste zurückgeben. Am Anfang der sortierten Liste soll sich die populärste Sprache, die unpopulärste hingegen am Ende der Liste befinden. 
Dazu ruft sie die rekursive Funktion `quicksort` auf, die als Eingabe die Liste `L` sowie zwei Indizes `low` und `high` erhält. 
Die Hilfsfunktion `teile` erhält die zu sortierende Liste und die beiden Indizes `low` und `high`. Sie sortiert die Liste `L` mit Hilfe des Pivotelementes, welches dabei stets das mittlere Element der Liste ist (siehe Vorlesung). Die Funktion soll am Ende die neuen Indizes in Form eines **Tupels (i, j)** zurückgeben. 

Um das Sortieren nach Popularität durchzuführen, benutzen Sie die Datenstruktur *dictionary*. Dafür steht das dictionary `languagePopularity` zur Verfügung, welches die oben genannten Relationen zwischen den Programmiersprachen enthält. 

**Wichtig:** Lösungen, die in Python eingebaute Sortierfunktionen wie z.B. `list.sort()`, `sort()`, `sorted()` oder ähnliche verwenden, werden nicht akzeptiert.

&nbsp;

## Beispiele

| Mustereingabe | Erwarteter Rückgabewert der Funktion `quicksort` |
| --- | --- |
| `["Java", "Shell", "CSS"]` | `['Java', 'CSS', 'Shell']` |
| `["C++", "Python", "JavaScript", "Ruby", "PHP"]` | `['JavaScript', 'Python', 'PHP', 'Ruby', 'C++']` |
| `["Ruby", "C#", "C#", "Python"]` | `['Python',  'Ruby',  'C#',  'C#']` |
| `["Java", "Java", "PHP", "Shell"]` | `['Java', 'Java', 'PHP', 'Shell']` |
| `[]` | `[]` |

