import mysql.connector
from difflib import SequenceMatcher
import time


con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter a word: ")
start_time = time.time()
query = cursor.execute(
    "SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()


def close_match_word(word):
    cursor.execute("SELECT * FROM Dictionary")
    results = cursor.fetchall()
    for result in results:
        if SequenceMatcher(a=word, b=result[0]).ratio() > 0.8:
            return result[0]


if results:
    for result in results:
        print(result[1])
elif close_match_word(word) != None:
    answer = input(
        f"Did you mean '{close_match_word(word)}'? Enter Y if yes, or N if no: ")
    cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" %
                   close_match_word(word))
    results = cursor.fetchall()
    if answer.upper() == "Y":
        for result in results:
            print(result[1])
    else:
        print("Please double check and try again.")
else:
    print("No word found!")

print(f"{time.time() - start_time} seconds")
