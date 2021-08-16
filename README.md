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

## Umgang mit externen Modulen (requirements.txt)
Für die Erzeugung der Beep-Töne benötigen wir andere Python Module wie z.B. `numpy` oder `wave`. Diese Module müssen getrennt 
installiert werden. Wir haben Dir hierfür mit `virtualenv` eine virtuelle Python-Umgebung angelegt. Im Visual Studio Code 
ist diese Umgebung normalerweise aktiviert (siehe in der Statusleiste links unten). Wenn Du Python-Kommandos direkt im 
Terminal ausführen möchtest, solltest Du diese virtuelle Python-Umgebung erst im Terminal aktivieren:

`source activate ./myenv/bin/activate` (Linux, Mac OS)

oder 

`.\myenv\Scripts\activate.bat` (Windows)

Dann wird die virtuelle Umgebung verwendet und nicht Deine Haupt-Python-Installation. Damit werden zusätzliche Module nur 
hier installiert und man hält sich die Hauptinstallation sauber. Man kann die benötigten Module entweder manuell mit 

`python -m pip install der_modul_name`

installieren oder alle nötigen Module einmal aus der Datei `requirements.txt`, die die Abhängigkeiten enthält. Für die Installation 
aller Module auf einmal verwendet man das Kommando:

`python -m pip install -r requirements.txt`

### Erzeugung der Datei requirements.txt
Die Datei kann man automatisch aus der virtuellen Python-Umgebung erzeugen. Hierzu muss vorher auf jeden Fall die virtuelle Umgebung 
aktiviert werden (siehe oben). Dann wird die Datei `requirements.txt` über folgendes Kommando erzeugt:

`python -m pip freeze > requirements.txt`




