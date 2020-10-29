import json
from difflib import get_close_matches
import time

start_time = time.time()
data = json.load(open("data.json"))
word = input("Enter word: ").lower()
start_time = time.time()


def def_word(word):

    if word in data.keys():
        return "\n".join(data[word])

    elif word.title() in data.keys():
        return "\n".join(data[word.title()])

    elif word.upper() in data.keys():
        return "\n".join(data[word.upper()])

    elif len(close_match_word(word)) > 0:
        close_word = "".join(close_match_word(word))
        answer = input(
            f"Did you mean '{close_word}'? Enter Y if yes, or N if no: ")
        if answer.upper() == 'Y':
            return "\n".join(data[close_word])
        else:
            return "Please double check and try again."

    else:
        return "The word doesn't exist. Please double check it."


def close_match_word(word):
    return get_close_matches(word, data.keys(), n=1, cutoff=0.8)


print(def_word(word))
print(f"{time.time() - start_time} seconds")
