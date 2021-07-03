from recognizer import Recognizer
import Spacy


class Recognizer_named_entities(Recognizer):

    def recognize(self, doc: Spacy.Doc):
        self.doc = doc
        self.text = str(doc)
        self.answer = "bla bla bla"

    doc = nlp("San Francisco considers banning sidewalk delivery robots")

    # document level
    ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
    print(ents)

    # token level
    ent_san = [doc[0].text, doc[0].ent_iob_, doc[0].ent_type_]
    ent_francisco = [doc[1].text, doc[1].ent_iob_, doc[1].ent_type_]
    print(ent_san)  # ['San', 'B', 'GPE']
    print(ent_francisco)  # ['Francisco', 'I', 'GPE']