def le_matriz(x,y):
    matriz2 = cria_matriz(lin,col)
    return matriz2
    

def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha=[]
        for j in range(num_colunas):
            valor = float(input("Digite o valor [" +str(i) +"][" +str(j)+ "]: "))
            linha.append(valor)
        matriz.append(linha)
    
    return matriz


lin = int(input("Digite o número de linhas da matriz: "))
col = int(input("Digite o número de colunas da matriz: "))
matriz3 = le_matriz(lin,col)

for i in range(lin):
    for j in range(col):
        print(f'[{matriz3[i][j]:^5}]',end='')
    print()



    
