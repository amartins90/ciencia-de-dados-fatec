import random

# Recebe as dimensões das matrizes A e B
matrix_dimensions = []

while len(matrix_dimensions) < 1:
    ma_d1 = input("Informe a primeira dimensão da matriz A: ")
    if ma_d1.isdigit():
        matrix_dimensions.append(int(ma_d1))

while len(matrix_dimensions) < 2:
    ma_d2 = input("Informe a segunda dimensão da matriz A: ")
    if ma_d2.isdigit():
        matrix_dimensions.append(int(ma_d2))

while len(matrix_dimensions) < 3:
    mb_d1 = input("Informe a primeira dimensão da matriz B: ")
    if mb_d1.isdigit():
        matrix_dimensions.append(int(mb_d1))

while len(matrix_dimensions) < 4:
    mb_d2 = input("Informe a segunda dimensão da matriz B: ")
    if mb_d2.isdigit():
        matrix_dimensions.append(int(mb_d2))

if matrix_dimensions[1] != matrix_dimensions[2]:
    print("Não é possível realizar a multiplicação, a ordem das matrizes não são compatíveis")
    exit()

# Recebe os elementos das matrizes A e B
elements_matrix_a = []
while len(elements_matrix_a) < int(ma_d1) * int(ma_d2):
    #element = input("Informe o elemento #" + str(len(elements_matrix_a) + 1) + " da Matriz A: ")
    element = str(random.randint(1, 9))
    if element.isdigit():
        elements_matrix_a.append(int(element))

elements_matrix_b = []
while len(elements_matrix_b) < int(mb_d1) * int(mb_d2):
    #element = input("Informe o elemento #" + str(len(elements_matrix_a) + 1) + " da Matriz B: ")
    element = str(random.randint(1, 9))
    if element.isdigit():
        elements_matrix_b.append(int(element))

# Cria as matrizes     
matrix_a = []
for i in range(0, int(ma_d1) * int(ma_d2), int(ma_d2)):
    matrix_a.append(elements_matrix_a[i:i + int(ma_d2)])
    
matrix_b = []
for i in range(0, int(mb_d1) * int(mb_d2), int(mb_d2)):
    matrix_b.append(elements_matrix_b[i:i + int(mb_d2)])

# Imprime as matrizes
print("Matriz A:")
for line in matrix_a:
    print(" ".join(str(element) for element in line))
    
print("Matriz B:")
for line in matrix_b:
    print(" ".join(str(element) for element in line))

# Multiplica as matrizes
mult = []
for line in matrix_a:
    col_index = 0
    for i in range(matrix_dimensions[3]):
        row_index = 0
        total = 0
        for item in line:
            total += item * matrix_b[row_index][col_index]
            row_index += 1
        mult.append(total)
        col_index += 1

# Cria matriz resultante da multiplicação das matrizes A e B
matrix_c = list()
for i in range(0, matrix_dimensions[1] * matrix_dimensions[2], matrix_dimensions[1]):
    matrix_c.append(mult[i:i + matrix_dimensions[1]])

# Imprime a matriz resultante da multiplicação
print("Matriz A * Matriz B:")
for line in matrix_c:
    print(" ".join(str(element) for element in line))
