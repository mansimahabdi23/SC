import numpy as np

# -------------------------------------------
# Objective (fitness) function to minimize
# Example: f(x) = x^2   --> minimum at x = 0
# -------------------------------------------
def fitness_function(x):
    return np.sum(x**2)   # You can change this as per problem

# -------------------------------------------
# Crow Search Optimization (CSO)
# -------------------------------------------
def crow_search_optimization(num_crows=10, dim=2, max_iter=50, flight_length=2.0, awareness_prob=0.1):
    # Step 1: Initialize positions of crows randomly
    # Here, we assume the search space is [-10, 10]
    lower_bound = -10
    upper_bound = 10
    positions = np.random.uniform(lower_bound, upper_bound, (num_crows, dim))
    
    # Step 2: Initialize memory of each crow (best position so far)
    memory = np.copy(positions)
    
    # Step 3: Evaluate fitness of initial positions
    fitness = np.apply_along_axis(fitness_function, 1, positions)
    best_index = np.argmin(fitness)
    global_best = positions[best_index]
    global_best_fitness = fitness[best_index]
    
    # Step 4: Main loop
    for iteration in range(max_iter):
        for i in range(num_crows):
            # Randomly select another crow to follow
            j = np.random.randint(0, num_crows)
            while j == i:
                j = np.random.randint(0, num_crows)
            
            # Generate a random number
            r = np.random.rand()
            
            if r >= awareness_prob:
                # Crow i follows crow j's memory (not aware)
                new_position = positions[i] + r * flight_length * (memory[j] - positions[i])
            else:
                # Crow j is aware, moves to random position
                new_position = np.random.uniform(lower_bound, upper_bound, dim)
            
            # Boundary check
            new_position = np.clip(new_position, lower_bound, upper_bound)
            
            # Evaluate new fitness
            new_fitness = fitness_function(new_position)
            
            # Update memory if better
            if new_fitness < fitness_function(memory[i]):
                memory[i] = new_position
        
        # Update positions
        positions = np.copy(memory)
        
        # Find global best
        fitness = np.apply_along_axis(fitness_function, 1, positions)
        best_index = np.argmin(fitness)
        
        if fitness[best_index] < global_best_fitness:
            global_best_fitness = fitness[best_index]
            global_best = positions[best_index]
        
        print(f"Iteration {iteration+1} → Best Fitness: {global_best_fitness:.5f}")
    
    print("\nBest solution found:")
    print("Position:", global_best)
    print("Fitness:", global_best_fitness)

# -------------------------------------------
# Run the algorithm
# -------------------------------------------
crow_search_optimization()
