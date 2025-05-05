import StringDatabase
import random


class Game:
    """
    Encapsulates game data and maintain information about specific game.
    """
    pointValuesForLettersDictionary = {
        "a": 8.17,
        "b": 1.49,
        "c": 2.78,
        "d": 4.25,
        "e": 12.70,
        "f": 2.23,
        "g": 2.02,
        "h": 6.09,
        "i": 6.97,
        "j": 0.15,
        "k": 0.77,
        "l": 4.03,
        "m": 2.41,
        "n": 6.75,
        "o": 7.51,
        "p": 1.93,
        "q": 0.10,
        "r": 5.99,
        "s": 6.33,
        "t": 9.06,
        "u": 2.76,
        "v": 0.98,
        "w": 2.36,
        "x": 0.15,
        "y": 1.97,
        "z": 0.07
    }

    def __init__(self, gameId = None):

        self.stringDatabaseObj = StringDatabase.StringDatabase('four_letters.txt')
        self.gameId = gameId
        self.currentWord = self.pick_random_word()
        self.currentGuess = "----"
        self.status = ""
        self.incorrectGuesses = 0
        self.missedLetters = 0
        self.turnOverLetters = 0
        self.isSuccess = False
        self.didGaveUp = False
        self.didFinish = False
        self.score = 0.0

    def pick_random_word(self):
        return random.choice(self.stringDatabaseObj.wordsList)