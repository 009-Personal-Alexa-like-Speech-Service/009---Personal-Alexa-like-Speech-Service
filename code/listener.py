from recorder import Recorder
import hal

class Listener():
    def __init__(self):
        self.recorder = Recorder()
        self.text = ""
    def listen(self):
        self.text = ""
        hal.Hal.clear_screen()
        print("I'm listening. Give me three seconds break before I answer.")

        if self.recorder.record():
            self.text = self.recorder.spoken_words

        return self.text



