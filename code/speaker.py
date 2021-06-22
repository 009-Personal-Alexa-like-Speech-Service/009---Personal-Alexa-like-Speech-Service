import pyttsx3

class Speaker():
    def __init__(self):
        #initialize library
        self.engine = pyttsx3.init()

    def speak(self, text:str):
        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == "__main__":
    s=Speaker()
    s.speak("Hello Dave")

