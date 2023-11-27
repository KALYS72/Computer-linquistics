import random, json
from better_profanity import profanity
from datetime import datetime, timedelta

def talk(person, text):
    RED   = "\033[1;31m"  
    BLUE  = "\033[1;34m"
    YELLOW = '\033[33m'
    RESET = "\033[0;0m"
    if person == "human":
        text = profanity.censor(text)
        print("\n")
        print(RED + f"            {YELLOW}{text}{RESET}")
        print(RED + "            /         " + RESET)
        print(RED + " ||||||||| /          " + RESET)
        print(RED + " | -   - |            " + RESET)
        print(RED + " | O   O |            " + RESET)
        print(RED + "  \  ∆  /             " + RESET)
        print(RED + "   \_o_/              " + RESET)

    elif person == "robot":
        text = profanity.censor(text)
        print(BLUE + f"                             {YELLOW}{text}{RESET}")
        print(BLUE + "                             /         " + RESET)
        print(BLUE + "                 __________ /          " + RESET)
        print(BLUE + "                 |         |           " + RESET)
        print(BLUE + "                 |  ^   ^  |           " + RESET)
        print(BLUE + "                 |    @    |           " + RESET)
        print(BLUE + "                 |  ~~~~~  |           " + RESET)
        print(BLUE + "                 |_________|           " + RESET)

def time():
    hour = (datetime.utcnow() + timedelta(hours=12)).hour
    if hour >= 6 and hour <= 12:
        return "Guten morgen"
    elif hour >= 13 and hour <= 18:
        return "Guten tag"
    elif hour >= 19 and hour <= 24:
        return "Guten abend"
    elif hour >= 1 and hour <= 5:
        return "Guten nacht"

def record_get():
    try:
        with open('answers.json', 'r') as json_file:
            answers = json.load(json_file)
            return answers
    except FileNotFoundError:
        answers = {}
        return answers
    
def record_push(answers):
    with open('answers.json', 'w') as json_file:
        json.dump(answers, json_file)