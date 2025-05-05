class StringDatabase:

    wordsList = []

    def __init__(self, filename):

        self.filename = filename
        self.read_words_from_file()

    def read_words_from_file(self):

        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    for word in line.split():
                        self.wordsList.append(word)
        except Exception as ex:
            print(ex)