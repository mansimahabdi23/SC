import numpy as np
import random
import matplotlib.pyplot as plt

# Fitness function
def fitness_function(x):
    return x**2

# Grey Wolf Optimizer
def GWO(num_wolves=8, max_iter=50, lb=-10, ub=10):
    wolves = np.random.uniform(lb, ub, num_wolves)
    alpha, beta, delta = None, None, None

    convergence_curve = []  # store best fitness per iteration

    for t in range(max_iter):
        fitness = [fitness_function(w) for w in wolves]

        # Sort wolves by fitness (lower is better)
        sorted_idx = np.argsort(fitness)
        wolves = wolves[sorted_idx]
        fitness = [fitness[i] for i in sorted_idx]

        alpha, beta, delta = wolves[0], wolves[1], wolves[2]

        a = 2 - t * (2 / max_iter)  # linearly decreases from 2 to 0
        new_wolves = []

        for i in range(num_wolves):
            X = wolves[i]

            # Update with respect to alpha
            A1 = 2 * a * random.random() - a
            C1 = 2 * random.random()
            D_alpha = abs(C1 * alpha - X)
            X1 = alpha - A1 * D_alpha

            # Update with respect to beta
            A2 = 2 * a * random.random() - a
            C2 = 2 * random.random()
            D_beta = abs(C2 * beta - X)
            X2 = beta - A2 * D_beta

            # Update with respect to delta
            A3 = 2 * a * random.random() - a
            C3 = 2 * random.random()
            D_delta = abs(C3 * delta - X)
            X3 = delta - A3 * D_delta

            # Final new position
            new_X = (X1 + X2 + X3) / 3

            # Clip to bounds
            new_X = np.clip(new_X, lb, ub)
            new_wolves.append(new_X)

        wolves = np.array(new_wolves)

        # Store best fitness of this iteration
        convergence_curve.append(fitness_function(alpha))

    return alpha, fitness_function(alpha), convergence_curve

# Run GWO
best_sol, best_fit, curve = GWO(num_wolves=8, max_iter=50)

print("Best solution found:", best_sol)
print("Fitness value:", best_fit)

# Plot convergence
plt.plot(curve, 'b-', linewidth=2)
plt.xlabel("Iteration")
plt.ylabel("Fitness (Best so far)")
plt.title("GWO Convergence Curve")
plt.grid(True)
plt.show()
