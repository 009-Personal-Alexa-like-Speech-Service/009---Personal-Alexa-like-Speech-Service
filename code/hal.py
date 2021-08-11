import sys
import utilities
from interpreter import Interpreter
from listener import Listener


class Hal:
    """
    Hal is our speech assistant and he starts to record spoken words after someone said "Hello Hal".
    And the speech assistant "Hal" reacts with an answer.
    """
    def __init__(self):
        self.listener = Listener()
        self.spoken_words = ""
        self.interpreter = Interpreter()

    def activate(self):
        print("mock: Hal is now activated and listening")
        print("Hello Dave what can I do for you?")
        self.main_menu()

    def main_menu(self):
        while True:
            utilities.clear_screen()
            print("*"*80)
            print("Hal main menu")
            print("*" * 80)
            print("\t press 1 to talk to Hal")
            print("\t press 2 to turn off Hal")
            inp = input("Please type 1 or 2 and press enter:")
            if inp == "1":
                self.start_listening()
            elif inp == "2":
                sys.exit()
            else:
                input("Wrong command please press enter to continue and repeat")

    def start_listening(self):
        self.spoken_words = self.listener.listen()
        self.interpreter.execute(self.spoken_words)
        self.spoken_words = self.listener.listen()

    @staticmethod
    def error(message=''):
        print(message)
        input('Invalid input. Please press enter to continue. ')
