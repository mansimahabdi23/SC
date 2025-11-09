import random

def roulette_wheel_selection(population_size, num_parents_to_select, fitness_values):
    """
    Implements the Roulette Wheel Selection method for Genetic Algorithms.

    Args:
        population_size (int): The total number of individuals in the current population (N).
        num_parents_to_select (int): The number of individuals to select as parents (Np).
        fitness_values (list): A list of fitness scores for each individual.

    Returns:
        list: A list of selected parent labels (e.g., 'A', 'B', 'C', ...) 
              with a length equal to num_parents_to_select.
    """
    # 1. Calculate Total Fitness (Sum of all fitness values)
    total_fitness = sum(fitness_values)

    # 2. Calculate Selection Probabilities
    # Each individual's probability is (its fitness / total_fitness)
    probabilities = [f / total_fitness for f in fitness_values]

    # 3. Calculate Cumulative Probabilities
    # This creates the 'roulette wheel' slices.
    cumulative_probabilities = []
    current_sum = 0
    for p in probabilities:
        current_sum += p
        cumulative_probabilities.append(current_sum)

    # 4. Generate Individual Labels
    # e.g., N=4 -> ['A', 'B', 'C', 'D']
    labels = [chr(65 + i) for i in range(population_size)] # 65 is ASCII for 'A'

    # 5. Select Parents
    selected_parents = []
    for _ in range(num_parents_to_select):
        # Generate a random number 'r' between 0 and 1
        r = random.random() # [0.0, 1.0)

        # Determine which individual's cumulative probability slice 'r' falls into
        for i, cum_p in enumerate(cumulative_probabilities):
            if r <= cum_p:
                selected_parents.append(labels[i])
                break

    return selected_parents

# --- User Input Section ---
print("--- Genetic Algorithm: Roulette Wheel Selection ---")
while True:
    try:
        # N: Population Size
        N = int(input("Enter the total population size (N): "))
        if N <= 0: raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer for N.")

while True:
    try:
        # Np: Number of Parents to Select
        Np = int(input(f"Enter the number of parents to select (Np <= {N}): "))
        if Np <= 0 or Np > N: raise ValueError
        break
    except ValueError:
        print(f"Invalid input. Please enter a positive integer for Np, less than or equal to N ({N}).")

# Input Fitness Values
print(f"\nEnter the fitness value for each of the {N} individuals:")
fitness_input = []
for i in range(N):
    while True:
        try:
            # Individual labels are A, B, C...
            label = chr(65 + i)
            fitness = float(input(f"Fitness for Individual {label}: "))
            if fitness < 0: raise ValueError
            fitness_input.append(fitness)
            break
        except ValueError:
            print("Invalid input. Please enter a non-negative number for fitness.")

# --- Execution and Output ---
print("\n--- Execution Result ---")
if sum(fitness_input) == 0:
    print("All fitness values are zero. Selection is not possible with this method.")
else:
    parents = roulette_wheel_selection(N, Np, fitness_input)

    # Print the selected parents in the requested series format
    print(f"Selected Parent Series ({Np} parents):")
    print(", ".join(parents))

    # Detailed Output for Clarity
    print("\n--- Selection Details ---")
    print("Random values generated: {}")
    print(f"Initial Fitnesses: {dict(zip([chr(65 + i) for i in range(N)], fitness_input))}")
    print(f"Total Fitness: {sum(fitness_input)}")
    print(f"The individuals selected for the next generation are: **{', '.join(sorted(list(set(parents))))}**")