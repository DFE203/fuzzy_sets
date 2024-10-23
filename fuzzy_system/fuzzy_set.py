class FuzzySet:
    def __init__(self, elements: dict):
        """
        elements: dict, где ключ — элемент множества, значение — степень принадлежности (от 0 до 1)
        """
        self.elements = elements

    def intersection(self, other):
        """Возвращает пересечение с другим нечетким множеством"""
        return FuzzySet({k: min(self.elements.get(k, 0), other.elements.get(k, 0)) for k in self.elements})

    def complement(self):
        """Возвращает дополнение множества"""
        return FuzzySet({k: 1 - v for k, v in self.elements.items()})
