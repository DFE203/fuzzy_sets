class RuleInference:
    @staticmethod
    def modus_ponens(implication_matrix, fuzzy_set):
        """
        Применение правила Modus Ponens для нечетких множеств.
        :param implication_matrix: Матрица импликаций (отношений).
        :param fuzzy_set: Нечеткое множество фактов (множество условий).
        :return: Нечеткое множество вывода (conclusion set).
        """
        conclusion_set = {}

        # Для каждого элемента во втором множестве (последствия), находим максимальное значение
        for j in range(len(implication_matrix[0])):
            max_value = 0
            for i in range(len(fuzzy_set.elements)):
                max_value = max(max_value, min(fuzzy_set.elements[f"element_{i + 1}"], implication_matrix[i][j]))
            conclusion_set[f"conclusion_{j + 1}"] = max_value

        return conclusion_set

    @staticmethod
    def modus_tollens(implication_matrix, fuzzy_set):
        """
        Применение правила Modus Tollens для нечетких множеств.
        :param implication_matrix: Матрица импликаций (отношений).
        :param fuzzy_set: Нечеткое множество фактов (множество последствий).
        :return: Нечеткое множество вывода (условий).
        """
        conclusion_set = {}

        # Для каждого элемента в первом множестве (условие), находим максимальное значение
        for i in range(len(implication_matrix)):
            max_value = 0
            for j in range(len(fuzzy_set.elements)):
                max_value = max(max_value, min(fuzzy_set.elements[f"element_{j + 1}"], implication_matrix[i][j]))
            conclusion_set[f"condition_{i + 1}"] = max_value

        return conclusion_set
