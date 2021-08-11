import spacy
import utilities
from speaker import Speaker
from recognizersimplemath import RecognizerSimpleMath
from recognizersimple import RecognizerSimple
from recognizernamedentities import RecognizerNamedEntities
from recognizertime import RecognizerTime


class Interpreter:
    """
    The interpreter recognises an input of spoken words and is able to process the correct answer which is defined
    in each of our recognizer classes.
    """
    def __init__(self):
        self.spoken_words = None
        self.speaker = Speaker()
        self.doc = None
        self.recognizers = []
        self.recognizers.append(RecognizerSimple())
        self.recognizers.append(RecognizerSimpleMath())
        self.recognizers.append(RecognizerNamedEntities())
        self.recognizers.append(RecognizerTime())
        self.nlp = spacy.load("en_core_web_sm")
        self.answer = utilities.DAVE_STANDARD_ANSWER

    def execute(self, spoken_words: str = None):
        if not spoken_words:
            spoken_words = self.spoken_words
        if not spoken_words:
            print("error: Missing spoken words")
            return
        self.spoken_words = spoken_words
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
    # interpreter.spoken_words = "The quick brown fox jumps over the lazy dog."
    interpreter.spoken_words = "2*3"
    interpreter.spoken_words = "2*3.14"
    interpreter.spoken_words = "What time is it"
    interpreter.spoken_words = "Are you from Hamburg"
    if interpreter.execute():
        print(interpreter.answer)
