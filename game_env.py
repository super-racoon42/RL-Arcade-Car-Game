import random
import copy

class ObstacleGame:
    def __init__(self):
        # Initialisation
        
        self.obstacle_pattern1 = [[0,0,1], [0,1,0], [1,0,0]]
        self.obstacle_pattern2 =  [[0,1,1], [1,1,0], [1,0,1]]
        
        self.obstacle = [
            [0,0,0],
            [0,0,0]
        ]

        self.pos = 1
        
        self.j = [0,1,0]

        self.state = False

        self.vie = 4

        self.game_over = False

        
    def reset(self):
        # Recommence une partie et renvoie le contexte initial de la partie
        self.vie = 4
        self.game_over = False
        self.j = [0,1,0]
        self.pos = 1
        self.obstacle = [
            self.random_pat(),
            [0,0,0] 
        ]

        return self.get_state()
        
    # def step(self, action):

    #     """
    #     Exécute une action et retourne le résultat
    #     action: 0=gauche, 1=rester, 2=droite
    #     """
    #     # 1. Déplacer le joueur selon l'action
    #     if action == 0 and self.pos > 0:  # Gauche
    #         self.pos -= 1
    #     elif action == 2 and self.pos < 2:  # Droite
    #         self.pos += 1
    #     # action == 1 : ne bouge pas
        
    #     # Mettre à jour la représentation du joueur
    #     self.j = [0, 0, 0]
    #     self.j[self.pos] = 1

    #     self.next_line()
    #     # On remplace la première ligne par un pattern aléatoire
    #     self.obstacle[0] = self.random_pat()

    #     if (action == 0 and self.pos == 0) or (action == 2 and self.pos = 2):
    #         return self.get_state(), -10, False
    #     else:
    #         if (self.verif()):
    #             self.vie-=1
    #             if(self.vie == 0):
    #                 return self.get_state(), -10, True 
    #             else:
    #                 return self.get_state(), -1, False 
    #         else: 
    #             return self.get_state(), 1, False

    # Laisse l'agent apprendre qu'il ne faut pas aller dans les murs
    def step(self, action):
        # 1. Vérifier si le mouvement est valide
        mouvement_invalide = False
        
        if action == 0:  # Gauche
            if self.pos > 0:
                self.pos -= 1
            else:
                mouvement_invalide = True  # Essaye d'aller dans le mur gauche
        elif action == 2:  # Droite
            if self.pos < 2:
                self.pos += 1
            else:
                mouvement_invalide = True  # Essaye d'aller dans le mur droit
        # action == 1 : ne bouge pas (toujours valide)
        
        # Mettre à jour la représentation du joueur
        self.j = [0, 0, 0]
        self.j[self.pos] = 1

        # Faire avancer le jeu
        self.next_line()
        self.obstacle[0] = self.random_pat()

        # Calculer la récompense
        if mouvement_invalide:
            return self.get_state(), -10, False  # Pénalité pour mur
        
        if self.verif():  # Collision avec voiture
            self.vie -= 1
            if self.vie == 0:
                return self.get_state(), -10, True  # Game over
            else:
                return self.get_state(), -5, False  # Perd une vie
        else:
            return self.get_state(), 1, False  # Survit = récompense positive



    def get_state(self):
        # Retourne le contexte actuel
        obstacle = self.obstacle [0]
        return str(self.pos) + str(obstacle[0]) + str(obstacle[1]) + str(obstacle[2])

    def random_pat(self):
        nb_car = 1 if random.random() >= 0.5 else 2
        return copy.copy(self.obstacle_pattern1[random.randint(0, 2)]) if nb_car == 1 else copy.copy(self.obstacle_pattern2[random.randint(0, 2)])

    def next_line(self):
        obstacle = self.obstacle
        for i in range(3):
            obstacle[1][i] = obstacle[0][i]

    def verif(self):
        return self.obstacle[1][self.pos] == 1


a = ObstacleGame()
a.reset()
print(a.get_state())

        