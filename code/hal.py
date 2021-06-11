import os
import sys


from interpreter import Interpreter
from listener import Listener


class Hal():
    def activate(self):
        print("mock: Hal is now activated and listening")
        print("Hello Dave what can I do for you?")
        self.main_menu()

    def main_menu(self):
        while True:
            Hal.clear_screen()
            print("*"*80)
            print("Hal main menu")
            print("*" * 80)
            print("\t press 1 to talk to Hal")
            print("\t press 2 to turn off Hal")
            inp = input("Please type 1 or 2 and press enter:")
            if inp == "1":
                print("mock: I'm listening...")
                #initialize listener and start listening
            elif inp == "2":
                sys.exit()
            else:
                input("Wrong command please press enter to continue")


    def start_listening(self):
        l = Listener()
        i = Interpreter(l.listen())
        spoken_words = i.process(l.recording)
        print(f"Hello Dave did u mean: {spoken_words}")

        i.execute(spoken_words)




    @staticmethod
    def clear_screen():
       # for mac and linux(here, os.name is 'posix')
       if os.name == 'posix':
          _ = os.system('clear')
       else:
          # for windows platfrom
          _ = os.system('cls')



