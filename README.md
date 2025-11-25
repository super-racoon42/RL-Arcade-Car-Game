# RL Arcade Car Game

A small project where I recreated an arcade-style car game in **PICO-8**, inspired by an old McDonald's toy.  
I also built a **Reinforcement Learning agent in Python** (using the Q-Learning Method) capable of beating the game.

---

## 📁 Files included

- **voiture.p8** — Playable game  
- **voiture_rl.p8** — Version where the agent plays and beats the game  
- **voiture_rl_endless.p8** — Version where the agent plays endlessly  

---

## 🎮 How to use

To play, simply drag any `.p8` file into the **PICO-8 Education Edition**, then press: CTRL+r to run the game.

---

## 🤖 RL Agent (Python)

The RL agent is trained separately in Python and exported to a compact Lua Q-table embedded into the PICO-8 version of the game.
