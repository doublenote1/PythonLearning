# 要素の取得
squares = [1, 4, 9, 16, 25]
print(squares[0], end=' | ')
print(squares[-1], end=' | ')
print(squares[-3:], end=' | ')
print(squares[:])
print()

# リスト演算
print([1, 2, 3] + [4, 5] * 3)
print()

# 要素の変更
cubes = [1, 8, 27, 65, 125]
print(cubes)
cubes[3] = 4 ** 3
print(cubes)
print()

# 要素の追加
cubes.append(6 ** 3)
cubes.append(7 ** 3)
print(cubes)
print()

# 要素を削除
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del lst[1]
print(lst)
del lst[-2]
print(lst)
del lst[2:3]
print(lst)
del lst[::2]
print(lst)
del lst[:]
print(lst)
print()

# スライスへ代入

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5] = ['C', 'D', 'E']
print(letters)

letters[2:5] = []
print(letters)

letters[:] = []
print(letters)

letters[:] = [1, 2, 3]
print(letters)

# 要素のサイズ取得
print(len(letters))
print()

# 入れ子のリスト
s = ['a', 'b', 'c']
n = [1, 2, 3]
nest = [s, n, 'string', 100]
print('nest =', nest)
print('nest[0] =', nest[0])
print('nest[0][1] =', nest[0][1])
print('nest[2] =', nest[2])
print('size =', len(nest))
