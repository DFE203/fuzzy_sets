import os
import json
from fuzzy_system.fuzzy_set import FuzzySet
from fuzzy_system.relation_matrix import RelationMatrix
from fuzzy_system.graph_builder import GraphBuilder
from fuzzy_system.rule_inference import RuleInference
from fuzzy_system.generate import generate_json


def load_fuzzy_sets(filepath):
    """
    Загружает нечеткие множества из JSON-файла и извлекает метки для графа.
    """
    with open(filepath, 'r') as f:
        data = json.load(f)

    # Преобразуем данные JSON в объекты FuzzySet
    fuzzy_sets = {name: FuzzySet(elements) for name, elements in data["fuzzy_sets"].items()}

    # Извлекаем метки для графа
    labels1 = list(data["fuzzy_sets"]["set1"].keys())
    labels2 = list(data["fuzzy_sets"]["set2"].keys())

    return fuzzy_sets, labels1, labels2


def main():
    # Шаг 1: Генерация JSON-файлов с нечеткими множествами
    json_file_path = 'data/generated_fuzzy_sets.json'

    # Проверяем и удаляем файл, если он уже существует, для новой генерации
    if os.path.exists(json_file_path):
        os.remove(json_file_path)

    # Генерация новых данных
    generate_json(json_file_path, num_sets=2, elements_per_set=3)

    # Шаг 2: Загрузка сгенерированных данных и меток
    fuzzy_sets, labels1, labels2 = load_fuzzy_sets(json_file_path)

    set1 = fuzzy_sets['set1']
    set2 = fuzzy_sets['set2']

    # Шаг 3: Построение матрицы отношений
    relation_matrix = RelationMatrix(set1, set2)
    matrix = relation_matrix.matrix

    # Шаг 4: Создание и визуализация графа
    graph_builder = GraphBuilder(matrix, labels1, labels2)
    graph_builder.build_graph()
    graph_builder.draw_graph()

    # Сохранение графа в файл
    graph_builder.save_graph("output_graph.png")

    # Шаг 5: Применение правила Modus Ponens
    modus_ponens_result = RuleInference.modus_ponens(matrix, set1)
    print("\nРезультат Modus Ponens:")
    print(modus_ponens_result)

    # Применение правила Modus Tollens
    modus_tollens_result = RuleInference.modus_tollens(matrix, set2)
    print("\nРезультат Modus Tollens:")
    print(modus_tollens_result)


if __name__ == "__main__":
    main()
