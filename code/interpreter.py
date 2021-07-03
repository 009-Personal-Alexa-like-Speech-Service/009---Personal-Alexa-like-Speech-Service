from recorder import Recorder
from speaker import Speaker
from recognizer_simple_math import Recognizer_simple_math
from recognizer_simple import Recognizer_simple
import spacy

class Interpreter():
    def __init__(self):
        self.spoken_words = None
        self.speaker = Speaker()
        self.doc = None
        self.recognizers = []
        self.recognizers.append(Recognizer_simple())
        self.recognizers.append(Recognizer_simple_math())
        self.nlp = spacy.load("en_core_web_sm")


    def execute(self, spoken_words:str=None):
        if not spoken_words:
            spoken_words = self.spoken_words
        if not spoken_words:
            print("error: Missing spoken words")
            return
        print(f"Hello Dave I understood: {self.spoken_words}")


        answer = ""
        doc = self.nlp(spoken_words)
        for recognizer in self.recognizers:
            if recognizer.recognize(doc):
                answer = recognizer.answer
                break
        if not answer:
            self.speaker.speak("Sorry Dave I did not understand you.")
        else:
            self.speaker.speak(answer)



if __name__ == "__main__":
    interpreter = Interpreter()
    interpreter.spoken_words = "The quick brown fox jumps over the lazy dog."
    interpreter.interprete()