import numpy as np
from typing import Tuple


def sum_non_neg_diag(X: np.ndarray) -> int:
    """
    Вернуть  сумму неотрицательных элементов на диагонали прямоугольной матрицы X. 
    Если неотрицательных элементов на диагонали нет, то вернуть -1
    """
    idx = np.diag(X) >= 0
    if ((Y := np.diag(X)[idx]).shape[0]):
        return Y.sum()
    return -1


def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    """
    Проверить, задают ли два вектора одно и то же мультимножество.
    """
    if x.shape[0] != y.shape[0]:
        return False
    return np.all((np.sort(x) == np.sort(y)) == True)


def max_prod_mod_3(x: np.ndarray) -> int:
    """
    Вернуть максимальное прозведение соседних элементов в массиве x, 
    таких что хотя бы один множитель в произведении делится на 3.
    Если таких произведений нет, то вернуть -1.
    """
    y = x[1:] * x[:-1]
    d = y[y % 3 == 0]
    if d.shape[0]:
        return d.max()
    return -1


def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """
    Сложить каналы изображения с указанными весами.
    """
    return (image * weights).sum(axis=2)


def rle_scalar(x: np.ndarray, y: np.ndarray) -> int:
    """
    Найти скалярное произведение между векторами x и y, заданными в формате RLE.
    В случае несовпадения длин векторов вернуть -1.
    """
    new_x = np.repeat(x.T[0], x.T[1])
    new_y = np.repeat(y.T[0], y.T[1])
    if new_x.shape[0] != new_y.shape[0]:
        return -1
    return np.dot(new_x, new_y)


def cosine_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """
    Вычислить матрицу косинусных расстояний между объектами X и Y.
    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
    """
    norm_x = np.linalg.norm(X, axis=1)[:, np.newaxis]
    norm_y = np.linalg.norm(Y, axis=1)[:, np.newaxis]
    d = np.dot(norm_x, norm_y.T)
    result = np.inner(X, Y)
    result[d != 0] = result[d != 0] / d[d != 0]
    result[d == 0] = 1
    return result