#!/usr/bin/env python

import json

open('puffpuff.json').read()
passwords = json.loads(open('puffpuff.json').read())
passwords = passwords["passwords"]

def writeout():
    global y
    with open('puffpuff.json', 'w') as outfile:
                json.dump({'passwords':y}, outfile, indent=4)

def add():
    print('Type the password that you want to add.')
    global y
    y = input()
    writeout()

print("Do you want to 'add' a password, 'ch'eck your passwords or 'cre'ate a new one?")
x = input()

if x == 'add':
    add()
