from typing import List, Tuple
from math import sqrt
import Vector

Matrix = List[List[float]]


def shape(matrix: Matrix) -> Tuple[int, int]:
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    return number_of_rows, number_of_columns


def get_row(matrix: Matrix, row: int) -> Vector:
    """Возвращает указанную строку как вектор"""
    return matrix[row]


def get_column(matrix: Matrix, column: int) -> Vector:
    """Возвращает указанный столбец как вектор"""
    return [matrix_row[column] for matrix_row in matrix]


def make_matrix(number_of_rows: int, number_of_columns: int, entry_fn: [[int, int], float]) -> Matrix:
    return [[entry_fn(rows, cols) for cols in range(number_of_columns)] for rows in range(number_of_rows)]


if __name__ == "__main__":
    assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)
    assert make_matrix(2, 2, lambda i, j: 1 if i == j else 0) == [[1, 0], [0, 1]]
