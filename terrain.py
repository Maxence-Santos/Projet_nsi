import rsk
from get_angle import *

def stay(robot) :
  x = robot.position[0]
  y = robot.position[1]
  if y >= 0.5 :
    robot.goto(x, 0.5)
  if y <= -0.5 :
    robot.goto(x, 0.5)
  if x >= 0.6 :
    robot.goto(0.6, y)
  if x <= -0.6 :
    robot.goto(-0.6, y)