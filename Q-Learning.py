import numpy as np

Q = np.zeros((3, 2))

alpha = 0.1
gamma = 0.9

state = 0
action = 1
reward = 10
next_state = 1

Q[state, action] += alpha * (
    reward + gamma * np.max(Q[next_state])
    - Q[state, action]
)

print(Q)