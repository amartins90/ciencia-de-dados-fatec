import random

# Recebe as dimensões das matrizes A e B
matrix_dimensions = []

while len(matrix_dimensions) < 1:
    ma_d1 = input("Informe a primeira dimensão da Matriz A: ")
    if ma_d1.isdigit():
        matrix_dimensions.append(ma_d1)
        
while len(matrix_dimensions) < 2:
    ma_d2 = input("Informe a segunda dimensão da Matriz A: ")
    if ma_d2.isdigit():
        matrix_dimensions.append(ma_d2)
        
while len(matrix_dimensions) < 3:
    mb_d1 = input("Informe a primeira dimensão da Matriz B: ")
    if mb_d1.isdigit():
        matrix_dimensions.append(mb_d1)
        
while len(matrix_dimensions) < 4:
    mb_d2 = input("Informe a segunda dimensão da Matriz B: ")
    if mb_d2.isdigit():
        matrix_dimensions.append(mb_d2)

# Retorna um erro caso as matrizes sejam de ordens diferentes
if not matrix_dimensions[0:2] == matrix_dimensions[2:4]:
    print("Erro: as matrizes A e B não são da mesma ordem")
    exit()
    
# Recebe os elementos das matrizes A e B
elements_matrix_a = []
while len(elements_matrix_a) < int(ma_d1) * int(ma_d2):
    # element = input("Informe o elemento #" + str(len(elements_matrix_a) + 1) + " da Matriz A: ")
    element = str(random.randint(1, 9))
    if element.isdigit():
        elements_matrix_a.append(int(element))

elements_matrix_b = []
while len(elements_matrix_b) < int(mb_d1) * int(mb_d2):
    # element = input("Informe o elemento #" + str(len(elements_matrix_a) + 1) + " da Matriz B: ")
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
    
# Soma as matrizes
sum_up = []
for line in range(len(matrix_a)):
    for item in range(len(matrix_a[line])):
        sum_up.append(matrix_a[line][item] + matrix_b[line][item])

# Cria matriz resultante da soma das matrizes A e B
matrix_c = []
for i in range(0, int(ma_d1) * int(ma_d2), int(ma_d2)):
    matrix_c.append(sum_up[i:i + int(ma_d2)])
    
# Imprime a matriz resultante da soma
print("Matriz A + Matriz B:")
for line in matrix_c:
    print(" ".join(str(element) for element in line))
