import random

def talk(person, text):
    RED   = "\033[1;31m"  
    BLUE  = "\033[1;34m"
    YELLOW = '\033[33m'
    RESET = "\033[0;0m"
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

# source of responces and 
good = ["good", "hey", "hi", "nice", "cool", "okay", "hello", "greetings", "positive", "vibrant", "excellent", 
"awesome", "fantastic", "superb", "amazing", "great", "wonderful", "pleased", "delighted", "friendly"]
bad = ["meh", "bad", "hard", "tough", "blah", "ugh", "down", "nah", "not good", "worse", "off", "struggling", 
"nope", "setbacks", "difficult", "challenging", "frustrating", "disappointing", "unpleasant", "discouraging"]
normal = ["okay", "normal", "regular", "usual", "fine", "meh", "typical", "standard", "same old", "ordinary", 
"routine", "plain", "usual", "same", "routine", "consistent", "steady", "average", "typical", "common"]
upset = ["upset", "nerves", "irritated", "annoyed", "stressed", "tense", "frustrated", "challenged", "agitated", 
"distressed", "displeased", "worried", "angry", "unhappy", "disheartened", "dejected", "disgruntled", "discontent", 
"disturbed", "perturbed"]


good_responses = [
    "I'm here for you, sending positive vibes your way. Let's focus on the good moments today.",
    "Hey! I'm here to brighten your day. Share with me the positive things happening around you.",
    "Hello! We can navigate through any challenges together. What's going well for you?",
]

bad_responses = [
    "Hey, I'm here to support you during this rough patch. Let's work through it together.",
    "Hi, I understand it's been a challenging day. You're not alone; I'm here for you.",
    "Dealing with unexpected hurdles is tough, but I'm here to offer support and encouragement.",
]

normal_responses = [
    "Just dropping by to say hello! If there's anything on your mind, feel free to share. I'm here for you.",
    "Hey! Today is quite ordinary. How are you feeling? Anything you want to talk about?",
    "Hello! If there's anything you need or want to discuss, I'm here to listen.",
]

upset_responses = [
    "Hey, thanks for sharing. I'm here for you, and we can work through these emotions together.",
    "I appreciate you opening up. Let's take it one step at a time, and I'm here to support you.",
    "Hi, I'm sorry to hear that. Your feelings are valid, and I'm here to lend a listening ear.",
]

neutral = [
    "I might need a bit more clarity. Could you please expand on that point, and we can work through it together?",
    "I'm not entirely sure I understood. Can you provide more details, so we can go through it step by step?",
    "It seems I may have missed something. Could you share more about what you meant? I'm here to help.",
    "I want to make sure I understand correctly. Could you clarify or provide more context? We can tackle it together."
]


# amount of words
def has_only_one_word(s):
    if s.count(" ") == 0:
        return True
    return False

# identifying the biggest amount of characters
def robot_responce(mood):
    most = ""
    num = 0
    for k,v in mood.items():
        if v > num:
            num = v
            most = k
    if most == "good":
        subject = good_responses
    elif most == "bad":
        subject = bad_responses
    elif most == "normal":
        subject = normal_responses
    elif most == "upset":
        subject = upset_responses
    else:
        subject = neutral
    response = random.randint(1, len(subject))
    talk("robot", subject[response-1])

answers = []
mood = {
    "good":0,
    "bad":0,
    "normal":0,
    "upset":0,
    "not_id":0
}
talk("robot", "Hello my friend!")
a = 1 # loop part
while a <= 3:
    print('\n')
    me = input("Your answer to my greeting: ")
    talk("human", me)
    answers.append(me)
    me = me.lower().replace('!', '')
    if has_only_one_word(me):
        if me in good:
            mood["good"] += 1
        elif me in bad:
            mood["bad"] += 1
        elif me in normal:
            mood["normal"] += 1
        elif me in upset:
            mood["upset"] += 1
        else:
            mood["not_id"] += 1
    else:
        me = me.split(' ')
        for word in me:
            if word in good:
                mood["good"] += 1
            elif word in bad:
                mood["bad"] += 1
            elif word in normal:
                mood["normal"] += 1
            elif word in upset:
                mood["upset"] += 1
            else:
                mood["not_id"] += 1
    robot_responce(mood)
    a += 1 # to get the loop until 3 times

with open('answers.py', 'a') as file:
    file.write(f"{answers}\n")




