
# Versão recursiva -> O(2^n)
'''
A complexidade de tempo dessa função é exponencial, pois a cada chamada recursiva, a função se chama duas vezes.
Levando a uma árvore de chamadas recursivas que cresce exponencialmente.
'''
def fibonacci_r(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonacci_r(n - 1) + fibonacci_r(n - 2)

# Versão iterativa -> O(n) (Programação Dinâmica Implícita)

'''
Isso é um caso especial de programação dinâmica, onde a redução de estado (armazenar apenas dois valores)
otimiza o uso de memória.
'''
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

# Versão iterativa -> O(n) (Programação Dinâmica Explícita)
def fibonacci_pd(n):
    if n == 0 or n == 1:
        return 1

    # Cria um array para armazenar os valores de Fibonacci calculados
    fib = [0] * (n + 1) # [0, 0, 0, ..., 0]
    fib[0] = 1          # [1, 0, 0, ..., 0]
    fib[1] = 1          # [1, 1, 0, ..., 0]

    # Calcula os valores de Fibonacci do índice 2 até n
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]
