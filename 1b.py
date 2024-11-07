import time
import random

def matrix_multiply(A, B):
    #check the length of the matrix
    n = len(A)
    #create an empty result matrix
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    #r picks the first row of A
    for r in range(n):
        #k picks the first column of B
        for k in range(n):
            #Multiplies the values and sums them
            for j in range(n): 
                result[r][k] += A[r][j] * B[j][k]
    
    return result

#generate the matrices with random numbers
def generate_matrix(size):
    return [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

# size of the different matrices (can be changed)
matrix_sizes = [10, 100, 200, 300, 1000]  
times = []

#creating the different matrices
for size in matrix_sizes:
    A = generate_matrix(size)
    B = generate_matrix(size)
    
    #Benchmark 
    start_time = time.time()
    matrix_multiply(A, B)
    end_time = time.time()
    
    #calculating the time
    duration = end_time - start_time
    times.append((size, duration))
    print(f"Matrix size {size}x{size} took {duration:.3f} seconds")

# Print the benchmark results
print("\nBenchmark Results:")
for size, duration in times:
    print(f"Size {size}x{size}: {duration:.3f} seconds")
