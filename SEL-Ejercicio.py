import numpy as np

A = np.array([[52,30,18],[20,50,30],[25,20,55]])
B = np.array([[4800],[5810],[5690]])

print("Matriz A: \n"+str(A))
print("Vector B: \n"+str(B))

A_inv = np.linalg.inv(A)
print("\nMatriz_inversa de A: \n"+str(A_inv))

x = A_inv.dot(B)
print("\nCantidades: \n"+str(x))

M=A.dot(A_inv)
print("\nIdentidad: \n"+str(M))
