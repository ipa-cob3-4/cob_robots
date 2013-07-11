import time
def action_print():

    print "hello there"

interval = 5
next_run = 0

while True:

    while next_run > time.time():
        pass

    next_run = time.time() + interval

    action_print()
