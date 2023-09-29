import numpy as np
# Create matrices
A= np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
#Addition
C = A + B
#Subtraction
D = A - B
#Multiplication(element-wise)
E = A * B
#Matrix multiplication
F = np.dot(A,B)# or A @ B
#Transpose
A_transpose = A.T
print("Addition:")
print(C)
print("nSubtraction:")
print(D)
print("\nElement-wise Multiplication:")
print(E)
print("\nMatrix Multiplication:")
print(F)
print("\nTranspose:")
print(A_transpose)
