import random

# Recebe os 25 elementos da matriz
elements = 0
matrix_elements = []

while elements < 25:
    # integer = input("Informe um número inteiro: ")
    integer = str(random.randint(1, 9))
    if integer.isdigit():
        elements += 1
        matrix_elements.append(integer)

# Cria a matriz 5x5 a partir dos elementos
matrix = []

for i in range(0, 25, 5):
    matrix.append(matrix_elements[i:i + 5])

# Imprime a matriz
print("Matriz A:")
for line in matrix:
    print(" ".join(str(element) for element in line))

# Imprime a matriz inferior
print("Matrix A inferior:")
n_line = 0
for position in range(4, -1, -1):
    line = matrix[n_line][0:n_line + 1] + [0] * position
    print(" ".join(str(element) for element in line))
    n_line += 1
    
# Imprime a matriz superior
print("Matriz A superior:")
for position in range(5):
    line = [0] * position + matrix[position][position:5]
    print(" ".join(str(element) for element in line))


