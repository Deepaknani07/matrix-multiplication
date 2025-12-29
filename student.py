import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5,6],
              [7,8]])
            
print("matrix A:\n",A)
print("matrix B:\n",B)

#matrix addition 

addtion = A+B
print("the addition of (a+b):\n",addtion)

# 2. Matrix Multiplication
# -----------------------------
multiplication = A @ B   # or np.matmul(A, B)
print("\nMultiplication (A × B):\n", multiplication)

# -----------------------------
# 3. Transpose
# -----------------------------
transpose_A = A.T
print("\nTranspose of Matrix A:\n", transpose_A)

# -----------------------------
# 4. Determinant
# -----------------------------
det_A = np.linalg.det(A)
print("\nDeterminant of Matrix A:", det_A)