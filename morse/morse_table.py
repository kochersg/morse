class CMorseTable():
    def __init__(self):
        self.table = self.fill_table()

    def __str__(self):
        print('Available letters in Morse table:')
        print('---------------------------------')
        for letter in self.table:
            print(letter+": "+self.table[letter])
            

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