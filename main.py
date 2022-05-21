import rsk
import Goal
from attaque import attaque
from os import system
from threading import Thread

SIDE = "g"

with rsk.Client(host='172.19.66.163', key='') as client:
    robotVert1 = client.robots['green'][1]
    robotVert2 = client.robots['green'][2]
    robotBleu1 = client.robots['blue'][1]
    robotBleu2 = client.robots['blue'][2]

    

    while client.ball is None:
        print("Waiting to detect the ball...")
        system("cls") # ou clear
    pos_balle = client.ball


    thread_goal = Thread(target=Goal.goal, args=(robotVert2,SIDE))
    thread_attaque = Thread(target=attaque, args=(SIDE, robotVert1))


    threads = []
    for t in [thread_goal, thread_attaque]:
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    

    """
    while True:
        Defense_p.pos_def(pos_ball,robotBleu1.pose,robotVert1,SIDE) 
        #Goal.goal(robotVert2,SIDE)"""