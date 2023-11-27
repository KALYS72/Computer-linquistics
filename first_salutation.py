from record import time, talk
import random

def Hello():
    greetings = [
    f"{time()}! How are you doing today? Anything exciting happening?",
    f"{time()}! How's the weather treating you?",
    f"{time()}! How's life treating you? Have any interesting plans?",
    f"{time()}! What's the latest and greatest in your world?",
    f"{time()}! How's your day going? Find any good news?",
    f"{time()}! How's everything on your end? Any fun stories to share?",
    f"{time()}! How's the day treating you so far? Hear any interesting gossip?",
    f"{time()}! How's your mood today? Anything making you smile?",
    f"{time()}! What's the vibe like in your corner of the world?",
    f"{time()}! How's your energy today? Anything giving you a boost?"
    ]
    random_greeting = random.randint(1, len(greetings))
    choise = greetings[random_greeting-1]
    talk("human", input('your greeting: '))
    talk("robot", choise)
    print('\n')
    talk("human", input('your answer: '))
    
    
Hello()