from typing import List


def sum_non_neg_diag(X: List[List[int]]) -> int:
    """
    Вернуть  сумму неотрицательных элементов на диагонали прямоугольной матрицы X. 
    Если неотрицательных элементов на диагонали нет, то вернуть -1
    """ 
    sum = 0
    flag = False
    for i in range (min(len(X), len(X[0]))):
        if X[i][i] >= 0:
            sum += X[i][i]
            flag = True
    if flag:
        return sum
    return -1


def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    """
    Проверить, задают ли два вектора одно и то же мультимножество.
    """
    dict_x = dict.fromkeys(x, 0)
    dict_y = dict.fromkeys(y, 0)
    for elem in x:
        dict_x[elem] += 1
    for elem in y:
        dict_y[elem] += 1
    return dict_x == dict_y


def max_prod_mod_3(x: List[int]) -> int:
    """
    Вернуть максимальное прозведение соседних элементов в массиве x, 
    таких что хотя бы один множитель в произведении делится на 3.
    Если таких произведений нет, то вернуть -1.
    """
    cur_prod = 0
    max_prod = 0
    flag = False
    for i in range (len(x) - 1):
        if (cur_prod := x[i] * x[i + 1]) % 3 == 0:
            flag = True
            if cur_prod > max_prod:
                max_prod = cur_prod
    if flag:
        return max_prod
    return -1


def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    """
    Сложить каналы изображения с указанными весами.
    """
    height = len(image)
    width = len(image[0])
    result = [[0] * width for i in range (height)]
    for i in range (height):
        for j in range (width):
            for k in range (len(weights)):
                result[i][j] += image[i][j][k] * weights[k]
    return result


def rle_scalar(x: List[List[int]], y:  List[List[int]]) -> int:
    """
    Найти скалярное произведение между векторами x и y, заданными в формате RLE.
    В случае несовпадения длин векторов вернуть -1.
    """
    new_x = []
    new_y = []
    for pair in x:
        for i in range (pair[1]):
            new_x.append(pair[0])
    for pair in y:
        for i in range (pair[1]):
            new_y.append(pair[0])
    if len(new_x) != len(new_y):
        return -1
    dotprod = 0
    for i in range (len(new_x)):
        dotprod += new_x[i] * new_y[i]
    return dotprod


def cosine_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    """
    Вычислить матрицу косинусных расстояний между объектами X и Y. 
    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
    """
    n = len(X)
    m = len(Y)

    def dot_prod(x, y):
        result = 0
        for i in range (len(x)):
            result += x[i] * y[i]
        return result
    
    output = [[0]*m for i in range (n)]

    for i in range (n):
        for j in range (m):
            len_x = dot_prod(X[i], X[i])
            len_y = dot_prod(Y[j], Y[j])
            if (len_x == 0 or len_y == 0):
                output[i][j] = 1
            else:
                output[i][j] = dot_prod(X[i], Y[j]) / (len_x * len_y)**0.5

    return output