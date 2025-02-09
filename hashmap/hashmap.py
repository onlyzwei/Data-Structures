from linked_list import LinkedList


class HashMap:
    def __init__(self, size):
        self.size = size
        self.elements = [LinkedList() for _ in range(size)]  # Cada elemento é uma lista encadeada

    def _hash(self, key):
        """Função de hash para calcular o índice do elemento."""
        return key % self.size

    def put(self, key, value):
        """Insere ou atualiza um par chave-valor no HashMap."""
        index = self._hash(key)
        element = self.elements[index]
        # Verifica se a chave já existe na lista encadeada
        if element.find(key) is not None:
            element.remove(key)  # Remove a chave existente para atualizar o valor
        element.append(key, value)  # Adiciona o novo par chave-valor

    def get(self, key):
        """Retorna o valor associado à chave, ou None se a chave não existir."""
        index = self._hash(key)
        element = self.elements[index]
        return element.find(key)

    def remove(self, key):
        """Remove o par chave-valor associado à chave."""
        index = self._hash(key)
        element = self.elements[index]
        element.remove(key)

    def contains_key(self, key):
        """Verifica se a chave existe no HashMap."""
        index = self._hash(key)
        element = self.elements[index]
        return element.find(key) is not None

    def items(self):
        """Retorna uma lista de todos os pares chave-valor no HashMap."""
        items = []
        for element in self.elements:
            items.extend(element.items())
        return items

    def __str__(self):
        """Retorna uma representação em string do HashMap."""
        return str(self.items())