import Game

class Guess:

    def __init__(self):

        self.Game = Game.Game()
        self.gameList = []
        self.gameRoundsCounter = 0

    def main(self):

        self.gameList.append(Game.Game(self.gameRoundsCounter))
        shouldContinue = True

        print("** The Great Guessing Game **")

        while shouldContinue:
            print("\nCurrent Guess: %s" % self.gameList[self.gameRoundsCounter].currentGuess)
            action = input("\ng = guess, t = tell me, l for a letter, and q to quit").lower()

            if action not in "gtlq" or len(action) != 1:
                print("\n@")
                print("@ FEEDBACK: I don't know how to do that!")
                print("@\n\n")
                continue

            if action == 'g':
                self.try_guess()
            elif action == 't':
                self.tell_me()
            elif action == 'l':
                self.try_letter()
            elif action == 'q':
                print("\n@")
                wantToQuit = input("Are you sure you want to quit?(y/n)").lower()
                print("@")
                if wantToQuit == "y":
                    shouldContinue = False
                    self.print_report()
                    print("\n@")
                    print("@ FEEDBACK: Bye-bye! Thank you for playing the game!")
                    print("@")

    def try_guess(self):

        userGuess = input("\nPlease enter guess:").lower()

        currentWordString = str(self.gameList[self.gameRoundsCounter].currentWord)

        if userGuess == currentWordString:
            self.gameList[self.gameRoundsCounter].isSuccess = True
            self.gameList[self.gameRoundsCounter].Finish = True
            print("\n@")
            print("@ FEEDBACK: Woo hoo! It was a correct guess..!")
            print("@")
            self.update_score()
            self.start_new_game()
        else:
            self.gameList[self.gameRoundsCounter].incorrectGuesses += 1
            print("\n@")
            print("@ FEEDBACK: Try again, Loser! It wasn't a correct guess..!")
            print("@")

    def try_letter(self):

        letter = input("\nEnter a letter:").lower()

        if len(letter) != 1:
            print("\n@")
            print("@ FEEDBACK: Not a valid single letter! Please, Try again.")
            print("@")
            return

        self.gameList[self.gameRoundsCounter].turnOverLetters += 1

        currentGuessString = str(self.gameList[self.gameRoundsCounter].currentGuess)
        currentWordString = str(self.gameList[self.gameRoundsCounter].currentWord)

        numberOfOccurrences = currentWordString.count(letter)
        charOccurrenceList = self.find_occurrences(currentWordString, letter)

        if len(charOccurrenceList) > 0:
            print("\n@")
            print("@ FEEDBACK: You found %d letters" % numberOfOccurrences)
            print("@")
            for index in charOccurrenceList:
                if currentGuessString[index] == "-":
                    currentGuessString = currentGuessString[:index] + letter + currentGuessString[index + 1:]
                else:
                    print("\n@")
                    print("@ FEEDBACK: But you already previously revealed the letter: '%s'" % letter)
                    print("@")
                    break

            self.gameList[self.gameRoundsCounter].currentGuess = currentGuessString

            if currentGuessString == currentWordString:
                self.gameList[self.gameRoundsCounter].isSuccess = True
                self.gameList[self.gameRoundsCounter].Finish = True
                print("\n@")
                print("@ FEEDBACK: Woo hoo! You ended up revealing all the missing character.")
                print("@")
                self.update_score()
                self.start_new_game()

        else:
            self.gameList[self.gameRoundsCounter].missedLetters += 1
            print("\n@")
            print("@ FEEDBACK: Oops! It wasn't a match. Try again.")
            print("@")

    def tell_me(self):

        self.gameList[self.gameRoundsCounter].GaveUp = True
        self.gameList[self.gameRoundsCounter].Finish = True
        print("\n@")
        print("@ FEEDBACK: You gave up! The correct guess was: %s" % self.gameList[self.gameRoundsCounter].currentWord)
        print("@")
        self.update_score()
        self.start_new_game()

    def update_score(self):

        currentScore = float(self.gameList[self.gameRoundsCounter].score)
        incorrectGuesses = int(self.gameList[self.gameRoundsCounter].incorrectGuesses)
        turnOverLetters = int(self.gameList[self.gameRoundsCounter].turnOverLetters)
        currentGuessString = str(self.gameList[self.gameRoundsCounter].currentGuess)
        currentWordString = str(self.gameList[self.gameRoundsCounter].currentWord)
        GaveUp = bool(self.gameList[self.gameRoundsCounter].GaveUp)
        isSuccess = bool(self.gameList[self.gameRoundsCounter].isSuccess)

        if isSuccess:
            charIndex = 0
            pointValuesForLettersDictionary = Game.Game.pointValuesForLettersDictionary
            for char in currentGuessString:
                if char == "-":
                    charFromWord = currentWordString[charIndex]
                    pointValueForChar = pointValuesForLettersDictionary.get(charFromWord)
                    currentScore += pointValueForChar
                charIndex += 1

            if turnOverLetters > 0:
                currentScore = currentScore / turnOverLetters

            if incorrectGuesses > 0:
                while incorrectGuesses > 0:
                    currentScore = currentScore - (currentScore * 0.10)
                    incorrectGuesses -= 1

        if GaveUp:
            charIndex = 0
            pointValuesForLettersDictionary = Game.Game.pointValuesForLettersDictionary
            for char in currentGuessString:
                if char == "-":
                    charFromWord = currentWordString[charIndex]
                    pointValueForChar = pointValuesForLettersDictionary.get(charFromWord)
                    currentScore -= pointValueForChar
                charIndex += 1

        self.gameList[self.gameRoundsCounter].score = currentScore

    def start_new_game(self):

        self.gameRoundsCounter += 1
        self.gameList.append(Game.Game(self.gameRoundsCounter)) 
        print("\n")
        print(" Game ended, You are playing a new game. ".center(70, "*"))

    def find_occurrences(self, s, ch):

        return [i for i, letter in enumerate(s) if letter == ch]

    def print_report(self):

        finalScore = 0.0
        gameIndex = 0
        Finish = bool(self.gameList[gameIndex].Finish)

        if not Finish:
            return

        print("\n@")
        print("@ Game Report:")
        print("@")
        print("\n")
        print("Game".ljust(8, " ") + "Word".ljust(8, " ") + "Status".ljust(11, " ") + "Bad Guesses".ljust(15, " ") + "Missed Letters".ljust(18, " ") + "Score".ljust(8, " "))
        print("----".ljust(8, " ") + "----".ljust(8, " ") + "------".ljust(11, " ") + "-----------".ljust(15, " ") + "---------------".ljust(18, " ") + "-----".ljust(8, " "))

        while gameIndex <= self.gameRoundsCounter:
            gameNumber = str(gameIndex + 1)
            word = str(self.gameList[gameIndex].currentWord)
            if bool(self.gameList[gameIndex].isSuccess):
                status = "Success"
            elif bool(self.gameList[gameIndex].GaveUp):
                status = "Gave up"
            else:
                status = "NIL"
            badGuesses = str(self.gameList[gameIndex].incorrectGuesses)
            missedLetters = str(self.gameList[gameIndex].missedLetters)
            scoreFloat = float(self.gameList[gameIndex].score)
            score = "{0:.2f}".format(scoreFloat)
            Finish = bool(self.gameList[gameIndex].Finish)
            if Finish:
                print(gameNumber.ljust(8, " ") + word.ljust(8, " ") + status.ljust(11, " ") + badGuesses.ljust(15, " ") + missedLetters.ljust(18, " ") + score.ljust(8, " "))
                finalScore = finalScore + float(self.gameList[gameIndex].score)
            gameIndex += 1
            status = "NIL"
        print("\nFinal Score: %.2f" % finalScore)


if __name__ == '__main__':
    Guess = Guess()
    Guess.main()