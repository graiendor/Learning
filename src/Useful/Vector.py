from typing import List
from math import sqrt

Vector = List[float]


def __add_drive(vector_1: Vector, vector_2: Vector, sign: int) -> Vector:
    """Собственно движок сложения"""
    assert len(vector_1) == len(vector_2), "Must have the same length"
    return [v_i + (w_i * sign) for v_i, w_i in zip(vector_1, vector_2)]


def add(vector_1: Vector, vector_2: Vector) -> Vector:
    """Сложение двух векторов"""
    return __add_drive(vector_1, vector_2, 1)


def subtract(vector_1: Vector, vector_2: Vector) -> Vector:
    """Вычитание двух векторов"""
    return __add_drive(vector_1, vector_2, 1)


def vectors_sum(vectors: List[Vector]) -> Vector:
    """Покомпонентная сумма списка векторов.
    Суммирует все соответствующие элементы"""
    assert vectors, "No vectors"

    number_of_elements = len(vectors[0])
    assert all(len(vector) == number_of_elements for vector in vectors), "All vectors must have the same length"

    return [sum(vector[i] for vector in vectors) for i in range(number_of_elements)]


def on_scalar_multiply(vector: Vector, number: float) -> Vector:
    """Умножает каждый элемент на число"""
    return [number * v_i for v_i in vector]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Вычисляет поэлементное среднее арифметическое"""
    length = len(vectors)
    return on_scalar_multiply(vectors_sum(vectors), 1 / length)


def scalar_multiply(vector_1: Vector, vector_2: Vector) -> float:
    """Скалярное произведение. Вычисляет сумму перемножений"""
    assert len(vector_1) == len(vector_2)

    return sum(vector_1_element * vector_2_element for vector_1_element, vector_2_element in zip(vector_1, vector_2))


def squares_sum(vector: Vector) -> float:
    """Вычисляет сумму квадратов каждого элемента"""
    return scalar_multiply(vector, vector)


def magnitude(vector: Vector) -> float:
    """Вычисляет магнитуду (или длину) вектора"""
    return sqrt(squares_sum(vector))


def squared_distance(vector_1: Vector, vector_2: Vector) -> float:
    """Вычисляет квадрат расстояния между двумя векторами"""
    return squares_sum(subtract(vector_1, vector_2))


def distance(vector_1: Vector, vector_2: Vector) -> float:
    """Вычисляет расстояние между двумя векторами"""
    return magnitude(subtract(vector_1, vector_2))


if __name__ == '__main__':
    assert vectors_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]
    assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]
    assert scalar_multiply([1, 2, 3], [4, 5, 6]) == 32
    assert squares_sum([1, 2, 3]) == 14

