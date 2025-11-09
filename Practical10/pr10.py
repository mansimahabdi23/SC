import numpy as np
import matplotlib.pyplot as plt

# --- Fitness Function ---
def fitness_function(x):
    # Example: Minimize f(x) = x^2 + 5*sin(x)
    return x**2 + 5 * np.sin(x)

# --- PSO Parameters ---
num_particles = 30
max_iter = 100
w = 0.7        # inertia weight
c1 = 1.5       # cognitive coefficient
c2 = 1.5       # social coefficient

# --- Initialize particles ---
x = np.random.uniform(-10, 10, num_particles)   # position
v = np.random.uniform(-1, 1, num_particles)     # velocity
pbest = x.copy()
pbest_fitness = fitness_function(x)
gbest_index = np.argmin(pbest_fitness)
gbest = pbest[gbest_index]

# --- PSO Iterations ---
convergence_curve = []

for t in range(max_iter):
    for i in range(num_particles):
        r1, r2 = np.random.rand(), np.random.rand()

        # Update velocity
        v[i] = (w * v[i]) + (c1 * r1 * (pbest[i] - x[i])) + (c2 * r2 * (gbest - x[i]))

        # Update position
        x[i] = x[i] + v[i]

        # Evaluate fitness
        fitness = fitness_function(x[i])

        # Update personal best
        if fitness < pbest_fitness[i]:
            pbest[i] = x[i]
            pbest_fitness[i] = fitness

    # Update global best
    gbest_index = np.argmin(pbest_fitness)
    gbest = pbest[gbest_index]
    convergence_curve.append(fitness_function(gbest))

# --- Results ---
print("Optimal x:", gbest)
print("Optimal fitness value:", fitness_function(gbest))

# --- Plot Convergence ---
plt.plot(convergence_curve)
plt.title("PSO Convergence Curve")
plt.xlabel("Iteration")
plt.ylabel("Best Fitness Value")
plt.show()
