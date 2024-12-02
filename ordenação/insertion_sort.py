def insertion_sort(lista):
    for i in range(1, len(lista)):  # Começa da segunda posição (índice 1)
        
        chave = lista[i]           # Elemento atual a ser inserido na parte ordenada
        j = i                      # Índice do elemento atual

        # Desloca os elementos maiores que a chave para a direita
        while j > 0 and lista[j - 1] > chave:
            lista[j] = lista[j - 1]
            j -= 1
        
        lista[j] = chave           # Insere a chave na posição correta
    
    return lista


def insertion_sort_recursivo(lista, num):
    if num > 1:                                   # Caso base: lista de tamanho 1 já está ordenada

        insertion_sort_recursivo(lista, num - 1)  # Ordena os primeiros n-1 elementos
        j = num - 1                               # Índice do elemento atual
        chave = lista[j]                          # Elemento atual a ser inserido

        # Desloca os elementos maiores que a chave para a direita
        while j > 0 and lista[j - 1] > chave:
            lista[j] = lista[j - 1]
            j -= 1

        lista[j] = chave  # Insere a chave na posição correta
    
    return lista


if __name__ == "__main__":
    lista = [200, 1, 12, 3, 100, 11, 13, 7, 5, 6]

    print("Iterativo:", insertion_sort(lista))
    print("Recursivo:", insertion_sort_recursivo(lista, len(lista)))
