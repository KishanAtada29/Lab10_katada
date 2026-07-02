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