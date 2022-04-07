import rsk
from metrics import *
from math import pi

def rester_att(robot) :
  while True :
    x = robot.position[0]
    y = robot.position[1]
    o = robot.orientation
    if y > 0.5 :
      r_a = robot.goto((x, 0.5, o), wait=False)
    elif y < -0.5 :
      r_a = robot.goto((x, -0.5, o), wait=False)
    elif x > 0.5 :
      r_a = robot.goto((0.5, y, o), wait=False)
    elif x < -0.5 :
      r_a = robot.goto((-0.5, y, o), wait=False)
