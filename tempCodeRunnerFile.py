from datetime import datetime, timedelta
import random

def talk(person, text):
    if person == "human":
        print("\n")
        print(f"           [ {text} ]")
        print("            /")
        print(" ||||||||| /   ")
        print(" | -   - |   ")
        print(" | O   O |   ")
        print("  \  ∆  /    ")
        print("   \_o_/     ")

    elif person == "robot":
        print(f"                            [ {text} ]")
        print("                             /")
        print("                 __________ /   ")
        print("                 |         |   ")
        print("                 |  ^   ^  |   ")
        print("                 |    @    |   ")
        print("                 |  ~~~~~  |   ")
        print("                 |_________|     ")
        


def Hello():
    hour = (datetime.utcnow() + timedelta(hours=12)).hour
    if hour >= 6 and hour <= 12:
        hello = "Good morning"
    elif hour >= 13 and hour <= 18:
        hello = "Good day"
    elif hour >= 19 and hour <= 24:
        hello = "Good evening"
    elif hour >= 1 and hour <= 5:
        hello = "Good night" 

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
    answer = input('your greeting: ')
    talk("human", answer)
    talk("robot", choise)
    
    
Hello()