#!/usr/bin/env python
# coding: utf-8

# In[21]:


import turtle
shelly=turtle.Turtle()
shelly.shape('turtle')
shelly.color('orange')
shelly.shapesize(1,0.5)

def turtle_shapes():
    sides = input("How many sides do you want shelly's shape to have?")
    sides = int(sides)
    if sides == 0:
        circle_size = input("What's the radius you want your circle to have?")
        circle_size = int(circle_size)
        shelly.circle(circle_size)
    if sides >= 3:
        length = input("How long do you want the sides of shelly's shape?")
        sides = int(sides)
        length = int(length)
        angle = 360 / sides
        for i in range (sides):
            shelly.forward(length)
            shelly.right(angle)
    else:
        print("I'm sorry, Shelly can't do that.")

turtle_shapes()


# In[ ]:




