import random

# ---------------------------------------
# Helper functions
# ---------------------------------------

# Fitness function: count of 1's in chromosome
def fitness(chromosome):
    return sum(chromosome)

# Roulette Wheel Selection
def roulette_wheel_selection(population, fitness_values, num_parents):
    total_fitness = sum(fitness_values)
    selection_probs = [f / total_fitness for f in fitness_values]

    selected_parents = []
    for _ in range(num_parents):
        r = random.random()
        cumulative = 0
        for i, prob in enumerate(selection_probs):
            cumulative += prob
            if r <= cumulative:
                selected_parents.append(population[i])
                break
    return selected_parents

# Single-point Crossover
def single_point_crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Bit-flip Mutation
def bit_flip_mutation(chromosome, mutation_rate=0.1):
    mutated = []
    for gene in chromosome:
        if random.random() < mutation_rate:
            mutated.append(1 - gene)  # flip 0↔1
        else:
            mutated.append(gene)
    return mutated

# ---------------------------------------
# Main Demonstration
# ---------------------------------------

# Sample binary population (4 individuals, each of length 6)
population = [
    [1, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 1]
]

print("Initial Population:")
for p in population:
    print(p)

# Step : Fitness Evaluation
fitness_values = [fitness(p) for p in population]
print("\nFitness of each individual:", fitness_values)

# Step : Selection (Roulette Wheel)
parents = roulette_wheel_selection(population, fitness_values, num_parents=2)
print("\nSelected Parents (via Roulette Wheel):")
for p in parents:
    print(p)

# Step : Crossover
child1, child2 = single_point_crossover(parents[0], parents[1])
print(f"\nCrossover between {parents[0]} and {parents[1]}")
print("Generated Children:")
print("Child 1:", child1)
print("Child 2:", child2)

# Step : Mutation
mutated_child1 = bit_flip_mutation(child1, mutation_rate=0.2)
mutated_child2 = bit_flip_mutation(child2, mutation_rate=0.2)
print("\nAfter Mutation (bit-flip with 0.2 rate):")
print("Mutated Child 1:", mutated_child1)
print("Mutated Child 2:", mutated_child2)
