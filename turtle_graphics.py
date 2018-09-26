# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 07:33:53 2018

@author: Paddy3118
"""

import turtle as t


# ## Turtle initialisation
# 
# I decided to always reset the turtles heading between writing sections of the graphic.
# 
# I couldn't find a turtle function to move delta x, delta y, from a current position so created one in the ``moveby`` function.

# In[23]:


def init_turtle_graphics():
    global t
    
    x, x2y = 70, 3/4 *9.7 / 8.9
    y = x* x2y
    t.reset()
    t.screensize(400, 300)
    t.setworldcoordinates(-x, -y, x, y)
    t.setposition(0, 0)
    t.setheading(0)
    t.width(4) # pixels
    t.delay(1)

def moveby(delta_x, delta_y):
    global t
    
    heading = t.heading()
    t.setheading(0)
    t.forward(delta_x)
    t.left(90)
    t.forward(delta_y)
    t.setheading(heading) # Preserve heading


# In[24]:


def square(side=1, colour="yellow"):
    global t
    
    t.pendown()
    t.fillcolor(colour)
    t.begin_fill()
    for _ in range(4):
        t.forward(side)
        t.left(90)
    t.end_fill()
    t.penup()


# In[25]:



def _chev(x, y, start):
    "Draw a single chevron. Initial heading going into the function is important"
    global t

    t.begin_fill()
    for s in (2*x - y, y - x, x, x, y - x, 2*x - y):
        t.fd(s)
        t.right(90)
    t.end_fill()
    t.penup()
    t.goto(start)
    t.setheading(0)


# In[26]:


def bl_chevron(x=5, y=7, colour="orange"):
    "Bottom left chevron"
    global t
    
    start = t.position()
    t.pendown()
    t.fillcolor(colour)
    _chev(x, y, start)

def ur_chevron(x=5, y=7, colour="orange"):
    "Upper right chevron"
    global t
    
    start = t.position()
    moveby(2*x - y, 2*x - y)
    t.pendown()
    t.fillcolor(colour)
    t.left(180)
    _chev(x, y, start)

def br_chevron(x=5, y=7, colour="orange"):
    "Bottom right chevron"
    global t
    
    start = t.position()
    moveby(2*x - y, 0)
    t.pendown()
    t.fillcolor(colour)
    t.left(90)
    _chev(x, y, start)

def ul_chevron(x=5, y=7, colour="orange"):
    "Upper left chevron"
    global t
    
    start = t.position()
    moveby(0, 2*x - y)
    t.pendown()
    t.fillcolor(colour)
    t.left(-90)
    _chev(x, y, start)



# In[27]:



def ur_square(x, y, colour="red"):
    global t
    
    start = t.position()
    moveby(2*x - y, 2*x - y)
    square(y - x, colour)
    t.goto(start)

def bl_square(x, y, colour="red"):
    global t
    
    start = t.position()
    moveby(-(y - x), -(y - x))
    square(y - x, colour)
    t.goto(start)

def ul_square(x, y, colour="red"):
    global t
    
    start = t.position()
    moveby(-(y - x), 2*x - y)
    square(y - x, colour)
    t.goto(start)

def br_square(x, y, colour="red"):
    global t
    
    start = t.position()
    moveby(2*x - y, -(y - x))
    square(y - x, colour)
    t.goto(start)


# In[28]:


init_turtle_graphics()
colour_names = "peru,lime green,dodger blue,slate blue".split(',')
colour_names += colour_names[:1] # Controls the level of nesting
x, y = 1, 1# Smallest nearest miss
# Pattern of drawing alternates between levels so will swap the drawing functions
chev_squares = [(bl_chevron, ur_chevron, ul_square, br_square),
                (ul_chevron, br_chevron, bl_square, ur_square)]
square(x, "yellow")
for colour in colour_names:
    x, y = x + y, 2*x + y # Next bigger tenenbaum squares: 2*x**2 == y**2 +/- 1
    chev1, chev2, sqr1, sqr2 = chev_squares[0]
    chev_squares.insert(0, chev_squares.pop(-1))
    chev1(x, y, colour)
    chev2(x, y, colour)
    sqr1(x, y)
    sqr2(x, y)
    moveby(-(y - x), -(y - x))
