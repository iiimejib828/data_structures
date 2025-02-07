class TreeNode:
    def __init__(self, value):
        """Инициализация узла бинарного дерева."""
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        """Инициализация пустого бинарного дерева."""
        self.root = None

    def insert(self, value):
        """Вставка нового значения в бинарное дерево."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        """Рекурсивная вставка в дерево."""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def delete(self, value):
        """Удаление узла с заданным значением."""
        self.root = self._delete_recursively(self.root, value)

    def _delete_recursively(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursively(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursively(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursively(node.right, min_larger_node.value)

        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder_traversal(self, node, result=None):
        """Обход дерева в порядке in-order (Левый-Корень-Правый)."""
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result


# Пример использования
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)

    print(tree.inorder_traversal(tree.root))  # [2, 3, 4, 5, 6, 7, 8]

    tree.delete(5)
    print(tree.inorder_traversal(tree.root))  # [2, 3, 4, 6, 7, 8]
