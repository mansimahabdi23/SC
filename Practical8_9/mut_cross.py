import random

# --- Step 1: Single Point Crossover ---
def single_point_crossover(parent1, parent2):
    # Random crossover point (not at ends)
    point = random.randint(1, len(parent1) - 1)
    # Generate two children by swapping segments
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    print(f"\nCrossover Point: {point}")
    return child1, child2

# --- Step 2: Bit Flip Mutation ---
def bit_flip_mutation(chromosome, mutation_rate=0.2):
    mutated = ""
    for gene in chromosome:
        if random.random() < mutation_rate:
            # Flip bit: 0 → 1, 1 → 0
            mutated += '1' if gene == '0' else '0'
        else:
            mutated += gene
    return mutated

# --- MAIN PROGRAM ---
if __name__ == "__main__":
    # Initial parent chromosomes
    parent1 = "110010"
    parent2 = "101101"

    print("Parent 1:", parent1)
    print("Parent 2:", parent2)

    # --- Crossover ---
    child1, child2 = single_point_crossover(parent1, parent2)
    print("Children after Crossover:")
    print("  Child 1:", child1)
    print("  Child 2:", child2)

    # --- Mutation ---
    mutated_child1 = bit_flip_mutation(child1)
    mutated_child2 = bit_flip_mutation(child2)
    print("\nChildren after Mutation:")
    print("  Mutated Child 1:", mutated_child1)
    print("  Mutated Child 2:", mutated_child2)
