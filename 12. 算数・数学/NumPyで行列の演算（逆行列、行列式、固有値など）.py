行列オブジェクトの生成: Pythonリスト、numpy.array(), numpy.matrix()
Pythonのリスト型

リストの要素としてリストを指定すれば二次元の配列となる。

import numpy as np

l_2d = [[0, 1, 2], [3, 4, 5]]

print(l_2d)
print(type(l_2d))
# [[0, 1, 2], [3, 4, 5]]
# <class 'list'>

source: numpy_matrix_ndarray_list.py
NumPy配列numpy.ndarray: numpy.array()

NumPy配列numpy.ndarrayはnumpy.array()で生成できる。

numpy.array — NumPy v1.13 Manual

第一引数にPythonのリストなどを渡す。

arr = np.array([[0, 1, 2], [3, 4, 5]])

print(arr)
print(type(arr))
# [[0 1 2]
#  [3 4 5]]
# <class 'numpy.ndarray'>

source: numpy_matrix_ndarray_list.py

numpy.array()のほかには等差数列を生成する関数np.arange()などでもndarrayを生成できる。さらにreshape()メソッドで形状を変更したりすることも可能。

arr = np.arange(6)

print(arr)
# [0 1 2 3 4 5]

arr = np.arange(6).reshape((2, 3))

print(arr)
# [[0 1 2]
#  [3 4 5]]

source: numpy_matrix_ndarray_list.py

そのほか、任意の形状を同じ値で初期化するnumpy.zeros(), numpy.ones(), numpy.full()などもある。

関連記事: NumPyで全要素を同じ値で初期化した配列ndarrayを生成

NumPy行列numpy.matrix: numpy.matrix()

NumPy行列numpy.matrixはコンストラクタnumpy.matrix()で生成できる。

numpy.matrix — NumPy v1.13 Manual

第一引数にPythonのリストやNumPy配列ndarrayなどを渡す。

mat = np.matrix([[0, 1, 2], [3, 4, 5]])

print(mat)
print(type(mat))
# [[0 1 2]
#  [3 4 5]]
# <class 'numpy.matrixlib.defmatrix.matrix'>

mat = np.matrix(arr)

print(mat)
print(type(mat))
# [[0 1 2]
#  [3 4 5]]
# <class 'numpy.matrixlib.defmatrix.matrix'>

source: numpy_matrix_ndarray_list.py

上述のように、NumPy行列numpy.matrixは行列（二次元配列）に特化したクラス。

コンストラクタの引数に一次元配列を渡すと二次元に拡張され、三次元以上の配列を渡すとエラーになる。

mat_1d = np.matrix([0, 1, 2])

print(mat_1d)
print(type(mat_1d))
print(mat_1d.shape)
# [[0 1 2]]
# <class 'numpy.matrixlib.defmatrix.matrix'>
# (1, 3)

# mat_3d = np.matrix([[[0, 1, 2]]])
# ValueError: matrix must be 2-dimensional

source: numpy_matrix_ndarray_list.py
行列の要素の取得と変更（代入）

Pythonリスト型の二次元配列の要素の値はlist[行番号][列番号]でアクセスできる。行番号・列番号は0始まり。値を取得することも、変更（代入）することもできる。

print(l_2d[0][1])
# 1

l_2d[0][1] = 100

print(l_2d)
# [[0, 100, 2], [3, 4, 5]]

source: numpy_matrix_ndarray_list.py

numpy.ndarray, numpy.matrixは、arr[行番号][列番号]またはarr[行番号, 列番号]でアクセスできる。行番号・列番号は0始まり。値を取得することも、変更（代入）することもできる。

以下の例はndarrayだが、matrixでも同様。

print(arr[0][1])
# 1

print(arr[0, 1])
# 1

arr[0, 1] = 100

print(arr)
# [[  0 100   2]
#  [  3   4   5]]

source: numpy_matrix_ndarray_list.py
転置行列: .T属性

Pythonリスト型の二次元配列の転置行列は以下のように取得できる。

l_2d = [[0, 1, 2], [3, 4, 5]]

print(l_2d)
# [[0, 1, 2], [3, 4, 5]]

l_2d_t = [list(x) for x in list(zip(*l_2d))]
print(l_2d_t)
# [[0, 3], [1, 4], [2, 5]]

source: numpy_matrix_ndarray_list.py

処理の詳細は以下の記事を参照。

関連記事: Pythonリスト型の二次元配列の行と列を入れ替える（転置）

numpy.ndarrayとnumpy.matrixは.Tで転置行列を取得できる。

以下の例はndarrayだが、matrixでも同様。

arr = np.arange(6).reshape((2, 3))

print(arr)
# [[0 1 2]
#  [3 4 5]]

arr_t = arr.T

