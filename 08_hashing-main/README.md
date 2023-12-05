# 8. Programmieraufgabe: Hashing

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

In der Vorlesung haben Sie Hashtabellen kennengelernt. Schreiben Sie eine Funktion `createHashTable` in Python, die eine Liste `L` bestehend aus Strings erhält, diese in eine Hashtabelle der Größe 13 einsortiert und die Hashtabelle dann zurückgibt. 

Dabei soll eine Hashfunktion verwendet werden, die durch folgenden Pseudo-Code beschrieben wird: 
```
für alle i Strings in der Liste L
    key <-- 0
    PRIME <-- 31
    für alle j von 0 bis [min(Länge des Strings oder 20 Durchläufe)-1]
        char <-- Buchstabe des Strings i an Stelle j 
        val <-- ( ASCII-Wert von char ) - 96 
        key <-- ( key * PRIME + val ) mod13
```

Als Strategie zur Kollisionsvermeidung verwenden Sie lineares Sondieren. Die Hashtabelle soll mit Hilfe von der Datenstruktur `dictionary` realisiert werden.

Die leere Hashtabelle ist bereits vorgegeben, wobei zu Beginn alle 13 Einträge den Wert `None` haben. Sie können annehmen, dass die Größe der Liste `L` die Größe der Hashtabelle nicht überschreitet. Als Rückgabe wird die nach dem Hashing-Verfahren erhaltene Hashtabelle vom Datentyp `dictionary` erwartet.

Verändern Sie die vorgegebene Schnittstelle der Funktion `createHashTable` nicht.  

&nbsp;

## Beispiele

| Mustereingabe | Erwarteter Rückgabewert der Funktion `createHashTable` |
| --- | --- |
| `['Laura', 'Max', 'Andreas', 'Lisa', 'Xavier', 'Markus']` | `{0:None, 1:None, 2:'Xavier', 3:None, 4:None, 5:'Lisa', 6:'Laura', 7:'Markus', 8:'Andreas', 9:'Max', 10:None, 11:None, 12:None}` |
| `['Max', 'Maximilian', 'Simone', 'Klaus', 'Richard', 'Sina', 'Maximiliane', 'Jutta', 'Andreas', 'Armin', 'Sebastian', 'Lisa', 'Anne']` | `{0:'Maximiliane', 1:'Sebastian', 2:'Anne', 3:'Klaus', 4:'Simone', 5:'Armin', 6:'Jutta', 7:'Lisa', 8:'Andreas', 9:'Max', 10:'Maximilian', 11:'Richard', 12:'Sina'}` |
| `[]` | `{0:None, 1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 10:None, 11:None, 12:None}` |