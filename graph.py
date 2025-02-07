class Graph:
    def __init__(self):
        """Инициализация графа с использованием списка смежности."""
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Добавление вершины в граф."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Добавление неориентированного ребра между вершинами."""
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        """Удаление ребра между вершинами."""
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)
            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        """Удаление вершины и всех связанных с ней рёбер."""
        if vertex in self.adjacency_list:
            for adjacent in self.adjacency_list[vertex]:
                self.adjacency_list[adjacent].remove(vertex)
            del self.adjacency_list[vertex]

    def display(self):
        """Вывод списка смежности графа."""
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {edges}")


# Пример использования
if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    graph.display()

    graph.remove_edge("A", "C")
    graph.display()

    graph.remove_vertex("B")
    graph.display()
