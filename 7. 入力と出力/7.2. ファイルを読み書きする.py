# 準備
import os

read_path = 'open_file.txt'
write_s = 'line1\nline2\nline3\n'
with open(read_path, mode="w") as f:
    f.write(write_s)


# === ファイルを開く ===

print('=== ファイルを開く ===')
print()

f = open(read_path)
print(type(f))
f.close()

# with メソッドを使う
with open(read_path) as f:
    print(type(f))
print()

# === 読み込み ===

print('=== 読み込み ===')
print()

# ファイル全体を文字列として読み込み: read()
with open(read_path) as f:
    read_s = f.read()
    print('-ファイル全体-')
    print()
    print(read_s, end='')
print('※ 代入した変数はwithブロックの外でも使える')
print(read_s)

# ファイル全体をリストとして読み込み: readlines()
with open(read_path) as f:
    read_l = f.readlines()
print('-ファイル全体（リスト形式）-')
print()
print(read_l)
print('※ リスト要素へアクセス')
print(read_l[1])

# ファイルを一行ずつ読み込み: readline()
read_s = ''
with open(read_path) as f:
    read_s += '1回目: ' + f.readline()
    read_s += '2回目: ' + f.readline()
    read_s += '3回目: ' + f.readline()
    read_s += '4回目: ' + f.readline()  # EOF 以降には空文字列''が返される
    read_s += '5回目: ' + f.readline()  # EOF 以降には空文字列''が返される
print('-一行ずつ-')
print()
print(read_s)
print()

# ファイルオブジェクトはイテラブル
read_s = ''
with open(read_path) as f:
    for line in f:
        read_s += line
print('-イテレート可能-')
print()
print(read_s)

os.remove(read_path)

# === 書き込み ===

print('=== 書き込み ===')
print()

# --- 新規作成・上書き ---

# 文字列で、ファイル全体を上書き
write_path = 'write_file.txt'
write_s = 'line1\nline2\nline3\n'
with open(write_path, mode='w') as f:
    f.write(write_s)
with open(write_path) as f:
    read_s = f.read()
print('-文字列を上書き-')
print()
print(read_s)

# リスト要素を連結して、ファイル全体を上書き
write_path_list = 'write_file_list.txt'
write_l = ['line1', 'line2', 'line3']
with open(write_path_list, mode='w') as f:
    f.writelines(', '.join(write_l))
with open(write_path_list) as f:
    read_s = f.read()
print('-リスト要素を連結して上書き-')
print()
print(read_s)
print()

os.remove(write_path_list)

# 空の新規ファイルを作成するか、既存ファイルを空にするだけ
empty_path = 'empty.txt'
with open(empty_path, mode="w"):
    pass

os.remove(empty_path)

# --- 新規作成のみ ---

print('-新規作成のみ-')
print()

new_path = 'new.txt'

def create_new():
    try:
        with open(new_path, mode='x'):
            print('<' + new_path + '> hadn\'t existed, and so created')
    except FileExistsError:
        print('<' + new_path + '> already exists !')

create_new()
create_new()
print()

os.remove(new_path)

# --- 既存ファイルへ上書きのみ ---

print('-既存ファイルへ上書きのみ-')
print()

def over_write():
    if os.path.isfile(new_path):
        with open(new_path, mode='w') as f:
            f.write('This file existed')
            print('<' + new_path + '> existed, and so overwrote !')
    else:
        with open(new_path, 'w'):
            pass
        print('<' + new_path + '> hadn\'t existed')

over_write()
over_write()
print()

os.remove(new_path)

# --- 追記 ---

print('-追記-')
print()

with open(write_path, mode='a') as f:
    f.write('Appended\n')

with open(write_path) as f:
    print(f.read())

os.remove(write_path)


