import pathlib
import string
"""
    Author: Kishan Atada
    Purpose: Menu-driven program that lets the user select one of four text
    files, counts word frequency in the selected file, and prints an
    alphabetized report of words and their counts.
    Starter Code: None used.
    Date: July 1st , 2026
"""
class WordAnalyzer:
    def __init__(self,filepath):
        self._filepath = pathlib.Path(filepath)
        self._frequiences = {}

    def process_file(self):
        try:
            if not self._filepath.exists():
                raise FileNotFoundError
            translation = str.maketrans('','', string.punctuation)

            file_open = self._filepath.open()

            for line in file_open:
                line = line.translate(translation).lower()
                words = line.split()
                for word in words:
                    if word in self._frequiences:
                        self._frequiences[words] += 1
                    else:
                        self._frequiences[words] = 1
            
        except  FileNotFoundError:
            return False
    
    def print_report(self):
        for word in sorted(self._frequiences.keys()):
            print(f'{word}. {self._frequiences[word]}')

