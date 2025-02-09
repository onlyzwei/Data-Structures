class Node:
    """Nó da lista encadeada."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None