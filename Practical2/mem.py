import numpy as np
import matplotlib.pyplot as plt

# --- Define membership functions ---

def triangular(x, a, b, c):
    return np.maximum(0, np.minimum((x-a)/(b-a), (c-x)/(c-b)))

def trapezoidal(x, a, b, c, d):
    return np.maximum(0, np.minimum(np.minimum((x-a)/(b-a), 1), (d-x)/(d-c)))

def gaussian(x, mean, sigma):
    return np.exp(-((x - mean)**2) / (2 * sigma**2))

# --- Define universes ---
X = np.linspace(0, 10, 100)  # Temperature
Y = np.linspace(0, 10, 100)  # Comfort Level

# --- Compute membership values ---
μX_tri = triangular(X, 2, 5, 8)
μY_tri = triangular(Y, 3, 6, 9)

μX_trap = trapezoidal(X, 1, 3, 7, 9)
μY_trap = trapezoidal(Y, 2, 4, 6, 8)

μX_gauss = gaussian(X, 5, 1.5)
μY_gauss = gaussian(Y, 6, 1.5)

# --- Fuzzy Relation using min(μX, μY) ---
R_tri = np.minimum.outer(μX_tri, μY_tri)
R_trap = np.minimum.outer(μX_trap, μY_trap)
R_gauss = np.minimum.outer(μX_gauss, μY_gauss)

# --- Plot Membership Functions ---
plt.figure(figsize=(10,6))
plt.plot(X, μX_tri, label="Triangular Membership (X)")
plt.plot(X, μX_trap, label="Trapezoidal Membership (X)")
plt.plot(X, μX_gauss, label="Gaussian Membership (X)")
plt.title("Fuzzy Membership Functions")
plt.xlabel("Input Variable (e.g., Temperature)")
plt.ylabel("Membership Degree")
plt.legend()
plt.grid(True)
plt.show()

# --- Display Fuzzy Relation Example ---
print("Sample Fuzzy Relation Matrix (Triangular):\n", np.round(R_tri, 2))
