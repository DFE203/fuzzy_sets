import json
import random


def generate_fuzzy_set(elements_count):
    """
    Генерирует нечеткое множество с заданным количеством элементов.
    Каждый элемент имеет случайную степень принадлежности от 0 до 1.
    """
    fuzzy_set = {}
    for i in range(elements_count):
        element_name = f"element_{i + 1}"
        membership_value = round(random.uniform(0, 1), 2)
        fuzzy_set[element_name] = membership_value
    return fuzzy_set


def generate_json(file_path, num_sets=2, elements_per_set=5):
    """
    Генерирует JSON-файл с нечеткими множествами.

    file_path: путь для сохранения файла
    num_sets: количество нечетких множеств
    elements_per_set: количество элементов в каждом множестве
    """
    fuzzy_sets = {}

    for set_num in range(1, num_sets + 1):
        fuzzy_set_name = f"set{set_num}"
        fuzzy_sets[fuzzy_set_name] = generate_fuzzy_set(elements_per_set)

    data = {"fuzzy_sets": fuzzy_sets}

    # Сохранение в файл
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Файл сгенерирован и сохранен как {file_path}")


# Пример использования
generate_json('data/generated_fuzzy_sets.json', num_sets=3, elements_per_set=4)
