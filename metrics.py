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

def get_pos_cadre(pos_balle:tuple, cote_attaque:str):
  """Permet de pouvoir récupérer la position que doit avoir le joueur, en se décalant un peu de la balle pour ne pas lui rouler dessus 

  Args:
      pos_balle:tuple: Contient client.ball, la position de la balle

  Returns:
      (x,y)  tuple: Position vers laquelle le joueur doit aller
  """
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

def get_angle_att(pos_balle:tuple, cote_attaque:str):
  """Retourne l'angle que doit avoir l'attaquant

  Args:
      pos_balle (tuple)
      cote_attaque (str): d ou g

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

def get_distance_balle(pos_ball:tuple,joueur):
  """Est-ce que je dois vraiment faire une doc?"""
  pos_joueur = joueur.pose
  return sqrt((pos_ball[0] - pos_joueur[0])**2 + 
        (pos_ball[1] - pos_joueur[1])**2)


if __name__=="__main__":
    pass
