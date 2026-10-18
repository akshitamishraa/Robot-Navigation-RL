# 🤖 Robot Navigation using Q-Learning

An interactive Reinforcement Learning project that trains a robot to navigate a grid environment, avoid obstacles, and reach its destination using the **Q-Learning algorithm**. The trained agent is visualized with Pygame.

## 🎮 Game Output

The screenshot below shows the robot navigation simulation after the goal has been reached.

![Robot Navigation Game Output](images/robot-navigation-output.png)

- 🟦 **Blue circle:** Robot
- 🟩 **Green cell:** Goal reached indicator in the current demo
- ⬛ **Black cells:** Obstacles
- 🟨 **Yellow cell:** Goal position

## ✨ Features

- Q-Learning reinforcement learning algorithm
- 10 × 10 grid-based environment
- Obstacle avoidance
- Goal-directed navigation
- Training reward visualization
- Agent evaluation in the configured environment
- Pygame animation
- Saved Q-table for the trained agent
- Jupyter Notebook for training and experimentation

## 🛠️ Technologies Used

- Python 3.13
- NumPy
- Matplotlib
- Pygame
- Jupyter Notebook
- Reinforcement Learning / Q-Learning

## 📂 Project Structure

```text
Robot-Navigation-RL/
├── images/
│   └── robot-navigation-output.png
├── Robot_Navigation_Training.ipynb
├── robot_demo.py
├── q_table.npy
├── requirements.txt
└── README.md
```

## 🧠 How It Works

The robot learns by interacting with a grid environment. At each state, it chooses an action (up, down, left, or right) and receives a reward or penalty. Q-Learning updates the estimated value of actions, allowing the agent to learn a route toward the goal.

### Environment

| Parameter | Value |
|---|---|
| Grid size | 10 × 10 |
| Start position | `(0, 0)` |
| Goal position | `(9, 9)` |
| Actions | Up, Down, Left, Right |
| Training episodes | 2,000 |

### Reward System

| Event | Reward |
|---|---:|
| Reach the goal | +100 |
| Valid non-goal move | -1 |
| Hit an obstacle or boundary | -5 |

### Q-Learning Update

`Q(s, a) ← Q(s, a) + α [r + γ maxₐ′ Q(s′, a′) − Q(s, a)]`

Where `α` is the learning rate, `γ` is the discount factor, `r` is the reward, `s` is the current state, and `s′` is the next state.

## 📊 Results

Results from the current training and evaluation run:

| Metric | Result |
|---|---:|
| Training episodes | 2,000 |
| Average training reward | 68.33 |
| Average reward in last 100 episodes | 82.76 |
| Evaluation episodes | 100 |
| Successful episodes | 100 |
| Failed episodes | 0 |
| Goal success rate | 100% |
| Average evaluation reward | 83.0 |
| Shortest path found | 18 moves |

**Note:** These results apply to the current grid, obstacle layout, and trained Q-table. Performance may vary in other environments.

## ⚙️ Installation and Setup

### 1. Clone the repository


git clone https://github.com/akshitamishraa/Robot-Navigation-RL.git
cd Robot-Navigation-RL


### 2. Install dependencies

Python 3.13 is recommended for the current setup:

```powershell
py -3.13 -m pip install -r requirements.txt
```

### 3. Run the simulation

```powershell
py -3.13 robot_demo.py
```

Keep `q_table.npy` in the project directory; the demo loads the trained Q-table from this file.

## 📓 Training the Agent

Open `Robot_Navigation_Training.ipynb` in Jupyter Notebook or VS Code and run the cells in order to create the environment, train the Q-Learning agent, visualize rewards, evaluate the policy, and save the Q-table.

## 🎮 Simulation

The current demo runs the trained robot automatically. Close the Pygame window to exit. The `R` reset key works only if it is implemented in the current `robot_demo.py`.

## 🚀 Future Improvements

- Add manual keyboard control
- Improve robot and environment graphics
- Display score, reward, and step count in the game window
- Test random obstacle layouts and larger grids
- Compare Q-Learning with Deep Q-Networks (DQN)
- Add more training and performance visualizations

## 👩‍💻 Author

**Akshita Mishra**

- GitHub: [@akshitamishraa](https://github.com/akshitamishraa)
- LinkedIn: [Akshita Mishra](https://www.linkedin.com/in/akshita-mishra-643244377/)

## 📜 License

This project is shared for educational and portfolio purposes. Add a specific open-source license if you want to formally define reuse permissions.