print(arr_t)
# [[0 3]
#  [1 4]
#  [2 5]]

source: numpy_matrix_ndarray_list.py
行列の和と差: +演算子, -演算子

Pythonリスト型では、+演算子はリストの結合となり、-演算子に対する処理は定義されていないためエラーTypeErrorになる。

l_2d_1 = [[0, 1, 2], [3, 4, 5]]
l_2d_2 = [[0, 2, 4], [6, 8, 10]]

l_2d_sum = l_2d_1 + l_2d_2

print(l_2d_sum)
# [[0, 1, 2], [3, 4, 5], [0, 2, 4], [6, 8, 10]]

# l_2d_sub = l_2d_1 - l_2d_2
# TypeError: unsupported operand type(s) for -: 'list' and 'list'

source: numpy_matrix_ndarray_list.py

numpy.ndarrayとnumpy.matrixでは、+演算子と-演算子で各要素がそれぞれ加算・減算される。

arr1 = np.arange(6).reshape((2, 3))

print(arr1)
# [[0 1 2]
#  [3 4 5]]

arr2 = np.arange(0, 12, 2).reshape((2, 3))

print(arr2)
# [[ 0  2  4]
#  [ 6  8 10]]

arr_sum = arr1 + arr2

print(arr_sum)
# [[ 0  3  6]
#  [ 9 12 15]]

arr_sub = arr1 - arr2

print(arr_sub)
# [[ 0 -1 -2]
#  [-3 -4 -5]]

mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)

mat_sum = mat1 + mat2

print(mat_sum)
# [[ 0  3  6]
#  [ 9 12 15]]

mat_sub = mat1 - mat2

print(mat_sub)
# [[ 0 -1 -2]
#  [-3 -4 -5]]

source: numpy_matrix_ndarray_list.py
スカラー倍と要素ごとの積: *演算子, numpy.multiply()

Pythonリスト型では、数値との*演算は配列の繰り返しとなり、リスト同士の*演算は定義されていないためエラーになる。

l_2d_mul = l_2d_1 * 2

print(l_2d_mul)
# [[0, 1, 2], [3, 4, 5], [0, 1, 2], [3, 4, 5]]

# l_2d_mul = l_2d_1 * l_2d_2
# TypeError: can't multiply sequence by non-int of type 'list'

source: numpy_matrix_ndarray_list.py

numpy.ndarrayとnumpy.matrixでは、数値との*演算は各要素のスカラー倍となる。

arr_mul = arr1 * 2

print(arr_mul)
# [[ 0  2  4]
#  [ 6  8 10]]

mat_mul = mat1 * 2

print(mat_mul)
# [[ 0  2  4]
#  [ 6  8 10]]

source: numpy_matrix_ndarray_list.py

行列同士の要素ごとの積（アダマール積）を取得するには、numpy.multiply()を使う。

numpy.multiply — NumPy v1.13 Manual

arr_mul = np.multiply(arr1, arr2)

print(arr_mul)
# [[ 0  2  8]
#  [18 32 50]]

mat_mul = np.multiply(mat1, mat2)

print(mat_mul)
# [[ 0  2  8]
#  [18 32 50]]

source: numpy_matrix_ndarray_list.py

numpy.ndarrayでは、*演算子はnumpy.multiply()と等価で、要素ごとの積算になる。

arr_mul = arr1 * arr2

print(arr_mul)
# [[ 0  2  8]
#  [18 32 50]]

source: numpy_matrix_ndarray_list.py

numpy.matrixでは、*演算子は行列の積になる（後述）。
行列の積: numpy.dot(), numpy.matmul(), @演算子, *演算子

行列の積を算出するには、numpy.dot(), numpy.matmul(), @演算子を使う。

numpy.dot — NumPy v1.14 Manual
numpy.matmul — NumPy v1.14 Manual

@演算子はPython3.5, NumPy1.10.0以降で利用可能で、numpy.matmul()と等価。

numpy.dot(), numpy.matmul()は三次元以上の多次元配列での処理が異なるがここでは深追いしない。行列（二次元配列）に対しては同じ結果となる。

dot()は関数だけでなくメソッドとしても用意されている。

arr1 = np.arange(4).reshape((2, 2))

print(arr1)
# [[0 1]
#  [2 3]]

arr2 = np.arange(6).reshape((2, 3))

print(arr2)
# [[0 1 2]
#  [3 4 5]]

arr_mul_matrix = np.dot(arr1, arr2)

