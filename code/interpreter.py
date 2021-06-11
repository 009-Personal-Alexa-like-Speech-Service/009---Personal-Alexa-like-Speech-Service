from recorder import Recorder
from speaker import Speaker

class Interpreter():
    def __init__(self):
        self.spoken_words = None
        self.speaker = Speaker

    def process(self, recording: Recorder):
        print("mock: processing actual recording")
        # get words form recording
        self.spoken_words = "mock: some spoken words"
        return self.spoken_words

    def execute(self, spoken_words=None):
        if not spoken_words:
            spoken_words = self.spoken_words
        if not spoken_words:
            print("mock: Missing spoken words")


        #  Interpreting commands
        if spoken_words == "How old are you?":
            self.speaker.speak("I am 100000 years old.")
        elif spoken_words == "What is your name?":
            self.speaker.speak("My name is Hal.")
        elif spoken_words == "Open Google.":
            self.speaker.speak("My name is Hal.")
        else:
            self.speaker.speak("Sorry Dave, I am afraid I cant do this.")

