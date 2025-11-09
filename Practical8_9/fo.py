import numpy as np
import random
import matplotlib.pyplot as plt

# Function to optimize
def fitness_function(x):
    return x * np.sin(10 * np.pi * x) + 2.0

# GA parameters
POP_SIZE = 20
GENS = 50
MUT_RATE = 0.1
CROSS_RATE = 0.8
X_BOUND = [-1, 2]  # Search space

# Generate initial population
population = np.random.uniform(X_BOUND[0], X_BOUND[1], POP_SIZE)

# Function to select parents (Roulette Wheel Selection)
def selection(pop, fitness):
    probs = fitness / np.sum(fitness)
    idx = np.random.choice(range(POP_SIZE), size=POP_SIZE, p=probs)
    return pop[idx]

# Crossover operation
def crossover(parent, pop):
    if np.random.rand() < CROSS_RATE:
        i = np.random.randint(0, POP_SIZE)
        cross_point = np.random.rand()
        child = cross_point * parent + (1 - cross_point) * pop[i]
        return child
    else:
        return parent

# Mutation operation
def mutate(child):
    if np.random.rand() < MUT_RATE:
        child += np.random.uniform(-0.1, 0.1)
    return np.clip(child, X_BOUND[0], X_BOUND[1])

# Main GA loop
best_scores = []
for gen in range(GENS):
    fitness = fitness_function(population)
    best_idx = np.argmax(fitness)
    best_scores.append(fitness[best_idx])
    
    selected = selection(population, fitness)
    new_pop = []
    for parent in selected:
        child = crossover(parent, population)
        child = mutate(child)
        new_pop.append(child)
    population = np.array(new_pop)

best_solution = population[np.argmax(fitness_function(population))]
best_value = np.max(fitness_function(population))

print(f"Optimal x = {best_solution:.4f}, Maximum value f(x) = {best_value:.4f}")

# Plot convergence
plt.plot(best_scores)
plt.title("Genetic Algorithm Optimization Progress")
plt.xlabel("Generation")
plt.ylabel("Best Fitness Value")
plt.show()
