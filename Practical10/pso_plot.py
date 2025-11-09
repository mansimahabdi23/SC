import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Parameters ---
num_particles = 30
w, c1, c2, c3 = 0.6, 1.5, 1.5, 1.2
goal = np.array([5, 5])      # Target position
bounds = [-10, 10]

# --- Initialize particles ---
positions = np.random.uniform(bounds[0], bounds[1], (num_particles, 2))
velocities = np.random.uniform(-1, 1, (num_particles, 2))
pbest = positions.copy()
gbest = np.mean(pbest, axis=0)

# --- Plot setup ---
fig, ax = plt.subplots()
scat = ax.scatter(positions[:, 0], positions[:, 1], color='blue')
goal_dot, = ax.plot(goal[0], goal[1], 'ro', markersize=8, label='Goal')
ax.set_xlim(bounds)
ax.set_ylim(bounds)
ax.set_title("Goal-Directed Particle Swarm")
ax.legend()

# --- Update Function ---
def update(frame):
    global positions, velocities, pbest, gbest
    for i in range(num_particles):
        r1, r2, r3 = np.random.rand(), np.random.rand(), np.random.rand()
        velocities[i] = (w * velocities[i] +
                         c1 * r1 * (pbest[i] - positions[i]) +
                         c2 * r2 * (gbest - positions[i]) +
                         c3 * r3 * (goal - positions[i]))
        positions[i] += velocities[i]
        # Keep within bounds
        positions[i] = np.clip(positions[i], bounds[0], bounds[1])
        # Update personal best
        if np.linalg.norm(goal - positions[i]) < np.linalg.norm(goal - pbest[i]):
            pbest[i] = positions[i]
    gbest = pbest[np.argmin(np.linalg.norm(pbest - goal, axis=1))]
    scat.set_offsets(positions)
    ax.set_title(f"Iteration: {frame}")
    return scat,

# --- Animate ---
ani = FuncAnimation(fig, update, frames=100, interval=100, repeat=False)
plt.show()
