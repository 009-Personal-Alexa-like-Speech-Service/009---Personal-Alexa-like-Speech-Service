from recognizer import Recognizer
from spacy.tokens import Doc
import utilities


class RecognizerNamedEntities(Recognizer):
    """
    Recognizes named entities like people names, city names etc.
    """
    def __init__(self, doc: Doc = None):
        self.doc = doc
        self.answer = utilities.DAVE_STANDARD_ANSWER

    def recognize(self, doc: Doc):
        self.doc = doc
        for token in doc:
            if token.tag_ == "NNP":
                self.answer = f"The text contains at least one named entity: {token.text}"
                return True

        return False
