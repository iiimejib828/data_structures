class Stack:
    def __init__(self):
        """Инициализация пустого стека."""
        self.items = []

    def push(self, item):
        """Добавление элемента в стек."""
        self.items.append(item)

    def pop(self):
        """Удаление и возврат верхнего элемента стека."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """Возвращает верхний элемент стека без удаления."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        """Проверка, пуст ли стек."""
        return len(self.items) == 0

    def size(self):
        """Возвращает размер стека."""
        return len(self.items)


# Пример использования
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())  # 3
    print(stack.peek())  # 2
    print(stack.size())  # 2
