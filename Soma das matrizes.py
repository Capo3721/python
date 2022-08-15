def soma_matrizes(m1, m2):
    rMatriz = []
    lin = len(m1)
    lin2 = len(m2)
    if lin != lin2:
        return False
    else:
        col = len(m1[0])
        col2 = len(m2[0])
        if col != col2:
            return False
            
        else:
            for i in range(lin):
                linhas = [0]*col #aqui você diz quantas colunas a sua nova matriz terá.
                
                rMatriz.append(linhas)
                for j in range(col):
                    rMatriz[i][j] = m1[i][j] + m2[i][j]
                        
                
    return rMatriz
    
    
m1 = [[2,3],[1,2],[4,8]]
m2 = [[3,4],[1,6],[6,7]]

resp = soma_matrizes(m1, m2)

print(resp)
                
        
        


            
