from recording import Recording

class Interpreter():
    def __init__(self):
        self.spoken_words = None

    def process(self, recording: Recording):
        print("mock: processing actual recording")
        self.spoken_words = "mock: some spoken words"
        return self.spoken_words

    def execute(self, spoken_words=None):
        if not spoken_words:
            spoken_words = self.spoken_words
        if not spoken_words:
            print("mock: Missing spoken words")


        #  Interpreting commands
        if spoken_words == "How old are you?":
            print("I am 100000 years old")
        elif

