# Fuzzy Set Operations Implementation
# Example: Customer Satisfaction at Two Restaurants (A and B)

# Define fuzzy sets (Customer Satisfaction levels)
A = {'C1': 0.2, 'C2': 0.5, 'C3': 0.8, 'C4': 1.0}
B = {'C1': 0.4, 'C2': 0.7, 'C3': 0.6, 'C4': 0.9}

#  Fuzzy Union (A ∪ B) - max of memberships
def fuzzy_union(A, B):
    return {x: max(A[x], B[x]) for x in A}

# Fuzzy Intersection (A ∩ B) - min of memberships
def fuzzy_intersection(A, B):
    return {x: min(A[x], B[x]) for x in A}

# Fuzzy Complement (A') - 1 - membership
def fuzzy_complement(A):
    return {x: round(1 - A[x], 2) for x in A}

# 4Fuzzy Difference (A - B) - min(A(x), 1 - B(x))
def fuzzy_difference(A, B):
    return {x: round(min(A[x], 1 - B[x]), 2) for x in A}

#fuzzy algebraic sum (A ⊕ B) - A(x) + B(x) - A(x)*B(x) 
def fuzzy_sum(A, B):                                                                                                             
    return {x: round(A[x] + B[x] - (A[x] * B[x]), 2) for x in A}

#  Fuzzy Cartesian Product (A × B)
# gives all possible pairs with min(A(x), B(y))
def fuzzy_cartesian_product(A, B):
    return {(x, y): round(min(A[x], B[y]), 2) for x in A for y in B}

# Perform operations
union_AB = fuzzy_union(A, B)
intersection_AB = fuzzy_intersection(A, B)
complement_A = fuzzy_complement(A)
difference_AB = fuzzy_difference(A, B)
sum_AB = fuzzy_sum(A, B) 
cartesian_AB = fuzzy_cartesian_product(A, B)

# Display results
print("Fuzzy Set A (Restaurant A):", A)
print("Fuzzy Set B (Restaurant B):", B)
print("\nUnion (A ∪ B):", union_AB)
print("\nIntersection (A ∩ B):", intersection_AB)
print("\nComplement (A'):", complement_A)
print("\nDifference (A - B):", difference_AB)
print("\nAlgebraic Sum A(x)+B(x):", sum_AB)
print("\nCartesian Product (A × B):")
for pair, value in cartesian_AB.items():
    print(f"{pair}: {value}")
