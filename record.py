from functions import talk, time, record_get, record_push

answers = record_get()
me = input("Say something: ")
talk("human", me)
me.lower()
if me in answers:
    talk("robot", answers[me])
    hi = input("Your response: ")
    answers[me] = hi
else:
    talk("robot", time())
    answers[me] = me

record_push(answers)