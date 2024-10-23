import numpy as np


class RelationMatrix:
    def __init__(self, fuzzy_set1, fuzzy_set2):
        """
        Инициализация матрицы отношений между двумя нечеткими множествами.
        :param fuzzy_set1: Объект класса FuzzySet
        :param fuzzy_set2: Объект класса FuzzySet
        """
        self.fuzzy_set1 = fuzzy_set1
        self.fuzzy_set2 = fuzzy_set2
        self.matrix = self._create_relation_matrix()

    def _create_relation_matrix(self):
        """
        Создание матрицы отношений на основе пересечения элементов двух нечетких множеств.
        :return: Матрица отношений (numpy.ndarray)
        """
        elements1 = list(self.fuzzy_set1.elements.keys())
        elements2 = list(self.fuzzy_set2.elements.keys())

        matrix = np.zeros((len(elements1), len(elements2)))

        # Заполняем матрицу минимумами степеней принадлежности
        for i, e1 in enumerate(elements1):
            for j, e2 in enumerate(elements2):
                value1 = self.fuzzy_set1.elements.get(e1, 0)
                value2 = self.fuzzy_set2.elements.get(e2, 0)
                matrix[i][j] = min(value1, value2)

        return matrix

    def print_matrix(self):
        """
        Печатает матрицу отношений в удобочитаемом формате.
        """
        print("Матрица отношений:")
        print(self.matrix)

    def transpose(self):
        """
        Транспонирует матрицу отношений.
        :return: Транспонированная матрица (numpy.ndarray)
        """
        return np.transpose(self.matrix)

    def fold(self):
        """
        Сворачивает матрицу отношений (получение новых правил на основе текущей матрицы).
        :return: Свернутая матрица (numpy.ndarray)
        """
        # Простая свертка - нахождение максимальных значений в строках
        folded_matrix = np.max(self.matrix, axis=1)
        return folded_matrix
