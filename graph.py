import blessings, sys, time
import readline
from math import *
t = blessings.Terminal()

def slowoperation(x):
    time.sleep(.2)
    return x

def setpt(x, y):
    if t.width > x + t.width // 2 >= 0 and t.height > t.height // 2 - y >= 0:
        with t.location(x + t.width // 2, t.height // 2 - y):
            if x == y == 0:
                t.stream.write(t.on_white("+"))
            elif x == 0:
                t.stream.write(t.on_white("|"))
            elif y == 0:
                t.stream.write(t.on_white("-"))
            else:
                t.stream.write(t.on_white(" "))

def linebtwn(newpt, oldpt):
    setpt(*newpt)
    return
    ybase = oldpt[1]
    ystop = newpt[1]
    dy = ystop - ybase
    ymid = ybase + dy//2
    for y in range(ybase, ymid):
        setpt(oldpt[0], y)
    for y in range(ymid, ystop):
        setpt(newpt[0], y)

with t.fullscreen():
    tx = "x"
    while tx != "":
        with t.location(0, t.height):
            tx = input("y=")
            last = None

            t.stream.write('\x1b[2J')
            for x in range(t.width):
                with t.location(x, t.height // 2):
                    t.stream.write("-")
            for y in range(t.height):
                with t.location(t.width // 2, y):
                    t.stream.write("|")

            with t.location(t.width // 2, t.height // 2):
                t.stream.write('+')

            for xf in range(10 *(-t.width // 2), 10*(t.width // 2 + 1)): 
                x = xf / 10
                try:
                    xh = int(eval(tx))
                except: # div by zero, domain error, syntax error, whatever
                    continue

                if last:
                    linebtwn((xf // 10, xh), last)
#                   print('lbt\'n')
                else:
                    setpt(xf // 10, xh)
#                   print('setpt\'n')
                t.stream.flush()
                last = xf // 10, xh

