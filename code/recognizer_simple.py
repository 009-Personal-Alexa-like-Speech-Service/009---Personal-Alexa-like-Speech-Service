from recognizer import Recognizer
from typing import List
import Spacy


class Recognizer_simple(Recognizer):

    def recognize(self, doc: Spacy.Doc):
        self.doc = doc
        self.text = str(doc)
        self.answer = "bla bla bla"

        if self.compare(self.text, ["How old are you?", "What is your age?"]):
            self.answer = "I am 100000 years old."
            return True
        if self.text == "What is your name?":
            self.answer = "My name is Hal."
            return True
        if self.compare(self.text, ["Open Google." "Open browser."]):
            self.answer = "I open google.com for you."
            return True
        if self.compare(self.text, ["How are you?", "How are you doing?", "How are you feeling today?", "What is up?", "How is everything?", "How have you been?", "What are you up to?"]):
            self.answer = "I'm feeling good dave and you?"
            return True
        if self.compare(self.text, ["Tell me a joke.", "Do you know a joke?", "Tell me something funny."]):
            self.answer = "Did you hear about the monkeys who shared an Amazon account? They were Prime mates."
            return True

        return False


    def compare(self, text:str, phrases:List[str]):
        text = text.lower().strip()
        finaltext = ""
        for character in text:
            if character.isalnum() or character.isspace():
                finaltext += character
        for phrase in phrases:
            phrase = phrase.lower().strip()
            finalphrase = ""
            for character in phrase:
                if character.isalnum() or character.isspace():
                    finalphrase += character
            if finaltext == finalphrase:
                return True

        return False
