def selection_sort(lista):
    """Implementação iterativa do Selection Sort."""
    tam = len(lista)

    for i in range(0, tam - 1):  # Itera sobre cada elemento da lista, exceto o último (lista de um elemento já esta ordenada)
        min = i                  # Assume que o menor elemento é o atual
        for j in range(i + 1, tam):  # Itera sobre os elementos restantes para encontrar o menor elemento da sublista não ordenada
            if lista[j] < lista[min]: 
                min = j 
        lista[i], lista[min] = lista[min], lista[i]  # Troca o menor elemento encontrado com o primeiro elemento da sublista não ordenada

    return lista


def selection_sort_recursivo(lista, inicio=0):
    """Implementação recursiva do Selection Sort."""
    tam = len(lista)

    if inicio >= (tam - 1):  # Caso base: lista de tamanho 1 ou já ordenada
        return lista

    min = inicio  # Assume que o menor elemento é o primeiro da sublista não ordenada

    for i in range(inicio + 1, tam):  # Itera sobre os elementos restantes para encontrar o menor elemento da sublista não ordenada
        if lista[i] < lista[min]:
            min = i

    lista[inicio], lista[min] = lista[min], lista[inicio]  # Troca o menor elemento encontrado com o primeiro elemento da sublista não ordenada

    return selection_sort_recursivo(lista, inicio + 1) 


if __name__ == "__main__":
    lista = [200, 1, 12, 3, 100, 11, 13, 7, 5, 6]

    print("Iterativo:", selection_sort(lista))
    print("Recursivo:", selection_sort_recursivo(lista, len(lista)))