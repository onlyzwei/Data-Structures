from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, key, value):
        new_node = Node(key, value)
        # Caso especial: a lista está vazia
        if self.head == None:
            self.head = new_node
        # Caso contrário, percorre a lista até o último nó
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find(self, key):
        current = self.head
        # Percorre a lista até encontrar a chave
        while current:
            if current.key == key:
                return current.value
            current = current.next
        # Se chegou até aqui a chave não foi encontrada
        return None

    def remove(self, key):
        # Caso especial: a lista está vazia, não há nada para remover
        if self.head == None:
            return

        # Caso especial: remover o primeiro nó (nó-cabeça)
        if self.head.key == key:
            trash = self.head
            self.head = self.head.next
            del trash
            return

        # Tratado os casos especiais, o nó só pode estar em algum lugar após o nó-cabeça ou não estar na lista
        current = self.head
        while current.next:
            if current.next.key == key:
                trash = current.next
                current.next = current.next.next
                del trash
                return

    def items(self):
        """Retorna uma lista de todos os pares chave-valor na lista encadeada."""
        items = []
        current = self.head
        while current:
            items.append((current.key, current.value))
            current = current.next
        return items

    def __str__(self):
        """Retorna uma representação em string da lista encadeada."""
        return str(self.items())