import numpy as np
import time
import random
import matplotlib.pyplot as plt

# Generate the matrices with random numbers
def generate_matrix(size):
    return [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

# Define matrix sizes
matrix_sizes = [10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]  
times = []

# Creating the different matrices
for size in matrix_sizes:
    A = generate_matrix(size)
    B = generate_matrix(size)
    
    # Benchmark 
    start_time = time.time()
    result_numpy = np.matmul(A, B)
    end_time = time.time()
    
    # Calculate and store the time
    duration = end_time - start_time
    times.append((size, duration))
    print(f"Matrix size {size}x{size} took {duration:.3f} seconds")

# Extract data for plotting
sizes = [size for size, _ in times]
durations = [duration for _, duration in times]

# Plot the benchmark results
plt.plot(sizes, durations, marker='o')
plt.xlabel("Matrix Size (N x N)")
plt.ylabel("Time (seconds)")
plt.title("Matrix Multiplication Benchmark")
plt.show()

# Print the benchmark results
print("\nBenchmark Results:")
for size, duration in times:
    print(f"Size {size}x{size}: {duration:.3f} seconds")
