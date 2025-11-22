from game_env import ObstacleGame
from agent import QLearningAgent

def train(num_episodes=1000, display_interval=100):
    """
    Entraîne l'agent sur plusieurs épisodes
    
    num_episodes : Nombre de parties à jouer
    display_interval : Afficher stats tous les X épisodes
    """
    
    env = ObstacleGame()
    
    agent = QLearningAgent(num_actions = 3)
    
    scores = []  # Scores de chaque épisode
    
    for episode in range(num_episodes):
        
        state = env.reset()
        done = False
        total_reward = 0
        steps = 0
        
        while not done:
            
            action = agent.get_action(state, training = True)
            
            next_state, reward, done = env.step(action)
            
            agent.update(state, action, reward, next_state, done)
            
            state = next_state
            total_reward += reward
            steps += 1
        
        agent.decay_epsilon()
        
        scores.append(total_reward)
        
        if (episode + 1) % display_interval == 0:
            avg_score = sum(scores[-display_interval:]) / min(len(scores), display_interval)
            
            print(f"Épisode {episode + 1}/{num_episodes}")
            print(f"  Score moyen (derniers {display_interval}): {avg_score:.2f}")
            print(f"  Epsilon: {agent.epsilon:.3f}")
            print(f"  Taille Q-table: {len(agent.q_table)} états")
            print()
    
    # Sauvegarde de la q-table
    
    agent.save("q_table.txt")
    agent.convert_qtable_compact("q_table.txt", "q_table.lua")
    
    print("=" * 50)
    print("ENTRAÎNEMENT TERMINÉ")
    print("=" * 50)
    print(f"Score moyen (100 derniers épisodes): {avg_score}")
    print(f"Meilleur score: {max(scores)}")
    print()


    
    return agent, scores


if __name__ == "__main__":
    print("=== ENTRAÎNEMENT DE L'AGENT ===\n")
    agent, scores = train(num_episodes=1000, display_interval=100)