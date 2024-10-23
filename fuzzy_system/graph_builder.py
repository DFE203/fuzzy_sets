import matplotlib.pyplot as plt
import networkx as nx


class GraphBuilder:
    def __init__(self, matrix, labels1, labels2):
        """
        Инициализация графа на основе матрицы отношений.
        :param matrix: Матрица отношений (numpy.ndarray или список списков)
        :param labels1: Метки для вершин (множество 1)
        :param labels2: Метки для вершин (множество 2)
        """
        self.matrix = matrix
        self.labels1 = labels1  # Метки для множества 1
        self.labels2 = labels2  # Метки для множества 2
        self.graph = nx.Graph()

    def build_graph(self):
        """
        Создает граф на основе матрицы отношений и добавляет ребра между элементами.
        """
        # Добавляем вершины для первого множества
        for i, label1 in enumerate(self.labels1):
            self.graph.add_node(label1, bipartite=0)

        # Добавляем вершины для второго множества
        for j, label2 in enumerate(self.labels2):
            self.graph.add_node(label2, bipartite=1)

        # Добавляем ребра на основе значений матрицы
        for i, label1 in enumerate(self.labels1):
            for j, label2 in enumerate(self.labels2):
                weight = self.matrix[i][j]
                if weight > 0:  # Только для ненулевых весов
                    self.graph.add_edge(label1, label2, weight=weight)

    def draw_graph(self):
        """
        Визуализирует граф с использованием networkx и matplotlib.
        """
        pos = nx.spring_layout(self.graph)  # Расположение вершин графа

        # Рисуем вершины и ребра
        nx.draw(self.graph, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10,
                font_weight='bold')

        # Рисуем веса на рёбрах
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)

        plt.title("Граф продукционных отношений")
        plt.show()

    def save_graph(self, file_path):
        """
        Сохраняет граф в виде изображения.
        :param file_path: Путь для сохранения изображения графа.
        """
        pos = nx.spring_layout(self.graph)
        plt.figure(figsize=(8, 8))
        nx.draw(self.graph, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10,
                font_weight='bold')
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.title("Граф продукционных отношений")
        plt.savefig(file_path)
        print(f"Граф сохранен как {file_path}")
