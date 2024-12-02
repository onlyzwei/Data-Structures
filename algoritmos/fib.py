def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    
    atual = 1
    anterior = 1
    contador = 2

    while contador <= n:
        temp = atual
        atual = atual + anterior
        anterior = temp
        contador += 1

    return atual

