import numpy as np
'''
score = 0
def max_after_zero(x: np.array) -> int:
    """
        Задание: найти максимальный элемент массива среди элементов, которым предшествует ноль

         Вход: np.array([0, 2, 0, 3])
         Выход: 3
         """
    # assert False, 'Не реализовано!'  # Здесь должен быть ваш код
    after_cond_zero = np.where(x[:-1]==0)[0]+1
    sorted_vals = np.sort(x[after_cond_zero])
    return sorted_vals[-1]
assert max_after_zero(np.array([0, 6, 0, 3])) == 6, "Тест 1 провален"
assert max_after_zero(np.array([1, 0, 5, 0, 2])) == 5, "Тест 2 провален"
assert max_after_zero(np.array([0, -1, 0, -5])) == -1, "Тест 3 провален"
assert max_after_zero(np.array([0, 100, 0, 50, 0, 200])) == 200, "Тест 4 провален"
print("Все тесты пройдены!")
'''
# задание 2
'''
def block_matrix(block: np.array) -> np.array:
    """
       Задание: построить блочную матрицу из четырех блоков, где каждый блок представляет собой заданную матрицу

        Вход: np.array([[1, 2], [3, 4]])
        Выход: np.array([[1, 2, 1, 2],
                         [3, 4, 3, 4],
                         [1, 2, 1, 2],
                         [3, 4, 3, 4]])
        """
    return np.tile(block,(2,2))
print(block_matrix(np.array([[1, 2], [4, 5]])))
'''
# 3 задание
'''
def diag_prod(matrix: np.array) -> int:
    """
    Задание: вычислить произведение всех ненулевых диагональных элементов квадратной матрицы

    Вход: np.array([[3, 5, 1, 4],
                    [6, 2, 7, 9],
                    [3, 6, 0, 8],
                    [1, 3, 4, 6]])
    Выход: 36
    """
    diag = np.diag(matrix)
    non_zer = diag[diag != 0]
    return np.prod(non_zer)

matrix = np.array([[3, 5, 1, 4],
                   [6, 2, 7, 9],
                   [3, 6, 0, 8],
                   [1, 3, 4, 6]])
print(diag_prod(matrix))
'''
# задание 4
'''
from typing import Tuple
class StandardScaler:

    def fit(self, X: np.array) -> None:
        self.mean_ = np.mean(X, axis=0)
        self.var_ = np.var(X, axis=0)

    def transform(self, X: np.array) -> np.array:
        sigma = np.sqrt(self.var_)
        return (X - self.mean_) / sigma


matrix = np.array([[1, 4, 4200], [0, 10, 5000], [1, 2, 1000]])

scaler = StandardScaler()
scaler.fit(matrix)

assert np.allclose(
    scaler.mean_,
    np.array([0.66667, 5.3333, 3400])
), 'Тест не пройден. Некорректное значение scaler.mean_'

assert np.allclose(
    scaler.var_,
    np.array([0.22222, 11.5556, 2986666.67])
), 'Тест не пройден. Некорректное значение scaler.var_'

assert np.allclose(
    scaler.transform(matrix),
    np.array([[0.7071, -0.39223, 0.46291],
              [-1.4142, 1.37281, 0.92582],
              [0.7071, -0.98058, -1.38873]])
), 'Тест не пройден. Некорректный результат scaler.transform(matrix)'
'''
#задание 5
import numpy as np


def antiderivative(coefs: np.array, const: float) -> np.array:
    n = len(coefs)
    powers = np.arange(n - 1, -1, -1)
    new_powers = powers + 1
    integrated_coefs = coefs / new_powers
    result = np.zeros(n + 1)
    result[:-1] = integrated_coefs
    result[-1] = const
    return result
