# === 配列 ===

'''
同じ型しか格納できない
一次元配列のみ
型に制限がある以外はリストと同様の処理が可能
'''

import array

# 'i' = int
arr_int = array.array('i', [0, 1, 2])
print(arr_int)

# 'f' = float
arr_float = array.array('f', [0.0, 0.1, 0.2])
print(arr_float)
print()


# === 多次元配列 - numpy.ndarray ===

import numpy as np

arr = np.array([0, 1, 2])
print(arr)

arr_2d = np.array([[0, 1, 2], [3, 4, 5]])
print(arr_2d)

arr_2d_sqrt = np.sqrt(arr_2d)
print(arr_2d_sqrt)

arr_1 = np.array([[1, 2], [3, 4]])
arr_2 = np.array([[1, 2, 3], [4, 5, 6]])

arr_product = np.dot(arr_1, arr_2)
print(arr_product)
print()
