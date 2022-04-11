import rsk
from math import pi, radians
import random

with rsk.Client(host='172.19.66.163', key='') as client:
    robotVert1 = client.robots['green'][1]
    robotVert2 = client.robots['green'][2]
    robotBleu1 = client.robots['blue'][1]
    robotBleu2 = client.robots['blue'][2]

    def taper_dans_les_mains(r1, r2):
        a = False
        while not a :
            a1 = r1.goto((-0.5, 0.1, (3*pi/2)), wait=False)
            a2 = r2.goto((-0.5, -0.1, (pi/2)), wait=False)
            a = a1 and a2
        r1.kick()
        r2.kick()
    
    def spirale_groupe(r1, r2):
        a = False
        while not a :
            a1 = r1.goto((-0.5, 0.3, 0), wait=False)
            a2 = r2.goto((-0.5, -0.3, 0), wait=False)
            a = a1 and a2
        a = False
        while not a :
            a1 = r1.goto((-0.5, 0.3, radians(180)), wait=False)
            a2 = r2.goto((-0.5, -0.3, radians(180)), wait=False)
            a = a1 and a2
        a = False
        while not a :
            a1 = r1.goto((-0.5, 0.3, 0), wait=False)
            a2 = r2.goto((-0.5, -0.3, 0), wait=False)
            a = a1 and a2
    
    def tour_centre(r1, r2):
        pass
    
    taper_dans_les_mains(robotBleu1, robotBleu2)
    spirale_groupe(robotBleu1, robotBleu2)
    tour_centre(robotBleu1, robotBleu2)