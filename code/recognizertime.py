import utilities
from recognizer import Recognizer
from spacy.tokens import Doc
from datetime import datetime


class RecognizerTime(Recognizer):
    """
    This class returns the current time of the following questions. And returns a standard answer if it's not one of the
    defined questions.
    """

    def __init__(self, doc: Doc = None):
        self.doc = doc
        self.answer = ""

    def recognize(self, doc: Doc):
        self.answer = utilities.DAVE_STANDARD_ANSWER

        if utilities.compare(doc.text, ["What time is it", "How late is it", "What's the time"]):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.answer = f"The current time is {current_time}"
            return True
        return False
