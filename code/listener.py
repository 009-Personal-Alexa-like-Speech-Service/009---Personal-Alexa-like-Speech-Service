from recorder import Recorder
import utilities

class Listener():
    def __init__(self):
        self.recorder = Recorder()
        self.text = ""
    def listen(self):
        self.text = ""
        utilities.clear_screen()
        print("I'm listening. Give me three seconds break before I answer.")

        if self.recorder.record():
            self.text = self.recorder.spoken_words

        return self.text


if __name__ == "__main__":
    listener = Listener()
    listener.listen()


