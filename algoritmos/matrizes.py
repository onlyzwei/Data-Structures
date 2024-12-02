def multiplicacao(A, B):
    # Determina as dimensões das matrizes A e B
    linhas_a = len(A)        # Número de linhas da matriz A
    colunas_a = len(A[0])    # Número de colunas da matriz A
    linhas_b = len(B)        # Número de linhas da matriz B
    colunas_b = len(B[0])    # Número de colunas da matriz B

    # Verifica se a multiplicação é possível (colunas de A == linhas de B)
    if colunas_a != linhas_b:
        return None

    # Inicializa a matriz resultante com zeros
    resultante = []
    for i in range(linhas_a):
        linha = [0] * colunas_b
        resultante.append(linha)

    # Calcula a multiplicação de matrizes
    for i in range(linhas_a):
        for j in range(colunas_b):
            soma = 0
            for k in range(colunas_a):
                soma += A[i][k] * B[k][j]
            resultante[i][j] = soma

    return resultante


def contador_de_multiplicacoes(A, B):
    # Determina as dimensões das matrizes A e B
    linhas_a = len(A)        # Número de linhas da matriz A
    colunas_a = len(A[0])    # Número de colunas da matriz A
    linhas_b = len(B)        # Número de linhas da matriz B
    colunas_b = len(B[0])    # Número de colunas da matriz B

    # Verifica se a multiplicação é possível
    if colunas_a != linhas_b:
        return None

    # Conta o número de multiplicações necessárias
    contador_de_multiplicacoes = 0
    for i in range(linhas_a):
        for j in range(colunas_b):
            for k in range(colunas_a):
                contador_de_multiplicacoes += 1

    return contador_de_multiplicacoes


if __name__ == "__main__":
    # Definição das matrizes de exemplo
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    B = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    C = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    # Primeira operação: (A x B) x C
    D = multiplicacao(A, B)  # Multiplica A x B, resultando em D (3x3)
    R = multiplicacao(D, C)  # Multiplica D x C, resultando na matriz final R (3x2)

    # Conta as multiplicações em cada etapa
    R1 = contador_de_multiplicacoes(A, B)  # Multiplicações para A x B
    R2 = contador_de_multiplicacoes(D, C)  # Multiplicações para D x C

    # Total de multiplicações para (A x B) x C
    print(R1 + R2)  # Resultado esperado: 45

    '''
    Explicação: é baseado nos 3 for's 

    - A primeira multiplicação (A x B) é entre matrizes 3x3 e 3x3:
        Número de multiplicações = linhas_A * colunas_B * (colunas_A ou linhas_B, pois sao iguais) = 3 * 3 * 3 = 27

    - A segunda multiplicação (D x C) é entre matrizes 3x3 e 3x2:
        Número de multiplicações = linhas_D * colunas_C * (colunas_D ou linhas_C, pois sao iguais) = 3 * 2 * 3 = 18
        
    - Soma total: 27 + 18 = 45
    '''

    # Segunda operação: A x (B x C)
    D = multiplicacao(B, C)  # Multiplica B x C, resultando em D (3x2)
    R = multiplicacao(A, D)  # Multiplica A x D, resultando na matriz final R (3x2)

    # Conta as multiplicações em cada etapa
    R1 = contador_de_multiplicacoes(B, C)  # Multiplicações para B x C
    R2 = contador_de_multiplicacoes(A, D)  # Multiplicações para A x D

    # Total de multiplicações para A x (B x C)
    print(R1 + R2)  # Resultado esperado: 36

    '''
    Explicação: é baseado nos 3 for's 

    - A primeira multiplicação (B x C) é entre matrizes 3x3 e 3x2:
        Número de multiplicações = linhas_B * colunas_C * (colunas_B ou linhas_C, pois sao iguais) = 3 * 2 * 3 = 18

    - A segunda multiplicação (A x D) é entre matrizes 3x3 e 3x2:
        Número de multiplicações = linhas_A * colunas_D * (colunas_A ou linhas_D, pois sao iguais) =3 * 2 * 3 = 18

    - Soma total: 18 + 18 = 36
    '''

    '''
    Conclusão:
    Dependendo da ordem da multiplicação, o número total de operações muda.
    '''