import random
import numpy as np

# -----------------------------------------------
# Objective Function (to minimize)
# Example: f(x) = x^2 + 2x + 1
# -----------------------------------------------
def objective_function(x):
    return x**2 + 2*x + 1  # Minimum occurs at x = -1

# -----------------------------------------------
# Generate initial population (random real numbers)
# -----------------------------------------------
def initialize_population(pop_size, lower_bound, upper_bound):
    return [random.uniform(lower_bound, upper_bound) for _ in range(pop_size)]

# -----------------------------------------------
# Fitness Function (lower function value = higher fitness)
# Convert minimization → maximization by taking reciprocal
# -----------------------------------------------
def fitness(population):
    fitness_values = []
    for x in population:
        f = objective_function(x)
        fitness_values.append(1 / (1 + f))  # add 1 to avoid divide by zero
    return fitness_values

# -----------------------------------------------
# Roulette Wheel Selection
# -----------------------------------------------
def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    selection_probs = [f / total_fitness for f in fitness_values]
    r = random.random()
    cumulative = 0
    for i, prob in enumerate(selection_probs):
        cumulative += prob
        if r <= cumulative:
            return population[i]

# -----------------------------------------------
# Crossover (Single Point)
# -----------------------------------------------
def crossover(parent1, parent2):
    alpha = random.random()  # Blend crossover (for real numbers)
    child1 = alpha * parent1 + (1 - alpha) * parent2
    child2 = alpha * parent2 + (1 - alpha) * parent1
    return child1, child2

# -----------------------------------------------
# Mutation
# -----------------------------------------------
def mutate(x, mutation_rate=0.1):
    if random.random() < mutation_rate:
        x += random.uniform(-1, 1)  # small random change
    return x

# -----------------------------------------------
# Genetic Algorithm Main Function
# -----------------------------------------------
def genetic_algorithm(pop_size=10, generations=30, lb=-10, ub=10, mutation_rate=0.1):
    population = initialize_population(pop_size, lb, ub)

    for gen in range(generations):
        fitness_values = fitness(population)
        new_population = []

        # Elitism: keep best individual
        best_index = np.argmax(fitness_values)
        best_individual = population[best_index]
        best_value = objective_function(best_individual)
        new_population.append(best_individual)

        # Create rest of the population
        while len(new_population) < pop_size:
            # Selection
            parent1 = roulette_wheel_selection(population, fitness_values)
            parent2 = roulette_wheel_selection(population, fitness_values)

            # Crossover
            child1, child2 = crossover(parent1, parent2)

            # Mutation
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)

            # Add children
            new_population.extend([child1, child2])

        # Update population for next generation
        population = new_population[:pop_size]

        print(f"Generation {gen+1}: Best X = {best_individual:.4f}, f(X) = {best_value:.4f}")

    # Final result
    print("\n🎯 Optimized Result:")
    print(f"Best X = {best_individual:.4f}")
    print(f"Minimum f(X) = {best_value:.4f}")

# -----------------------------------------------
# Run GA
# -----------------------------------------------
genetic_algorithm()
