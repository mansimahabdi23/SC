import numpy as np

# Define the objective function
def objective_function(x):
    # Example: Sphere function (minimize f(x) = sum(x^2))
    return np.sum(x**2)

# Grey Wolf Optimization algorithm
def grey_wolf_optimization(obj_func, dim=2, n_wolves=10, max_iter=50, lb=-10, ub=10):
    # Initialize the positions of search agents (wolves)
    wolves = np.random.uniform(lb, ub, (n_wolves, dim))
    
    # Initialize Alpha, Beta, Delta (best three wolves)
    X_alpha = np.zeros(dim)
    X_beta = np.zeros(dim)
    X_delta = np.zeros(dim)
    alpha_score = float("inf")
    beta_score = float("inf")
    delta_score = float("inf")

    # Main loop
    for iter in range(max_iter):
        # Evaluate each wolf
        for i in range(n_wolves):
            # Keep wolves within search space
            wolves[i] = np.clip(wolves[i], lb, ub)

            # Calculate fitness
            fitness = obj_func(wolves[i])

            # Update Alpha, Beta, Delta
            if fitness < alpha_score:
                alpha_score = fitness
                X_alpha = wolves[i].copy()
            elif fitness < beta_score:
                beta_score = fitness
                X_beta = wolves[i].copy()
            elif fitness < delta_score:
                delta_score = fitness
                X_delta = wolves[i].copy()

        # Parameter 'a' decreases linearly from 2 to 0
        a = 2 - iter * (2 / max_iter)

        # Update the position of each wolf
        for i in range(n_wolves):
            r1, r2 = np.random.rand(), np.random.rand()
            A1 = 2 * a * r1 - a
            C1 = 2 * r2
            D_alpha = abs(C1 * X_alpha - wolves[i])
            X1 = X_alpha - A1 * D_alpha

            r1, r2 = np.random.rand(), np.random.rand()
            A2 = 2 * a * r1 - a
            C2 = 2 * r2
            D_beta = abs(C2 * X_beta - wolves[i])
            X2 = X_beta - A2 * D_beta

            r1, r2 = np.random.rand(), np.random.rand()
            A3 = 2 * a * r1 - a
            C3 = 2 * r2
            D_delta = abs(C3 * X_delta - wolves[i])
            X3 = X_delta - A3 * D_delta

            # Average position update
            wolves[i] = (X1 + X2 + X3) / 3

        # Print iteration info
        print(f"Iteration {iter+1}/{max_iter} | Best Fitness: {alpha_score:.6f}")

    # Return the best solution found
    return X_alpha, alpha_score


# Run the algorithm
best_pos, best_score = grey_wolf_optimization(objective_function, dim=2, n_wolves=15, max_iter=100)

print("\n------------------------------")
print("Best Solution (Position):", best_pos)
print("Best Objective Value (Fitness):", best_score)
print("------------------------------")
