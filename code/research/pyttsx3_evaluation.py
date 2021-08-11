import pyttsx3

def set_language(engine, language:str = "en_US"):
    voices = engine.getProperty('voices')
    language_set = False
    for voice in voices:
        print(voice)
        if not voice.languages:
            key = language.upper().replace("_", "-")
            if key in voice.id:
                engine.setProperty('voice', voice.id)
                language_set = True
                break
        elif voice.languages[0] == language:
            engine.setProperty('voice', voice.id)
            language_set = True
            break
    if not language_set:
        engine.setProperty('voice', voices[0].id)



engine = pyttsx3.init()
set_language(engine, "de_DE")
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()