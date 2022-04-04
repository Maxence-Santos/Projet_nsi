import rsk
import get_angle
from math import pi
with rsk.Client(host='172.19.66.163', key='') as client:
    robotVert1 = client.robots['green'][1]
    robotVert2 = client.robots['green'][2]
    robotBleu1 = client.robots['blue'][1]
    robotBleu2 = client.robots['blue'][2]
    arrived = False
    while not arrived:
        robot_1_arrived = robotVert1.goto((0.4, 0, pi), wait=False)
        robot_2_arrived = robotVert2.goto((-0.4, 0, 0), wait=False)
        arrived = robot_1_arrived and robot_2_arrived
