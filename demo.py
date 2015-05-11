#!/usr/bin/python3
from events.Events import Events

events = Events()

recorder = events.recorder()

@recorder.subscribe
def a(parent, text):
    print('a prints: '+text)

@recorder.subscribe('a', 1)
def b(parent, text):
    parent('b prepends: '+text)

#events.subscribe(a, 0)
#events.subscribe(b, 0, 'a')

events.invoke('a', 'hello')

recorder.unsubscribe_all()

events.invoke('a', 'hello')
