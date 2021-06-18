from recorder import Recorder
from speaker import Speaker

class Interpreter():
    def __init__(self):
        self.spoken_words = None
        self.speaker = Speaker()

    def execute(self, spoken_words:str=None):
        if not spoken_words:
            spoken_words = self.spoken_words
        if not spoken_words:
            print("error: Missing spoken words")
            return
        print(f"Hello Dave I understood: {self.spoken_words}")
        spoken_words = spoken_words.strip().lower()

        #  Interpreting commands
        if spoken_words == "How old are you?":
            self.speaker.speak("I am 100000 years old.")
        elif spoken_words == "What is your name?":
            self.speaker.speak("My name is Hal.")
        elif spoken_words == "Open Google.":
            self.speaker.speak("I open google.com for you.")
        elif spoken_words == "how are you":
            self.speaker.speak("i'm feeling good dave and you")
        else:
            self.speaker.speak("Sorry Dave, I am afraid I cant do this.")

