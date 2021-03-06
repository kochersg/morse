class CMorseTable():
    """
    A class to convert written text into morse code

    Attributes
    ----------
    table
        Dictionary with letters and numbers as keys and strings with dots and dashes as corresponding morse code as entry.

    Methods
    -------
    fill_table(), staticmethod
        Generates dictionary with letters and numbers as keys and morse strings like '.-' as morse code entry and returns ist

    """
    def __init__(self):
        """
        Parameters
        ----------
        None
        """
        self.table = self.fill_table()

    def __str__(self):
        """
        Generates the output string when the class object ist called with the print() command
        
        Parameters
        ----------
        None
        """
        outstr=''
        outstr+='Available letters in Morse table:\n'
        outstr+='---------------------------------\n'
        for letter in self.table:
            outstr+=letter+": "+self.table[letter]+'\n'
        return outstr
    
    def text_to_morse(self, text_to_translate:str="Hallo Welt"):
        """
        Translate a text string into a morse code string

        Parameters
        ----------
        text_to_translate:str, optional
            String of text to be translated. Default: "Hallo Welt"

        Returns
        -------
        Output string with morse -. symbols
        """
        out_str=''
        for letter in text_to_translate:
            out_str+=self.table[letter.lower()]
            out_str+=' '
        return out_str

    @staticmethod
    def fill_table():
        """
        Fills the morse table dictionary and returns it. The method is a staticmethod, 
        i.e. the method can be called without instantiating the class (no class object needed). 
        Just call CMorseTable.fill_table() directly.

        Note: we do not pass the member variable "self" to the method. This is a direct consequence of the @staticmethod decorator.
        """
        return {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '..-.',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '.-..',
            'm': '--',
            'n': '-.',
            'o': '---',
            'p': '.--.',
            'q': '--.-',
            'r': '.-.',
            's': '...',
            't': '-',
            'u': '..-',
            'v': '...-',
            'w': '.--',
            'x': '-..-',
            'y': '-.--',
            'z': '--..',
            ' ': '   ',
        }

# Dieser Teil des Codes k??nnte man ausf??hren, wenn man die Datei morse_table.py direkt mit Python ausf??hren w??rde. 
# In unserem Fall brauchen wir das nicht. Aber man k??nnte z.B. Code ausf??hren um Funktionen der Klasse direkt zu testen,
# unabh??ngig vom Hauptprogramm
if __name__ == "__main__":
    # In der if-Anweisung muss zwingend ein Kommando stehen. Wenn man nichts tun m??chte, 
    # schreibt man das pass-Kommando rein.
    pass