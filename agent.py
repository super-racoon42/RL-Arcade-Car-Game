import random
import json
from collections import defaultdict

class QLearningAgent:
    def __init__(self, num_actions, learning_rate=0.1, 
                 discount_factor=0.95, epsilon=1.0, 
                 epsilon_decay=0.995, epsilon_min=0.01):
        """
        num_actions : Nombre d'actions possibles (3 dans votre cas)
        learning_rate : Vitesse d'apprentissage (alpha)
        discount_factor : Importance du futur (gamma)
        epsilon : Taux d'exploration initial
        epsilon_decay : Diminution d'epsilon après chaque épisode
        epsilon_min : Epsilon minimum
        """
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon 
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min

        # clé = ("contexte", action) -> valeur
        self.q_table = defaultdict(lambda: [0.0] * num_actions)

    
    def get_action(self, state, training=True):
        """
        Choisit une action pour un état donné
        Si training=True : exploration (epsilon-greedy)
        Si training=False : exploitation pure (meilleure action)
        """
        
        # Exploration vs Exploitation
        if training and random.random() < self.epsilon:
            # EXPLORATION : action aléatoire
            return random.randint(0, self.num_actions - 1)
        else:
            # EXPLOITATION : meilleure action selon Q-table
            q_values = self.q_table[state]  # Liste des Q-values pour cet état
            return q_values.index(max(q_values))  # Index de la plus grande valeur
    
    def update(self, state, action, reward, next_state, done):
        """
        Met à jour la Q-table avec l'équation de Bellman
        Q(s,a) = Q(s,a) + α * [r + γ * max(Q(s',a')) - Q(s,a)]
        """
        current_q = self.q_table[state][action]

        if done:
            target_q = reward
        else:
            max_next_q = max(self.q_table[next_state])
            target_q = reward + self.discount_factor * max_next_q

        new_q = current_q + self.learning_rate * (target_q - current_q)  
        self.q_table[state][action] = new_q
    




    # def decay_epsilon(self):
    #     """Réduit epsilon après chaque épisode"""
    #     if (epsilon - epsilon_decay < epsilon_min):
    #         epsilon = epsilon_min
    #     else:
    #         epsilon -= epsilon_decay
    
    # décroissance multiplicative et non soustractive => plus naturel et progressif
    def decay_epsilon(self):
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)





    def save(self, filename):
        """Sauvegarde la Q-table dans un fichier JSON (lisible)"""
        with open(filename, 'w') as f:
            json.dump(dict(self.q_table), f, indent=2)
        print(f"Q-table sauvegardée dans {filename}")

    def load(self, filename):
        """Charge une Q-table sauvegardée depuis JSON"""
        with open(filename, 'r') as f:
            q_dict = json.load(f)
            self.q_table = defaultdict(lambda: [0.0] * self.num_actions, q_dict)
        print(f"Q-table chargée depuis {filename}")

    def convert_qtable_compact(self, json_file, lua_file):
        with open(json_file, 'r') as f:
            q_table = json.load(f)
        
        entries = []
        
        for state, q_values in q_table.items():
            vals = ",".join([f"{v:.1f}" for v in q_values])
            entries.append(f'["{state}"]='+'{'+vals+'}')
        
        # Joindre avec des virgules, puis entourer de {}
        lua_code = "q_table={" + ",".join(entries) + "}"
        
        with open(lua_file, 'w') as f:
            f.write(lua_code)