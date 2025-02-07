class Queue:
    def __init__(self):
        """Инициализация пустой очереди."""
        self.items = []

    def enqueue(self, item):
        """Добавление элемента в конец очереди."""
        self.items.append(item)

    def dequeue(self):
        """Удаление и возврат первого элемента очереди."""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")

    def peek(self):
        """Возвращает первый элемент очереди без удаления."""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("peek from empty queue")

    def is_empty(self):
        """Проверка, пуста ли очередь."""
        return len(self.items) == 0

    def size(self):
        """Возвращает размер очереди."""
        return len(self.items)


# Пример использования
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())  # 1
    print(queue.peek())  # 2
    print(queue.size())  # 2
