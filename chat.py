# -*- coding:utf-8 -*-

import readline
from simsimi import SimSimiChat


def complete(text, state):
    for cmd in ['quit', 'tech']:
        if not cmd.startswith(text):
            return
        if not state:
            return cmd
        else:
            state -= 1

readline.set_completer(complete)
readline.parse_and_bind("tab: complete")
readline.parse_and_bind('set editing-mode emacs')
robot = SimSimiChat()

while True:
    message = raw_input('me: ')
    if message == "quit":
        break
    if message == 'tech':
        req = raw_input("req> ")
        resp = raw_input("resp> ")
        print robot.tech(req, resp)
    else:
        print "simsimi: ", robot.chat(message)
