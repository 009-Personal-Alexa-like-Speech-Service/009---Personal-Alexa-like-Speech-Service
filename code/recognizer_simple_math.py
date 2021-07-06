from recognizer import Recognizer
import Spacy

#
class Recognizer_simple_math(Recognizer):


    def recognize(self, doc:Spacy.Doc):
        self.doc = doc
        self.answer = "bla bla bla"

        # Check if just 3 Tokens, e.g. 3 x 4
        if len(doc) != 3:
            return False

        # Get mathematical operator
        operator = doc[1].text
        operant_left = doc[0].text
        operant_right = doc[2].text
        if operant_left.isnumeric() and operant_right.isnumeric():
            if operator == "*":
                self.answer = str(float(operant_left) * float(operant_right))
            elif operator == "-":
                self.answer = str(float(operant_left) - float(operant_right))
            elif operator == "+":
                self.answer = str(float(operant_left) + float(operant_right))
            elif operator == "/":
                self.answer = str(float(operant_left) / float(operant_right))
            else:
                return False
            return True

        return False

    def interprete (self):

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


