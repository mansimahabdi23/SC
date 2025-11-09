import numpy as np

# --- 1. FIXED MATRICES AND PARAMETERS ---

# Places: Tree (0), Car (1), House (2), Pond (3)
PLACES = ["Tree", "Car", "House", "Pond"]
num_nodes = len(PLACES)
start_node = 0 # Tree
end_node = num_nodes - 1 # Pond

print("--- Ant Colony Optimization Setup (4 Cities) ---")
print(f"Places: {', '.join(PLACES)}. Start: {PLACES[start_node]}, End: {PLACES[end_node]}.")

# User-Defined Cost (Distance) Matrix
COST_MATRIX = np.array([
    [0, 5, 15, 4],
    [5, 0, 4, 8],
    [15, 4, 0, 1],
    [4, 8, 1, 0]
], dtype=float)
print("\nCOST MATRIX (Fixed):")
print(COST_MATRIX)

# User-Input for Initial Pheromone Matrix
PHEROMONE_MATRIX = np.zeros((num_nodes, num_nodes), dtype=float)
print("\nEnter Initial Pheromone Matrix (4x4):")
for i in range(num_nodes):
    while True:
        try:
            # Example input prompt for row i
            row_input = input(f"Enter Pheromone values for row {i} (e.g., '0.0 0.2 0.1 0.3'): ").split()
            if len(row_input) != num_nodes: raise ValueError
            PHEROMONE_MATRIX[i, :] = [float(x) for x in row_input]
            break
        except ValueError:
            print("Invalid input. Please enter exactly 4 numbers separated by spaces.")

# Ensure self-loops have zero pheromone for movement logic
np.fill_diagonal(PHEROMONE_MATRIX, 0.0) 

# ACO Parameters (Set these as constants or take user input if preferred)
ALPHA = 1.0  # Pheromone Importance
BETA = 2.0   # Heuristic Importance (Cost/Distance Importance)
Q = 1.0      # Pheromone Deposit Constant
RHO = 0.1    # Evaporation Rate (Adjustable, 0.0 for no evaporation)

# Heuristic Matrix (Visibility = 1 / Cost)
HEURISTIC_MATRIX = 1.0 / (COST_MATRIX + np.finfo(float).eps)
np.fill_diagonal(HEURISTIC_MATRIX, 0) 

print(f"\nParameters: Alpha={ALPHA}, Beta={BETA}, Q={Q}, Rho={RHO}")
print("-" * 50)


# --- 2. ACO CORE FUNCTIONS (Unchanged from previous optimal code) ---

def calculate_transition_probability(current_node, unvisited_nodes, pheromone_mat, heuristic_mat):
    """Calculates the probability P_ij of moving from current_node to any unvisited_node."""
    probabilities = {}
    total_attractiveness = 0.0

    for next_node in unvisited_nodes:
        # Attractiveness = (Pheromone^Alpha) * (Heuristic^Beta)
        pheromone = pheromone_mat[current_node, next_node]
        heuristic = heuristic_mat[current_node, next_node]
        
        attractiveness = (pheromone ** ALPHA) * (heuristic ** BETA)
        probabilities[next_node] = attractiveness
        total_attractiveness += attractiveness
    
    # Normalize probabilities
    if total_attractiveness == 0:
        return {node: 1.0 / len(unvisited_nodes) for node in unvisited_nodes}
    else:
        return {node: prob / total_attractiveness for node, prob in probabilities.items()}

def find_ant_path(start, end, pheromone_mat, heuristic_mat):
    """Simulates an ant finding a path from start to end."""
    path = [start]
    current_node = start
    unvisited = set(range(num_nodes))
    unvisited.remove(start)
    
    # The ant visits the remaining nodes (up to num_nodes - 1) before the end node
    while unvisited and len(unvisited) > 1:
        possible_next_nodes = list(unvisited)
        
        # Calculate P_ij for the available next nodes
        probs = calculate_transition_probability(current_node, possible_next_nodes, pheromone_mat, heuristic_mat)
        
        # Select the next node based on probability
        nodes = list(probs.keys())
        probabilities = list(probs.values())
        
        if not nodes: break
        
        # Stochastic selection using numpy.random.choice
        next_node = np.random.choice(nodes, size=1, p=probabilities)[0]
        
        path.append(next_node)
        current_node = next_node
        unvisited.remove(next_node)

    # Append the final destination (end_node) if not already the last step
    if end not in path:
        path.append(end)

    return path

def calculate_path_cost(path, cost_mat):
    """Calculates the total distance/cost of a given path."""
    cost = 0.0
    for i in range(len(path) - 1):
        cost += cost_mat[path[i], path[i+1]]
    return cost

def update_pheromone_matrix(pheromone_mat, paths_costs, rho, Q):
    """Applies evaporation and pheromone deposition."""
    
    # 1. Evaporation
    pheromone_mat *= (1.0 - rho)
    
    # 2. Deposition
    for path, cost in paths_costs:
        delta_tau = Q / cost if cost > 0 else 0
        
        for i in range(len(path) - 1):
            start = path[i]
            end = path[i+1]
            pheromone_mat[start, end] += delta_tau
            pheromone_mat[end, start] += delta_tau # Symmetric deposition

    return pheromone_mat

# --- 3. SIMULATION EXECUTION ---

# Store paths and costs for update
paths_costs_A1_A3 = []

# 3a. Ants A1, A2, A3 Follow Paths (Using the user's initial pheromone matrix)
print("\n1. Paths of Ants A1, A2, A3 (Based on your initial pheromone):")
for ant_label in ['A1', 'A2', 'A3']:
    path = find_ant_path(start_node, end_node, PHEROMONE_MATRIX, HEURISTIC_MATRIX)
    cost = calculate_path_cost(path, COST_MATRIX)
    
    paths_costs_A1_A3.append((path, cost))
    
    path_labels = [PLACES[n] for n in path]
    print(f"  Ant {ant_label}: {' -> '.join(path_labels)} (Cost: {cost:.2f})")

# 3b. Update Pheromone Matrix based on A1, A2, A3
PHEROMONE_MATRIX = update_pheromone_matrix(PHEROMONE_MATRIX, paths_costs_A1_A3, RHO, Q)

print("-" * 50)
print("2. Pheromone Matrix After A1, A2, A3 Update (Accumulated Pheromone):")
print(np.round(PHEROMONE_MATRIX, 4))
print("-" * 50)

# 3c. Ant A4 Follows Path (Using the new, updated matrix)
print("3. Ant A4 Follows Path:")
ant_a4_label = 'A4'
ant_a4_path = find_ant_path(start_node, end_node, PHEROMONE_MATRIX, HEURISTIC_MATRIX)
ant_a4_cost = calculate_path_cost(ant_a4_path, COST_MATRIX)

ant_a4_path_labels = [PLACES[n] for n in ant_a4_path]

print(f"  Ant {ant_a4_label} **will follow** the path: **{' -> '.join(ant_a4_path_labels)}** (Cost: {ant_a4_cost:.2f})")

# 3d. Update Pheromone Matrix based on A4
# This is the "after the 4th ant the pheromone level should change" step
PHEROMONE_MATRIX = update_pheromone_matrix(PHEROMONE_MATRIX, [(ant_a4_path, ant_a4_cost)], RHO, Q)

print("-" * 50)
print("4. Pheromone Matrix After A4 Update (Final Change):")
print(np.round(PHEROMONE_MATRIX, 4))