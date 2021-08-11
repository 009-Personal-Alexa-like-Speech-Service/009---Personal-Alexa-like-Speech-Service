import os
from typing import List

DAVE_STANDARD_ANSWER = "Sorry Dave, I am afraid I can't do this."


def clear_screen():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platform
        _ = os.system('cls')


def compare(text: str, phrases: List[str]):
    text = text.lower().strip()
    final_text = ""
    for character in text:
        if character.isalnum() or character.isspace():
            final_text += character
    for phrase in phrases:
        phrase = phrase.lower().strip()
        final_phrase = ""
        for character in phrase:
            if character.isalnum() or character.isspace():
                final_phrase += character
        if final_text == final_phrase:
            return True

    return False
