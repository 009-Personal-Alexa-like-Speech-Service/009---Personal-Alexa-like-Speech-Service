import pyttsx3


class Speaker:
    """
    The speaker class gives Hal the opportunity to speak and supported by the library "pyttsx3"
    """

    def __init__(self):
        # initialize library
        self.engine = pyttsx3.init()

    def speak(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()


if __name__ == "__main__":
    speaker = Speaker()
    speaker.speak("Hello Dave")
