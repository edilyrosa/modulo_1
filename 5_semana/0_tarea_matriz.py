# La diagonal principal de una matriz cuadrada, son los elementos donde el índice de fila es 
# igual al índice de columna, es decir, donde i == j.
matriz = [
[0, 1, 1], # fila 0
[1, 0, 1], # fila 1
[1, 1, 0]  # fila 2
]

for i in range(len(matriz)):        #[0, 1, 1]
    for j in range(len(matriz[i])): # 0, 1, 1
        if i == j:
            print(f'Diagonal[{i}][{j}]',matriz[i][j]) # 0, 0, 0
