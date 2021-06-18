import speech_recognition as sr

class Recorder():
    def play(self):
        pass

    def record(self):
        r = sr.Recognizer()
        r.pause_threshold = 3.0

        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        with sr.Microphone() as source:
            audio_data = r.record(source, duration=5)
        self.spoken_words = r.recognize_google(audio)

        return True











