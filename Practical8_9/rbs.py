import random

def rank_based_selection(population_size, num_parents_to_select, fitness_values):
    """
    Implements the Rank-Based Selection method for Genetic Algorithms.

    Args:
        population_size (int): The total number of individuals in the current population (N).
        num_parents_to_select (int): The number of individuals to select as parents (Np).
        fitness_values (list): A list of fitness scores for each individual.

    Returns:
        list: A list of selected parent labels (e.g., 'A', 'B', 'C', ...) 
              with a length equal to num_parents_to_select.
    """
    
    # 1. Pair Individuals with their Fitness and Label
    # We need to keep track of the original index/label after sorting.
    # Individual format: (fitness, original_index)
    labeled_individuals = [(fitness_values[i], i) for i in range(population_size)]

    # 2. Sort by Fitness (Descending)
    # The highest fitness gets the highest rank (Rank 1).
    # key=lambda x: x[0] sorts by the fitness value (the first element of the tuple).
    # reverse=True ensures sorting is from highest fitness to lowest.
    labeled_individuals.sort(key=lambda x: x[0], reverse=True)
    
    # 3. Assign Rank-Based Fitness (r)
    # Rank is assigned starting from population_size (N) down to 1.
    # Rank i (highest fitness) gets fitness N, Rank N (lowest fitness) gets fitness 1.
    # This is a common linear ranking scheme.
    rank_fitness_values = []
    original_indices = []
    
    for rank in range(1, population_size + 1):
        # The rank fitness for the individual at current rank position:
        # e.g., N=5: Rank 1 gets rank_fitness 5, Rank 5 gets rank_fitness 1.
        rank_fitness = population_size - rank + 1
        
        # Store the rank fitness and the original index of the individual
        original_index = labeled_individuals[rank - 1][1]
        rank_fitness_values.append(rank_fitness)
        original_indices.append(original_index)

    # 4. Calculate Total Rank Fitness (Sum of all rank values)
    total_rank_fitness = sum(rank_fitness_values)

    # ** The rest of the selection follows the standard Roulette Wheel logic **
    
    # 5. Calculate Selection Probabilities based on Rank
    probabilities = [r_f / total_rank_fitness for r_f in rank_fitness_values]

    # 6. Calculate Cumulative Probabilities
    cumulative_probabilities = []
    current_sum = 0
    for p in probabilities:
        current_sum += p
        cumulative_probabilities.append(current_sum)

    # 7. Generate Individual Labels (A, B, C...)
    # This must use the original indices to map back to the individual's label
    original_labels = [chr(65 + i) for i in range(population_size)] 

    # 8. Select Parents using the "Rank Wheel"
    selected_parents = []
    for _ in range(num_parents_to_select):
        r = random.random() # Spin the Rank Wheel
        
        # Determine which rank slice 'r' falls into
        for i, cum_p in enumerate(cumulative_probabilities):
            if r <= cum_p:
                # 'i' is the index in the sorted list (the rank position)
                # original_indices[i] gives us the original individual's index (0 for 'A', 1 for 'B', etc.)
                selected_original_index = original_indices[i]
                selected_parents.append(original_labels[selected_original_index])
                break

    return selected_parents

# --- User Input Section ---
print("--- Genetic Algorithm: Rank-Based Selection ---")
while True:
    try:
        N = int(input("Enter the total population size (N): "))
        if N <= 0: raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer for N.")

while True:
    try:
        Np = int(input(f"Enter the number of parents to select (Np <= {N}): "))
        if Np <= 0 or Np > N: raise ValueError
        break
    except ValueError:
        print(f"Invalid input. Please enter a positive integer for Np, less than or equal to N ({N}).")

# Input Fitness Values
print(f"\nEnter the fitness value for each of the {N} individuals:")
fitness_input = []
original_labels_map = {}
for i in range(N):
    while True:
        try:
            label = chr(65 + i)
            fitness = float(input(f"Fitness for Individual {label}: "))
            if fitness < 0: raise ValueError
            fitness_input.append(fitness)
            original_labels_map[i] = label
            break
        except ValueError:
            print("Invalid input. Please enter a non-negative number for fitness.")

# --- Execution and Output ---
print("\n--- Execution Result ---")
if sum(fitness_input) == 0:
    print("All fitness values are zero. Selection is not meaningful with this method.")
else:
    parents = rank_based_selection(N, Np, fitness_input)

    # Print the selected parents in the requested series format
    print(f"Selected Parent Series ({Np} parents):")
    print(", ".join(parents))

    # Detailed Output for Clarity
    print("\n--- Selection Details ---")
    print(f"Initial Fitnesses: {dict(zip([chr(65 + i) for i in range(N)], fitness_input))}")
    print(f"The selection is based on rank, ensuring a more balanced selection pressure.")
    print(f"The individuals selected for the next generation are: **{', '.join(sorted(list(set(parents))))}**")