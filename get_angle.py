# N'a pas été testé
from math import atan, pi, sqrt


goal_droit= [ # coté vert (c1 et c2)
  (0.9, 0.3), # poteaux supérieur, (x,y)
  (0.9,-0.3)  ] # poteaux inférieur, (x,y)
goal_gauche= [
  (-0.9, 0.3),
  (-0.9, -0.3)  ]

terrain_x = [-0.9, 0.9]
terrain_y = [-0.6, 0.6]

def get_alpha(pos_balle:tuple, goal:list):
  """
  Retourne les deux angles alpha (voir les explications) qui serviront pour le calcul de theta.
  Ceux-ci sont calculés en fonction des deux poteaux pour avoir les deux "extrémités" pour être correctement alignées.
  
  Paramètres:
    - pos_balle : tuple - contient les positions x et y de la balle
    - goal: list - contient les coordonnées des poteaux du goal 
  """
  up = (goal[0][0]-pos_balle[0])**2
  down_1 = (pos_balle[1]-goal[0][1])**2
  down_2 = (pos_balle[1]-goal[1][1])**2
  return (atan ( sqrt( up / down_1 ) ), 
        atan ( sqrt( up / down_2 ) ))
  
def get_theta_att(pos_balle:tuple, cote:str):
  """
  Retourne les deux angles theta (voir les explications) pour que l'attaquant puisse cadrer.
  Ceux-ci sont calculés en fonction des deux poteaux pour avoir les deux "extrémités" pour être correctement alignées.
  
  Paramètres:
    - pos_balle : tuple - contient les positions x et y de la balle
    - cote : str - Côté que l'on attaque. d pour droite, g pour gauche 
                    ( par rapport au sens de l'axe des abscisses ) 
  """
  if cote.lower() == "d":
    alpha = get_alpha(pos_balle, goal_droit)
    if pos_balle[1] > 0:
      return (- ( pi/2 - alpha[0]),
             - ( pi/2 - alpha[1]))
    else:
      return (pi/2 - alpha[0],
              pi/2 - alpha[1])
  elif cote.lower() == "g":
    alpha = get_alpha(pos_balle, goal_gauche)
    if pos_balle[1] > 0:
      return (- ( pi/2 + alpha[0]),
              - ( pi/2 + alpha[1]))
    else:
      return (pi/2 + alpha[0],
              pi/2 + alpha[1])
    
def get_theta_def(pos_balle:tuple, cote:str):
    """
  Retourne les deux angles theta (voir les explications) pour que le goal soit aligné avec la balle.
  Ceux-ci sont calculés en fonction des deux poteaux pour avoir les deux "extrémités" pour être correctement alignées.
  
  Paramètres:
    - pos_balle : tuple - contient les positions x et y de la balle
    - cote : str - Côté que l'on attaque. d pour droite, g pour gauche 
                    ( par rapport au sens de l'axe des abscisses ) 
  """
    if cote.lower() == "d":
        alpha = get_alpha(pos_balle, goal_droit)
        if pos_balle[1] > 0:
            return (pi/2 - alpha[0],
                    pi/2 - alpha[1])
        else:
            return (-(pi/2 - alpha[0]),
                    -(pi/2 - alpha[1]))
    elif cote.lower() == "g":
        alpha = get_alpha(pos_balle, goal_gauche)
        if pos_balle[1] > 0:
            return (pi/2 + alpha[0],
                    pi/2 + alpha[1])
        else:
            return (-(pi/2 + alpha[0]),
                    -(pi/2 + alpha[1]))

def get_pos(pos_balle):
    x_balle = pos_balle[0]
    y_balle = pos_balle[1]
    #Cas x- et y-
    if x_balle < 0 and y_balle < 0:
        x = x_balle + 0.06
        y = y_balle - 0.06
    
    #Cas x- et y+
    if x_balle < 0 and y_balle > 0:
        x = x_balle + 0.06
        y = y_balle + 0.06
    
    #cas x+ et y+
    if x_balle > 0 and y_balle > 0:
        x = x_balle - 0.06
        y = y_balle + 0.06
    
    #Cas x+ et y-
    if x_balle > 0 and y_balle < 0:
        x = x_balle - 0.06
        y = y_balle - 0.06
        
    return (x,y)


if __name__=="__main__":
    pass
