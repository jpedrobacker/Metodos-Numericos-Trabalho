import numpy as np


#Utiliza a Matriz A abaixo para fatorar em LU
def fatora_LU(a):
    n = a.shape[0]
   
    #identity cria uma matriz identidade
    l = np.identity(n)
    u = a.copy()


    #Seleciona o pivô de cada linha
    for k in range(n-1):
       
        #argmax retorna o índice de maior valor de um array como se estivesse em 1D, ou seja, como se a matriz fosse apenas uma
        pivo = np.argmax(abs(u[k:, k])) + k
        u[[k, pivo], k:] = u[[pivo, k], k:]
        l[[k, pivo], :k] = l[[pivo, k], :k]


        for i in range(k+1, n):
            factor = u[i, k] / u[k, k]
            l[i, k] = factor
            u[i, k:] = u[i, k:] - factor * u[k, k:]


    return l, u


#Resolve o sistema LU
def resolve_sistema(l, u, b):
    n = l.shape[0]
   
    #zeros_like é uma simples função do numpy cujo objetivo é criar um arranjo com o mesmo formato do arranjo dado, mas composto apenas de zeros
    y = np.zeros_like(b)
    x = np.zeros_like(b)






    for i in range(n):
        y[i] = (b[i] - np.dot(l[i, :i], y[:i])) / l[i, i]


    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(u[i, i+1:], x[i+1:])) / u[i, i]


    return x


a = np.array([[2, -1, 4, 0],[4, -1, 5, 1],[-2, 2, -2, 3],[0, 3, -9, 4]], dtype=float)


b = np.array([5, 9, 1, -2], dtype=float)




#Chama a função para fatorar a matriz A em LU
l, u = fatora_LU(a)


#Resolve o sistema de LU = A
x = resolve_sistema(l, u, b)


#Faz o print das Matrizes L e U e o retorna o resultado X
print("Matriz L:")
print(l)
print('')
print("Matriz U:")
print(u)
print('')
print("Vetor X:")
print(x)
print('')
