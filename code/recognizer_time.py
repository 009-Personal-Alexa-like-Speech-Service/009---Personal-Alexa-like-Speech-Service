from recognizer import Recognizer
# Import time library

from recognizer import Recognizer
import spacy
from spacy.tokens import Doc
# Import time library
import time
import utilities
from datetime import datetime

class Recognizer_time(Recognizer):


    def recognize(self, doc: Doc):
        self.doc = doc
        self.answer = utilities.DAVE_STANDARD_ANSWER

        if utilities.compare(doc.text, ["What time is it", "How late is it", "What's the time"]):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.answer = f"The current time is {current_time}"
            return True
        return False