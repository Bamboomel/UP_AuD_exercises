# 6. Programmieraufgabe: Mergesort

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

Die App eines Filmdatenbank-Betreibers möchte Ihren Usern eine Liste der beliebtesten Filme aus dem letzten Jahrzehnt anzeigen. Die Liste soll dabei **absteigend** sortiert nach dem Benutzer-Ranking angezeigt werden (siehe Beispiele). 

Ihre Aufgabe ist es, eine gegebene Liste aus der internen Film-Datenbank mit Hilfe des aus aus der Vorlesung bekannten Sortierverfahrens Mergesort, in Python, zu sortieren.

Schreiben Sie dazu drei Funktionen: `mergesort`, `split` und `merge`. 
Die Funktion `mergesort` erhält als Parameter eine Liste `L`, bestehend aus Tupeln (*movie, rating*), wobei *movie* vom Datentyp string und *rating* vom Datentyp integer ist. Ihre Funktion soll die Liste anhand der Rating-Werte **absteigend** sortieren und am Schluss zurückgeben.

Dazu ruft sie die Funktion `split` auf, welche als Eingabe ebenfalls die Liste `L` erwartet. Diese Funktion hat die Aufgabe, die Liste rekursiv zu teilen und dann durch den Aufruf der Hilfsfunktion `merge` wieder zusammenzuführen.

Dazu erhält `merge` zwei absteigend sortierte Listen `left` und `right`, die in eine einzige, absteigend sortierte Liste vereinigt werden soll und im Anschluss von der Funktion zurückgegeben wird.

Sie können davon ausgehen, dass keine zwei Filme denselben Rating-Wert haben und das Tupel keine fehlenden Werte haben. 

**Wichtig:** Lösungen, die eingebaute Sortierfunktionen in Python wie z.B. `list.sort()`, `sort()`, `sorted()` oder ähnliche verwenden, werden nicht akzeptiert.

&nbsp;

## Beispiele

| Mustereingabe | Erwarteter Rückgabewert der Funktion `mergesort` |
| --- | --- |
| `[]` | `[]` |
| `[("Interstellar", 13), ("James Bond", 76), ("La La Land", 77), ("Ziemlich beste Freunde", 78), ("Inception", 40), ("Herr der Ringe", 85)]` | `[('Herr der Ringe', 85), ('Ziemlich beste Freunde', 78), ('La La Land', 77), ('James Bond', 76), ('Inception', 40), ('Interstellar', 13) ]` |
| `[("James Bond", 76), ("Inception", 40), ("The Wolf of Wall Street", 2), ("La La Land", 32), ("Joker", 100), ("Ziemlich beste Freunde", 78), ("Interstellar", 13), ("Herr der Ringe", 85)]` | `[('Joker', 100), ('Herr der Ringe', 85), ('Ziemlich beste Freunde', 78), ('James Bond', 76), ('Inception', 40), ('La La Land', 32), ('Interstellar', 13), ('The Wolf of Wall Street', 2)]` |