import random

def matrix_multiply(A, B):
    #check the lenght of the Matrix
    n = len(A)
    # Create a empty result matrix
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    # Calculate the 2 Matrices
    #r picks the first row of A
    for r in range(n):
        #k picks the first column of B
        for k in range(n):
            #Multiplies the values and sums them
            for j in range(n): 
                result[r][k] += A[r][j] * B[j][k]
    
    return result

#generate the matrix with random numbers
def generate_matrix(size):
    return [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

# size of the different matrices (can be changed)
matrix_size = [4]

#creating the 2 matrices
for size in matrix_size:
    A = generate_matrix(size)
    B = generate_matrix(size)

    #print the 2 created matrices
    print (f'Matrix A:')
    for row in A:
        print (row)
    print (f'Matrix B:')
    for row in B:
        print(row)

    #prints the result matrix
    result = matrix_multiply(A, B)
    print ('\nresult:')
    for row in result:
        print(row)
