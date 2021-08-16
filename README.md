# morse
Translate text into Morse code. A small project to learn python and git.

## Idea and Credits
I found the basic idea on https://bmu-verlag.de/programmierideen-vorschlaege-fuer-die-umsetzung-eigener-programme/ while I was searching for interesting projects for my son to get an introduction into Python. This project also intends to introduce a basic understanding of git.

## Morse-Table
We are going to use this Table: https://de.wikipedia.org/wiki/Morsecode#Standard-Codetabelle

## Kurze git Anleitung für Einsteiger
### Das Projekt "clonen"
Falls Da das Projekt noch einmal komplett neu von github ziehen möchtest, dann funktioniert das über:

`git clone https://www.github.com/kochersg/morse`

Das ist nicht nötig, wenn Du das Projekt schon in einem Ordner hast. Aber falls z.B. noch jemand mitmachen möchte, dann kann er/sie das so von github ziehen.

### Einen aktuellen Stand von github ziehen (pull)
Für den Fall, dass Du den Stamm des Projektes ziehen möchtest, dann verwende folgendes:

`git pull origin main`

Das solltest Du immer machen, bevor Du loslegst.

### Änderungen in einem lokalen Repo überprüfen
Mit dem nächsten Befehl kannst Du prüfen, ob Du lokale Änderungen hast, oder auch ob Dateien noch nicht "getracked" werden.

`git status`

### Änderungen einchecken
Wenn Du Änderungen gemacht hast, dann kannst Du sie mit

`git commit -a -m"Hier eine Nachricht, was geändert wurde"`

einchecken und kommentieren.

### Dateien in ein Repository aufnehmen
Wenn Du eine neue Datei anlegst und später einchecken möchtest, dann musst Du sie ersmal mit 

`git add .\pfad\datei.ext`

hinzufügen. ".\pfad" ist natürlich der Unterordner und "datei.ext" muss durch den echten Dateinamen ersetzt werden.

### Dateien nach github schieben (push)
Wenn Du etwas mit mir teilen möchtest, dann verwendest Du folgendes Kommando:

`git push origin main`




