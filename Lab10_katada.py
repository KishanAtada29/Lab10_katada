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

            file_open = self._filepath.open('r', encoding = 'utf-8')

            for line in file_open:
                line = line.translate(translation).lower()
                words = line.split()
                for word in words:
                    if word in self._frequiences:
                        self._frequiences[word] += 1
                    else:
                        self._frequiences[word] = 1
            return True
            
        except  FileNotFoundError:
            return False
    
    def print_report(self):
        for word in sorted(self._frequiences.keys()):
            print(f'{word}. {self._frequiences[word]}')

def main():
    files = {
    "1": pathlib.Path("princess_mars.txt"),
    "2": pathlib.Path("Tarzan.txt"),
    "3": pathlib.Path("treasure_island.txt"),
    "4": pathlib.Path("monte_cristo.txt"),
    }

    while True:
        print("--- Word Analyzer ---")
        print("1. Princess of Mars")
        print("2. Tarzan")
        print("3. Treasure Island")
        print("4. Monte Cristo")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
 
        if choice == "5":
            print("Goodbye!")
            break
 
        if choice not in files:
            print("Invalid choice. Please select from 1-5.")
            input("Press Enter to return to the menu...")
            continue
 
        filename = files[choice]
        print(f"Processing '{filename}'..")
 
        analyzer = WordAnalyzer(filename)
        success = analyzer.process_file()
 
        if success:
            analyzer.print_report()
        else:
            print(f"Error: Could mot find the file '{filename}'.")
 
        input("Press Enter to return to the menu...")
 
 
if __name__ == "__main__":
    main()