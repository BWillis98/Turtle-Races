#!/bin/python3

from turtle import *
from random import randint

NUMBER_OF_LINES = 16
SPACE_BETWEEN_NUMBER_AND_LINE = 10
LENGTH_OF_LINES = 240
SPACE_BETWEEN_LINES = 20
STARTING_X = -140
STARTING_Y = 140
TURTLE_SPEED_MIN = -1
TURTLE_SPEED_MAX = 10
VICTORY_GAP = 20
Y_VICTORY_POS = STARTING_Y - SPACE_BETWEEN_NUMBER_AND_LINE - LENGTH_OF_LINES - VICTORY_GAP

speed(0)
penup()
goto(STARTING_X, STARTING_Y)

for step in range(NUMBER_OF_LINES):
  write(step, align='center')
  right(90)
  forward(SPACE_BETWEEN_NUMBER_AND_LINE)
  pendown()
  forward(LENGTH_OF_LINES)
  penup()
  backward(SPACE_BETWEEN_NUMBER_AND_LINE + LENGTH_OF_LINES)
  left(90)
  forward(SPACE_BETWEEN_LINES)

turtle_array = [];

def create_turtle(color, y_value):
  temp = Turtle()
  temp.color(color)
  temp.shape('turtle')
  temp.penup()
  temp.goto(STARTING_X - 20, y_value)
  temp.pendown()
  turtle_array.append(temp)
  return temp
  
ada = create_turtle('red', 100)
bob = create_turtle('blue', 70)
tim = create_turtle('yellow', 40)
jay = create_turtle('violet', 10)
dad = create_turtle('orange', -20)
mom = create_turtle('purple', -50)
fag = create_turtle('black', -80)

# NUMBER_OF_LINES - 1 is the logical number of lines
finish = ((NUMBER_OF_LINES - 1) * SPACE_BETWEEN_LINES) + STARTING_X;

while (True):
  for turt in turtle_array:
    turt.forward(randint(TURTLE_SPEED_MIN, TURTLE_SPEED_MAX))
  
  winning_turtle = None;
  
  for turt in turtle_array:
    if (turt.xcor() >= finish and winning_turtle is None):
      winning_turtle = turt
    elif (turt.xcor() >= finish and winning_turtle is not None):
      if (turt.xcor() >= winning_turtle.xcor()):
        winning_turtle = turt
  
  if (winning_turtle is not None):
    winning_turtle.penup()
    winning_turtle.goto(0, Y_VICTORY_POS)
    print("The winner of the race is " + winning_turtle.pencolor() + "!")
    break
	
input()