print(arr_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

arr_mul_matrix = arr1.dot(arr2)

print(arr_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

arr_mul_matrix = np.matmul(arr1, arr2)

print(arr_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

arr_mul_matrix = arr1 @ arr2

print(arr_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)

mat_mul_matrix = np.dot(mat1, mat2)

print(mat_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

mat_mul_matrix = mat1.dot(mat2)

print(mat_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

mat_mul_matrix = np.matmul(mat1, mat2)

print(mat_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

mat_mul_matrix = mat1 @ mat2

print(mat_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

source: numpy_matrix_ndarray_list.py

numpy.matrixでは、*演算子でも行列の積が算出される。

mat_mul_matrix = mat1 * mat2

print(mat_mul_matrix)
# [[ 3  4  5]
#  [ 9 14 19]]

source: numpy_matrix_ndarray_list.py
べき乗: **演算子

上述のように、numpy.ndarrayとnumpy.matrixでは*演算子に対する振る舞いが異なるため、べき乗**演算子に対する結果も異なる。

numpy.ndarrayでは各要素に対してべき乗処理が行われ、numpy.matrixでは行列の積が繰り返される。

arr = np.arange(1, 5).reshape(2, 2)

print(arr)
# [[1 2]
#  [3 4]]

arr_p = arr**2

print(arr_p)
# [[ 1  4]
#  [ 9 16]]

mat = np.matrix(arr)

print(mat)
# [[1 2]
#  [3 4]]

mat_p = mat**2

print(mat_p)
# [[ 7 10]
#  [15 22]]

print(mat**2 == mat * mat)
# [[ True  True]
#  [ True  True]]

print(mat**3 == mat * mat * mat)
# [[ True  True]
#  [ True  True]]

source: numpy_matrix_ndarray_list.py

負の値のべき乗についてもnumpy.ndarrayでは各要素に対してべき乗処理が行われる。このとき、元の配列のデータ型dtypeがintだとエラーになる。あらかじめデータ型をfloatにしておけばOK。

# arr_n = arr**-1
# ValueError: Integers to negative integer powers are not allowed.

arr_f = np.array(arr, dtype=float)

arr_f_n = arr_f**-1

print(arr_f_n)
# [[1.         0.5       ]
#  [0.33333333 0.25      ]]

source: numpy_matrix_ndarray_list.py

numpy.matrixに対する**-1は逆行列の演算になる。負の値のべき乗は逆行列の積の繰り返しになる。

mat_inv = mat**-1

print(mat_inv)
# [[-2.   1. ]
#  [ 1.5 -0.5]]

mat_inv2 = mat**-2

print(mat_inv2)
# [[ 5.5  -2.5 ]
#  [-3.75  1.75]]

print(mat**-2 == mat**-1 * mat**-1)
# [[ True  True]
#  [ True  True]]

print(mat**-3 == mat**-1 * mat**-1 * mat**-1)
# [[ True  True]
#  [ True  True]]

source: numpy_matrix_ndarray_list.py
ベクトルの内積: numpy.inner()

行列（二次元配列）というテーマからずれるが、ベクトル（一次元配列）の内積を算出するには、numpy.inner()を使う。

numpy.inner — NumPy v1.14 Manual

上述のように、numpy.matrixは行列（二次元配列）に特化したクラスであり、コンストラクタに一次元配列を渡すと二次元配列に拡張するため、ベクトル（一次元配列）を扱う場合はnumpy.ndarrayを用いる。

v1 = np.array([0, 1, 2])
v2 = np.array([3, 4, 5])

inner = np.inner(v1, v2)

print(inner)
# 14

source: numpy_vector_inner.py

numpy.dot(), numpy.matmul()でも引数が一次元配列の場合は内積を返すようになっている。@演算子でも同様。

inner_dot = np.dot(v1, v2)

print(inner_dot)
# 14

inner_matmul = np.matmul(v1, v2)

print(inner_matmul)
# 14

inner_matmul = v1 @ v2

print(inner_matmul)
# 14

source: numpy_vector_inner.py
逆行列: numpy.linalg.inv(), **-1, .I属性

逆行列を算出するには、numpy.linalg.inv()を使う。

numpy.linalg.inv — NumPy v1.14 Manual

arr = np.array([[2, 5], [1, 3]])

arr_inv = np.linalg.inv(arr)

print(arr_inv)
# [[ 3. -5.]
#  [-1.  2.]]

mat = np.matrix([[2, 5], [1, 3]])

mat_inv = np.linalg.inv(mat)

print(mat_inv)
# [[ 3. -5.]
#  [-1.  2.]]

source: numpy_matrix_inv.py

上述のように、numpy.matrixでは、**-1（-1乗）でも逆行列が算出できる。

mat_inv = mat**-1

print(mat_inv)
# [[ 3. -5.]
#  [-1.  2.]]

source: numpy_matrix_inv.py

また、.I属性でも逆行列を取得できる。

mat_inv = mat.I

print(mat_inv)
# [[ 3. -5.]
#  [-1.  2.]]

source: numpy_matrix_inv.py

numpy.matrixでは、行列の積が*演算子で計算できるので、例えば、元の行列と逆行列の積が単位行列になることが以下のような簡単な書き方で確認できる。

result = mat * mat.I

print(result)
# [[1. 0.]
#  [0. 1.]]

source: numpy_matrix_inv.py
行列式: numpy.linalg.det()

行列式を算出するには、numpy.linalg.det()を使う。

numpy.linalg.det — NumPy v1.14 Manual

例はnumpy.ndarrayだが、numpy.matrixでも同様。

arr = np.array([[0, 1], [2, 3]])

det = np.linalg.det(arr)

print(det)
# -2.0

source: numpy_matrix_det.py
固有値と固有ベクトル: numpy.linalg.eig()

固有値と固有ベクトルを算出するには、numpy.linalg.eig()を使う。

numpy.linalg.eig — NumPy v1.14 Manual

n次正方行列に対して、n個の固有値が要素となる一次元配列wと、各列が各々の固有値に対応する固有ベクトルとなる二次元配列vが返る。

i個目の固有値w[i]と、i列目の固有ベクトルv[:, i]が対応している。固有ベクトルは1に規格化した値。

例はnumpy.ndarrayだが、numpy.matrixでも同様。

arr = np.array([[8, 1], [4, 5]])

w, v = np.linalg.eig(arr)

print(w)
# [9. 4.]

print(v)
# [[ 0.70710678 -0.24253563]
#  [ 0.70710678  0.9701425 ]]

print('value: ', w[0])
print('vector: ', v[:, 0] / v[0, 0])
# value:  9.0
# vector:  [1. 1.]

source: numpy_matrix_eig.py

最大固有値を求めたい場合は、最大値のインデックスを返すnumpy.argmax()を使えばよい。

print(w[np.argmax(w)])
print(v[:, np.argmax(w)])
# 9.0
# [0.70710678 0.70710678]

source: numpy_matrix_eig.py

以下のような関数を定義すると、対応する固有値と固有ベクトルのペアのタプルのリストを取得できる。固有ベクトルは1で規格化された値だとよく分からないので、各列の0ではない最も絶対値が小さい値で割っている。

def get_eigenpairs(arr):
    w, v = np.linalg.eig(arr)
    eigenpairs = []

    for i, val in enumerate(w):
        vec = v[:, i] / np.min(np.abs(v[:, i][v[:, i] != 0]))
        eigenpairs.append((val, vec))

    return eigenpairs

eigenpairs = get_eigenpairs(arr)

for val, vec in eigenpairs:
    print('value: {}, vector: {}'.format(val, vec))
# value: 9.0, vector: [1. 1.]
# value: 4.0, vector: [-1.  4.]

source: numpy_matrix_eig.py

3 x 3の例。

arr = np.array([[1, 1, 2], [0, 2, -1], [0, 0, 3]])

eigenpairs = get_eigenpairs(arr)

for val, vec in eigenpairs:
    print('value: {}, vector: {}'.format(val, vec))
# value: 1.0, vector: [1. 0. 0.]
# value: 2.0, vector: [1. 1. 0.]
# value: 3.0, vector: [ 1. -2.  2.]

source: numpy_matrix_eig.py

複素数も扱うことができる。虚数単位はjで表される。

arr = np.array([[3, 2], [-2, 3]])

eigenpairs = get_eigenpairs(arr)

for val, vec in eigenpairs:
    print('value: {}, vector: {}'.format(val, vec))
# value: (3+2.0000000000000004j), vector: [0.-1.j 1.+0.j]
# value: (3-2.0000000000000004j), vector: [0.+1.j 1.-0.j]

source: numpy_matrix_eig.py

Pythonでの複素数の扱いについては以下の記事を参照。

関連記事: Python, complex型で複素数を扱う（絶対値、偏角、極座標変換など）

numpy.ndarrayとnumpy.matrixの違いまとめ

最後に、numpy.ndarrayとnumpy.matrixの違いをまとめておく。
numpy.ndarray 	numpy.matrix
次元数 	任意 	2次元のみ
*演算子 	各要素ごとの積 	行列の積
**演算子 	各要素をべき乗 	行列の積を繰り返す
**-1 	各要素を-1乗 	逆行列
**-n 	各要素を-n乗 	逆行列の積を繰り返す
.I属性 	無い 	逆行列

そのほかの+, -, /演算子はどちらでも各要素ごとの演算となる。

最初に書いたように、行列の積や逆行列を頻繁に計算する場合はmatrixのほうが記述が楽かもしれないが、そうでなければ特にmatrixを使う必要はない。

Python3.5, NumPy1.10.0以降ではndarrayでも@演算子で行列の積が計算できるようになったので、matrixを使うメリットは少なくなった。
