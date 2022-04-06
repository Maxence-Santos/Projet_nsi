from math import atan, pi

goal_droit= [ # coté vert (c1 et c2)
  (0.9, 0.3), # poteaux supérieur, (x,y)
  (0.9,-0.3)  ] # poteaux inférieur, (x,y)

goal_gauche= [
  (-0.9, 0.3),
  (-0.9, -0.3)  ]

def get_alpha(pos_balle:tuple, goal:list):
  """
  Retourne les deux angles alpha (voir les explications) qui serviront pour le calcul de theta.
  Ceux-ci sont calculés en fonction des deux poteaux pour avoir les deux "extrémités" pour être correctement alignées.
  
  Paramètres:
    - pos_balle : tuple - contient les positions x et y de la balle
    - goal: list - contient les coordonnées des poteaux du goal 
  """
  up_1 = pos_balle[0]-goal[0][1]
  up_1 = pos_balle[0]-goal[1][1]
  down = pos_balle[0]-goal[0][0]
  return (atan ( up_1 / down ), 
        atan ( up_1 / down ) )

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
      return ( - alpha[0],
              - alpha[1])
    else:
      return (alpha[0],
              alpha[1])
  elif cote.lower() == "g":
    alpha = get_alpha(pos_balle, goal_gauche)
    if pos_balle[1] > 0:
      return ( alpha[0] - pi,
              alpha[1] - pi)
    else:
      return (pi - alpha[0],
              pi - alpha[1])


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
            return (pi - alpha[0],
                    pi - alpha[1])
        else:
            return (alpha[0] - pi,
                    alpha[1] - pi)
    elif cote.lower() == "g":
        alpha = get_alpha(pos_balle, goal_gauche)
        if pos_balle[1] > 0:
            return (alpha[0],
                    alpha[1])
        else:
            return (- alpha[0],
                    - alpha[1])

def get_angle_att(pos_balle:tuple, cote_attaque:str, robots_adverses:list):
  """Retourne l'angle que doit avoir l'attaquant

  Args:
      pos_balle (tuple)
      cote_attaque (str): d ou g
      robots_adverses (list): liste des robots adverses

  Returns:
      float
  """
  return sum(list(get_theta_att(pos_balle, cote_attaque))) / 2

def get_angle_def(pos_balle:tuple, cote_attaque:str):
  """Retourne l'angle que doit avoir le  goal

  Args:
      pos_balle (tuple)
      cote_attaque (str): d ou g

  Returns:
      float
  """
  return sum(list(get_theta_def(pos_balle, cote_attaque))) / 2
