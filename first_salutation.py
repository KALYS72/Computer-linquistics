from datetime import datetime, timedelta
import random



RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
YELLOW = '\033[33m'
RESET = "\033[0;0m"
def talk(person, text):
    if person == "human":
        print("\n")
        print(RED + f"            {YELLOW + text + RESET}")
        print(RED + "            /         " + RESET)
        print(RED + " ||||||||| /          " + RESET)
        print(RED + " | -   - |            " + RESET)
        print(RED + " | O   O |            " + RESET)
        print(RED + "  \  ∆  /             " + RESET)
        print(RED + "   \_o_/              " + RESET)

    elif person == "robot":
        print(BLUE + f"                             {YELLOW + text + RESET}")
        print(BLUE + "                             /         " + RESET)
        print(BLUE + "                 __________ /          " + RESET)
        print(BLUE + "                 |         |           " + RESET)
        print(BLUE + "                 |  ^   ^  |           " + RESET)
        print(BLUE + "                 |    @    |           " + RESET)
        print(BLUE + "                 |  ~~~~~  |           " + RESET)
        print(BLUE + "                 |_________|           " + RESET)
        


def Hello():

    hour = (datetime.utcnow() + timedelta(hours=12)).hour
    if hour >= 6 and hour <= 12:
        hello = "Guten morgen"
    elif hour >= 13 and hour <= 18:
        hello = "Guten tag"
    elif hour >= 19 and hour <= 24:
        hello = "Guten abend"
    elif hour >= 1 and hour <= 5:
        hello = "Guten nacht" 

    greetings = [
    f"{hello}! How are you doing today? Anything exciting happening?",
    f"{hello}! How's the weather treating you?",
    f"{hello}! How's life treating you? Have any interesting plans?",
    f"{hello}! What's the latest and greatest in your world?",
    f"{hello}! How's your day going? Find any good news?",
    f"{hello}! How's everything on your end? Any fun stories to share?",
    f"{hello}! How's the day treating you so far? Hear any interesting gossip?",
    f"{hello}! How's your mood today? Anything making you smile?",
    f"{hello}! What's the vibe like in your corner of the world?",
    f"{hello}! How's your energy today? Anything giving you a boost?"
    ]
    random_greeting = random.randint(1, len(greetings))
    choise = greetings[random_greeting-1]
    talk("human", input(YELLOW + 'your greeting: '+ RESET))
    talk("robot", YELLOW + choise + RESET)
    print('\n')
    talk("human", YELLOW + input('your answer: ') + RESET)
    
    
Hello()