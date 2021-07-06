from recognizer import Recognizer
import spacy
from spacy.tokens import Doc
import utilities



class Recognizer_named_entities(Recognizer):

    def recognize(self, doc:Doc):
        self.doc = doc
        self.answer = utilities.DAVE_STANDARD_ANSWER
        for token in doc:
            if token.tag_ == "NNP":
                self.answer = f"The text contains at least one named entity: {token.text}"
                return True

        return False


    def das_ist_ein_bloeder_test(self):
        doc = nlp("San Francisco considers banning sidewalk delivery robots")

        # document level
        ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
        print(ents)

        # token level
        ent_san = [doc[0].text, doc[0].ent_iob_, doc[0].ent_type_]
        ent_francisco = [doc[1].text, doc[1].ent_iob_, doc[1].ent_type_]
        print(ent_san)  # ['San', 'B', 'GPE']
        print(ent_francisco)  # ['Francisco', 'I', 'GPE']