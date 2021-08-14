class CMorseTable():
    def __init__(self):
        self.table = self.fill_table()

    def __str__(self):
        outstr=''
        outstr+='Available letters in Morse table:\n'
        outstr+='---------------------------------\n'
        for letter in self.table:
            outstr+=letter+": "+self.table[letter]+'\n'
        return outstr
            

    @staticmethod
    def fill_table():
        return {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
        }

if __name__ == "__main__":
    pass