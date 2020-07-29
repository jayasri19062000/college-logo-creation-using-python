# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:56:53 2020

@author: JAYASRI
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:01:40 2020
cd

@author: JAYASRI
"""

import turtle
import random
from alpha import alphabet
message=input("enter ur name:")
n=len(message)
wn=turtle.Screen()
wn.title("snist")
s=turtle.Turtle()
s.speed(0)
s.color("blue")
s.up()
s.goto(-580,-250)
s.down()
s.left(90)
s.begin_fill()
s.forward(480)
s.right(90)
x=310+80*(n+1)
s.forward(x)
s.right(90)
s.forward(480)
s.right(90)
s.forward(x)
s.end_fill()
r=turtle.Turtle()
r.speed(0)
r.color("white")
r.up()
r.goto(-560,-180)
r.down()
r.left(90)
r.begin_fill()
r.forward(390)
r.right(90)
r.forward(260)
r.right(90)
r.forward(390)
r.right(90)
r.forward(260)
r.end_fill()
r=turtle.Turtle()
r.speed(0)
r.color("white")
r.up()
r.goto(-560,-240)
r.down()
r.left(90)
r.begin_fill()
r.forward(50)
r.right(90)
r.forward(x-50)
r.right(90)
r.forward(50)
r.right(90)
r.forward(x-50)
r.end_fill()
skk=turtle.Turtle()
skk.speed(0)
skk.color("blue")
skk.up()
skk.goto(-480,-180)
skk.down()
skk.begin_fill()
skk.forward(50)
skk.left(90)
skk.forward(100)
skk.left(90)
skk.forward(50)
skk.left(90)
skk.forward(100)
skk.left(90)
skk.end_fill()
skk.up()
skk.goto(-510,-80)
skk.down()
skk.begin_fill()
for _ in range(2):
    skk.fd(110)
    skk.circle(20,90)
    skk.fd(10)
    skk.circle(20,90)
skk.end_fill()
skk.up()
skk.goto(-540,-30)
skk.down()
skk.begin_fill()
skk.forward(170)
skk.left(90)
skk.forward(50)
skk.left(90)
skk.forward(170)
skk.left(90)
skk.forward(50)
skk.left(90)
skk.end_fill()
myPen = turtle.Turtle()
myPen.hideturtle()
myPen.pensize(10)

def displayMessage(message,fontSize,x,y):
  myPen.color("white")
  message=message.upper()
  
  for character in message:
    if character in alphabet:
      letter=alphabet[character]
      myPen.penup()
      for dot in letter:
        myPen.goto(x + dot[0]*fontSize, y + dot[1]*fontSize)
        myPen.pendown()
        
      x += fontSize
      
    if character == " ":
      x += fontSize
    x += characterSpacing
myPen1 = turtle.Turtle()
myPen1.hideturtle()
myPen1.pensize(5)
def displayMessagee(message,fontSize,x,y):
  myPen1.color("blue")
  message=message.upper()
  
  for character in message:
    if character in alphabet:
      letter=alphabet[character]
      myPen1.penup()
      for dot in letter:
        myPen1.goto(x + dot[0]*fontSize, y + dot[1]*fontSize)
        myPen1.pendown()
        
      x += fontSize
      
    if character == " ":
      x += fontSize
    x += characterSpacing 

#Main Program Starts Here
fontSize = int(input("enter input size:"))
characterSpacing = 5
displayMessage(message,fontSize,-260,-30)
fontSize = 15
characterSpacing = 1
displayMessagee("sreenidhi institute of science and technology",fontSize,-550,-235)
j=turtle.Turtle()
j.color("black")
j.pensize(5)
j.speed(0)
j.up()
j.goto(-650,-30)
j.down()
j.circle(30)
j.right(90)
j.forward(100)
j.right(30)
j.forward(60)
j.backward(60)
j.left(60)
j.forward(60)
j.backward(60)
j.right(30)
j.backward(50)
j.right(30)
j.forward(60)
j.backward(60)
j.left(60)
j.forward(60)
j.left(120)
j.color("brown")
j.forward(230)
j.color("white")
colors=["red","yellow"]
k=0
for i in range(2):
 k=k%2
 skk.color(colors[k])
 k=k+1
 k=k%2
 skk.up()
 skk.goto(-470,20)
 skk.down()
 skk.begin_fill()
 skk.left(90)
 skk.circle(-70,90)
 skk.left(20)
 skk.circle(70,90)
 skk.right(153)
 skk.circle(-90,145)
 skk.left(30)
 skk.circle(10,50)
 skk.end_fill()
 skk.left(90)
 skk.color(colors[k])
 skk.up()
 skk.goto(-472,20)
 skk.down()
 skk.begin_fill()
 skk.left(108)
 skk.circle(-72,90)
 skk.left(20)
 skk.circle(70,100)
 skk.left(150)
 skk.circle(-70,90)
 skk.right(1)
 skk.circle(70,110)
 skk.end_fill()
 skk.color("white",colors[k])
 skk.begin_fill()
 skk.left(178)

 skk.circle(-70,110)
 skk.right(0.25)
 skk.circle(60,120)
 skk.left(143)
 skk.circle(-70,90)
 skk.right(1)
 skk.circle(60,110)
 skk.end_fill()
 skk.left(88)
turtle.done()

