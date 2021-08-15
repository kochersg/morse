# Hier werden die nötigen Module importiert. Wenn Du mit der Maus über das Wort "CMorseTable" gehst, 
# wird Dir die Dokumentation zur Klasse angezeigt. Die Dokumentation befindet sich direkt im Quellcode 
# der Klasse.
from morse.morse_table import CMorseTable

if __name__=='__main__':
    """
    Hier beginnt das Programm. Diese Befehle werden ausgeführt, wenn Du diese Datei mit Python ausführst.
    """
    # Ein Objekt der Klasse CMorseTable() wir erzeugt. Die Klasse selbst haben wir oben aus der Datei morse_table.py importiert, die im Ordner .\morse liegt. 
    mt = CMorseTable()

   # Hier geben wir Informationen zur Klasse aus. Diese werden in der Funktion CMorseTable.__str__() erzeugt, die wir nach unseren Bedürfnissen anpassen können.
    print(mt)