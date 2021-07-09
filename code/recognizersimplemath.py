from recognizer import Recognizer
from spacy.tokens import Doc


class RecognizerSimpleMath(Recognizer):

    def __init__(self, doc: Doc = None):
        self.doc = doc
        self.answer = ""

    def recognize(self, doc: Doc):
        self.answer = "bla bla bla"

        # Check if just 3 Tokens, e.g. 3 x 4
        if len(doc) != 3:
            return False

        # Get mathematical operator
        operator = doc[1].text
        operand_left = doc[0].text
        operand_right = doc[2].text
        self.dump(doc)
        if self.isfloat(operand_left) and self.isfloat(operand_right):
            if operator == "*":
                self.answer = str(float(operand_left) * float(operand_right))
            elif operator == "-":
                self.answer = str(float(operand_left) - float(operand_right))
            elif operator == "+":
                self.answer = str(float(operand_left) + float(operand_right))
            elif operator == "/":
                self.answer = str(float(operand_left) / float(operand_right))
            else:
                return False
            return True

        return False

    @staticmethod
    def interpret(doc: Doc):

        # Analyze syntax
        print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
        print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

        # Find named entities, phrases and concepts
        for entity in doc.ents:
            print(entity.text, entity.label_)

        # Find named entities, phrases and concepts
        for entity in doc.ents:
            print(entity.text, entity.label_)

        for token in doc:
            print(token.text)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                  token.shape_, token.is_alpha, token.is_stop)

        for token in doc:
            if token.pos_ == "NOUN":
                print(token, token.pos_)

    @staticmethod
    def dump(doc: Doc):
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                  token.shape_, token.is_alpha, token.is_stop)

    @staticmethod
    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False
