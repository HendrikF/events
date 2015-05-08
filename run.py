#!/usr/bin/python3
from Events import Events

events = Events()

def a(parent, text):
    print('a prints: '+text)

def b(parent, text):
    parent('b prepends: '+text)

events.subscribe(a, 0)
events.subscribe(b, 0, 'a')

events.invoke('a', 'hello')
