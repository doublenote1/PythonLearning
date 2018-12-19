"""
■ 数値のリストを文字列のリストに変換
    ・数値を2進数、8進数、16進数の文字列に変換
    ・数値を指数表記の文字列に変換
■ 文字列のリストを数値のリストに変換
    ・2進数、8進数、16進数表記の文字列を数値に変換
    ・指数表記の文字列を数値に変換
    ・数値に変換できる文字列のみ変換
"""

# ****** 文字列のリストへ変換 ******

# === 数値のリストを文字列のリストに変換 ===

"""
・数値から文字列への変換はstr()関数を使う
・Pythonでは数値を指数表記や16進数、2進数など様々な形式で表現できるが、
  str() で変換した場合は通常の10進表記の文字列となる。
・桁数によっては自動的に指数表記となる場合もある。
"""
l_n = [-0.5, 0, 1.0, 100, 1.2e-2, 0xff, 0b11]
print([str(n) for n in l_n])
print()

# === 数値を2進数、8進数、16進数の文字列に変換 ===

"""
2進数、8進数、16進数の文字列に変換する場合は、
bin() や oct(), hex() 関数を使うか、
format() 関数（または文字列 str の format() メソッド）を使う
"""

l_i = [0, 64, 128, 192, 256]

print([bin(i) for i in l_i])
print([oct(i) for i in l_i])
print([hex(i) for i in l_i])
print()

print([format(i, '#011b') for i in l_i])
print([format(i, '#05o') for i in l_i])
print([format(i, '#06x') for i in l_i])
print()

# === 数値を指数表記の文字列に変換 ===

l_f = [0.0001, 123.456, 123400000]

print([format(f, 'e') for f in l_f])
print([format(f, '.3E') for f in l_f])
print()

# ****** 数値へ変換 ******

# === 文字列のリストを数値のリストに変換 ===

l_si = ['-10', '0', '100']
print([int(s) for s in l_si])

l_sf = ['.123', '1.23', '123']
print([float(s) for s in l_sf])
print()

# === 2進数、8進数、16進数表記の文字列を数値に変換 ===

"""
・int() 関数の第二引数には基数を指定できる
・2なら2進数、8なら8進数、16なら16進数として文字列を数値に変換する
・0を指定すると、0bや0o, 0xのプレフィックスが付いた文字列を
  それぞれ 2進数、8進数、16進数として整数に変換する
"""

l_sb = ['0011', '0101', '1111']
print([int(s, 2) for s in l_sb])
l_so = ['10', '100', '1000']
print([int(s, 8) for s in l_so])
l_sx = ['10', '100', '1000']
print([int(s, 16) for s in l_sx])
print()

l_sbox = ['100', '0b100', '0o100', '0x100']
print([int(s, 0) for s in l_sbox])
print()

# === 指数表記の文字列を数値に変換 ===

l_se = ['1.23e3', '0.123e-1', '123']
print([float(s) for s in l_se])
print()

# === 数値に変換できる文字列のみ変換 ===

def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True

def is_float(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

l_multi = ['-100', '100', '1.23', '1.23e2', 'one']

print([int(s) for s in l_multi if is_int(s)])
print([float(s) for s in l_multi if is_float(s)])
