import random
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

hour = (datetime.utcnow() + timedelta(hours=12)).hour
if hour >= 6 and hour <= 12:
    hello = "Guten morgen"
elif hour >= 13 and hour <= 18:
    hello = "Guten tag"
elif hour >= 19 and hour <= 24:
    hello = "Guten abend"
elif hour >= 1 and hour <= 5:
    hello = "Guten nacht"


good = [
    "Feeling good",
    "Having a nice day",
    "Feeling happy",
    "Today is great",
    "Hi! Feeling awesome",
    "Feeling fantastic",
    "Everything's wonderful",
    "Great mood",
    "Absolutely amazing",
    "Hello, superb feeling",
    "Feeling incredible",
    "Terrific day",
    "Superb",
    "Excellent mood",
    "Awesome",
    "Marvelous",
    "Brilliant",
    "Splendid",
    "Cheerful and positive",
    "Joyful vibes",
]

bad = [
    "Not so good",
    "Tough day",
    "Feeling down",
    "Struggling a bit",
    "Not great today",
    "Challenging times",
    "Setbacks today",
    "Bit frustrating",
    "A bit harsh",
    "Feeling discouraged",
    "Facing difficulties",
    "Unpleasant day",
    "Discouraging moments",
    "Feeling grim",
    "Harsh reality",
    "Disheartening",
    "Uncomfortable",
    "Meh",
    "Blah",
]

normal = [
    "Just a day",
    "Same old",
    "Usual stuff",
    "It's okay",
    "Hey, normal day",
    "Routine stuff",
    "Typical day",
    "Steady as usual",
    "Balanced day",
    "Maintaining routine",
    "Common day",
    "Consistent",
    "Unchanged",
    "So-so",
    "Average day",
    "Ordinary routine",
    "Nothing special",
    "Moderate day",
    "Fair enough",
    "Acceptable",
] 

positive_responses = [
    "Glad to hear about your positive day",
    "That's fantastic news, thanks for sharing",
    "Awesome! Your happiness is contagious",
    "Great to know you're feeling good",
    "Happy for you and your positive vibes",
    "Excellent! Keep that positivity going",
    "Fantastic! What a wonderful day for you",
    "Wonderful news! Your positivity is uplifting",
    "Terrific! Your good mood brightened my day",
    "Brilliant! Wishing you more moments like this",
    "Superb! Your positivity is truly inspiring",
    "Incredible! Your good mood is infectious",
    "Fantastic news! Thanks for sharing your joy",
    "Amazing! Your positive energy is palpable",
    "Marvelous! Keep embracing the good vibes",
    "Impressive! Your positivity is shining through",
    "Splendid! Your happiness is well-deserved",
    "Cheering for you and your continued joy",
    "Keep it up! Your positive outlook is wonderful",
    "Bravo! Your good day is well-celebrated"
]

negative_responses = [
    "I'm sorry to hear that you're not feeling great",
    "That sounds tough, but you're not alone",
    "Hang in there. Tough times don't last forever",
    "Things will get better, keep your head up",
    "Sending positive vibes your way",
    "Sorry to hear that you're facing challenges",
    "Stay strong. You've overcome hurdles before",
    "Wishing you strength during difficult times",
    "Tomorrow is a new day with new possibilities",
    "Here for you, offering support and empathy",
    "Take it one step at a time, progress is progress",
    "Sending support and positive thoughts your way",
    "You're not alone in facing life's difficulties",
    "I hope things improve for you soon",
    "Keep your head up, brighter days are ahead",
    "It'll pass. Remember, you're resilient",
    "Sending love and strength during tough times",
    "Stay positive, you've got the strength within",
    "You've got this. Lean on your support system",
    "I'm here if you need to talk or vent"
]

neutral_responses = [
    "Got it. Your update is noted",
    "Thanks for sharing your thoughts",
    "Noted. Anything else on your mind?",
    "Alright. Let me know if you need anything",
    "Understood. Feel free to share more",
    "Cool. Anything specific you'd like to discuss?",
    "Okay. If there's anything you'd like to talk about, I'm here",
    "Fair enough. Your input is appreciated",
    "No worries. Is there anything you'd like to add?",
    "Sounds good. Let me know if you have more to share",
    "Gotcha. If there's anything on your mind, I'm here",
    "I see. Anything else you'd like to mention?",
    "Sure thing. Is there anything specific on your mind?",
    "Fine by me. Is there a particular topic you're interested in?",
    "Alright then. Feel free to steer the conversation",
    "Roger that. If there's anything pressing, let me know",
    "All good. Is there something specific you'd like to discuss?",
    "Sounds like a plan. Any particular direction you'd like to go?",
    "Sure, why not. Is there a topic you'd like to explore?",
    "Okay. If you have any questions or thoughts, feel free to share"
]





def robot_responce(mood):
    response = random.randint(1, len(mood))
    talk("robot", mood[response-1])
    return mood[response-1]

answers = []
talk("robot", f"{hello} my friend!")
a = 1
mood = ""
while a <= 3:
    print('\n')
    me = input("Your answer to my greeting: ")
    talk("human", me)
    me = me.lower().replace('!', '')
    if mood == "":
        if me in good:
            mood = positive_responses
        elif me in bad:
            mood = negative_responses
        elif me in normal:
            mood = neutral_responses
        else:
            mood = positive_responses
        answers.append({me:robot_responce(mood)})
    a += 1

with open('answers.py', 'a') as file:
    file.write(f"{answers}\n")




