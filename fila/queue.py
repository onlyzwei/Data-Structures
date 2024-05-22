from node import Node

class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def enqueue(self, data):
        node = Node(data)
        # Fila vazia
        if self.last is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        
        self._size += 1

    def dequeue(self):
        # Fila não vazia
        if self.first is not None:
            data = self.first.data
            self.first = self.first.next
            self._size -= 1
            return data
        
        raise IndexError("The queue is empty")

    def peek(self):
        # Fila não vazia
        if self.first is not None:
            data = self.first.data
            return data
        
        raise IndexError("The queue is empty")

    def __len__(self):
        return self._size

    def __repr__(self):
        repr = ""
        if self.last is not None:
            runner = self.first
            while(runner):
                repr += f"{runner.data} "
                runner = runner.next
            return repr.strip()
        return "Empty queue"

    def __str__(self):
        return self.__repr__()
