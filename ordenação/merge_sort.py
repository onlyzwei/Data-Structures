def merge_sort_recursivo(lista):
    """Implementação recursiva do Merge Sort."""
    tam_lista = len(lista)
    # Caso base: listas com 1 ou 0 elementos já estão ordenadas.
    if tam_lista > 1:
        # Calcula o índice do meio para dividir a lista em duas partes.
        meio = tam_lista // 2  
        
        # Divide a lista original em duas sublistas:
        esquerda = lista[:meio]  # Sublista da esquerda (S1)
        direita = lista[meio:]   # Sublista da direita (S2)
        
        # Tamanhos das sublistas.
        tam_esquerda = len(esquerda)
        tam_direita = len(direita)

        # Chamada recursiva para ordenar as sublistas
        merge_sort_recursivo(esquerda) # ------------------------------------>t(n/2)
        merge_sort_recursivo(direita)  # ------------------------------------>t(n/2)

        # Índices para percorrer as sublistas e a lista final(k).
        i = j = k = 0  

        # Combina as duas sublistas ordenadas em uma única lista ordenada.
        while i < tam_esquerda and j < tam_direita:# ------------------------->n
            # Escolhe o menor elemento entre S1[i] e S2[j].
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]  # Adiciona o elemento de S1 à lista.
                i += 1  # Avança o índice em S1.
            else:
                lista[k] = direita[j]  
                j += 1
            k += 1  

        # Adiciona os elementos restantes de S1, se houver.
        while i < tam_esquerda:# ------------------------->n
            lista[k] = esquerda[i]
            i += 1
            k += 1

        # Adiciona os elementos restantes de S2, se houver.
        while j < tam_direita:
            lista[k] = direita[j]
            j += 1
            k += 1

    # Retorna a lista ordenada.
    return lista

if __name__ == "__main__":
    lista = [12, 11, 13, 5, 6, 7]
    merge_sort_recursivo(lista)
    print(f"Lista ordenada: {lista}")