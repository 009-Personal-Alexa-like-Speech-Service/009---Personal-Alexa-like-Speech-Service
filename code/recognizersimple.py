from recognizer import Recognizer
from typing import List
from spacy.tokens import Doc


class RecognizerSimple(Recognizer):
    """
    This class returns in comparison to a default text the correct answer to an input question.
    """

    def __init__(self, doc: Doc = None):
        self.doc = doc
        self.text = ""
        self.answer = ""

    def recognize(self, doc: Doc = None):
        self.answer = "bla bla bla"
        self.text = doc.text

        if self.compare(self.text, ["How old are you?", "What is your age?"]):
            self.answer = "I am 100000 years old."
            return True
        if self.text == "What is your name?":
            self.answer = "My name is Hal."
            return True
        if self.text == "Hello?":
            self.answer = "Hello Dave."
            return True
        if self.compare(self.text, ["Open Google." "Open browser."]):
            self.answer = "I open google.com for you."
            return True
        if self.compare(self.text, ["How are you?", "How are you doing?", "How are you feeling today?", "What is up?",
                                    "How is everything?", "How have you been?", "What are you up to?"]):
            self.answer = "I'm feeling good dave and you?"
            return True
        if self.compare(self.text, ["Tell me a joke.", "Do you know a joke?", "Tell me something funny."]):
            self.answer = "Did you hear about the monkeys who shared an Amazon account? They were Prime mates."
            return True

        return False

    @staticmethod
    def compare(text: str, phrases: List[str]):
        text = text.lower().strip()
        final_text = ""
        for character in text:
            if character.isalnum() or character.isspace():
                final_text += character
        for phrase in phrases:
            phrase = phrase.lower().strip()
            final_phrase = ""
            for character in phrase:
                if character.isalnum() or character.isspace():
                    final_phrase += character
            if final_text == final_phrase:
                return True

        return False
