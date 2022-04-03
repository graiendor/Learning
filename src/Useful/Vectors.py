from typing import List

Vector = List[float]


def __add_drive(v: Vector, w: Vector, sign: int) -> Vector:
    """Собственно движок сложения"""
    assert len(v) == len(w), "Must have the same length"
    return [v_i + (w_i * sign) for v_i, w_i in zip(v, w)]


def add(v: Vector, w: Vector) -> Vector:
    """Сложение двух векторов"""
    return __add_drive(v, w, 1)


def subtract(v: Vector, w: Vector) -> Vector:
    """Вычитание двух векторов"""
    return __add_drive(v, w, 1)


def vectors_sum(vectors: List[Vector]) -> Vector:
    """Покомпонентная сумма списка векторов.
    Суммирует все соответствующие элементы"""

    assert vectors, "No vectors"

    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "All vectors must have the same length"

    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]
