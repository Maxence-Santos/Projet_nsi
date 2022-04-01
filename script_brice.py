import rsk
from os import system

def print_the_ball(client, dt):
    print(client.ball)

with rsk.Client(host='172.19.66.163', key='') as client:
    robotBleu1 = client. robots['blue'][1]
    robotBleu2 = client. robots['blue'][2]
    robots = [robotBleu1, robotBleu2]
    while True:
        for i, robot in enumerate(robots):
            pos = robot.position
            print(f"Robot {i} : x={pos[0]}   y={pos[1]}")
        ball_pos = client.ball
        print(client.robots['green'][1].pose)
        client.on_update = print_the_ball
