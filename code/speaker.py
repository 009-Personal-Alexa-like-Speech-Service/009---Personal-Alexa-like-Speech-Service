import pyttsx3


class Speaker:
    """
    The speaker class gives Hal the opportunity to speak and supported by the library "pyttsx3"
    """

    def __init__(self):
        # initialize library
        self.engine = pyttsx3.init()
        self.set_language("en_US")

    def speak(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()

    def set_language(self, language: str = "en_US"):
        voices = self.engine.getProperty('voices')
        language_set = False
        for voice in voices:
            if not voice.languages:
                key = language.upper().replace("_", "-")
                if key in voice.id:
                    self.engine.setProperty('voice', voice.id)
                    language_set = True
                    break
            elif voice.languages[0] == language:
                self.engine.setProperty('voice', voice.id)
                language_set = True
                break
        if not language_set:
            self.engine.setProperty('voice', voices[0].id)


if __name__ == "__main__":
    speaker = Speaker()
    speaker.speak("Hello Dave")
