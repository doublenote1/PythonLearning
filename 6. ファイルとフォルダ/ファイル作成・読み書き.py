import os

path = 'existing_file.txt'
output_text = 'line1\nline2\nline3\n'
with open(path, 'w') as f:
    f.write(output_text)

# ****** ファイルを開く ******

"""
open(file, mode='r', buffering=-1, encoding=None, errors=None,
    newline=None, closefd=True, opener=None)
"""

# === with メソッドを使わない方法 ===

f = open(path)
print(type(f))  # -> <class '_io.TextIOWrapper'>
f.close()

# === with メソッドを使う方法 ===

with open(path) as f:
    print(type(f))  # -> <class '_io.TextIOWrapper'>
print()

# ****** 読み込み: mode='r' ******

# === ファイル全体を文字列として読み込み: ===
# read()

with open(path) as f:
    input_text = f.read().strip()
    print(input_text)
    print()
# 代入した変数は with ブロックの外でも使える
print(input_text)
print()

"""存在しないパスを指定するとエラーになる"""
try:
    with open('file_not_exists.txt') as f:
        pass
except FileNotFoundError as e:
    print(e)
print()

# === ファイル全体をリストとして読み込み: ===
# readlines()

with open(path) as f:
    print(f.readlines())

"""改行コードを削除したい場合はリスト内包表記を使って各要素で strip() を適用する"""
with open(path) as f:
    print([x.strip() for x in f.readlines()])
    print()

# === ファイルを一行ずつ読み込み: ===

# --- for文を使う ---

"""ファイルオブジェクトはイテラブル"""
with open(path) as f:
    for line in f:
        print(line.strip())
    print()

# --- readline() を使う ---

with open(path) as f:
    while True:
        line = f.readline().strip()
        print(line)
        if not line:
            break

# ****** 書き込み ******

# === 新規作成・上書き: mode='w' ===

# --- 文字列で、ファイル全体を上書き ---
# write()

with open(path, mode='w') as f:
    f.write('Over Written !!!')

with open(path) as f:
    print(f.read())
    print()

# --- リスト要素を連結して、ファイル全体を上書き ---
# writelines(<文字列を要素とするリスト>)

lst_lines = ['line1', 'line2', 'line3']

with open(path, mode='w') as f:
    f.writelines(lst_lines)

with open(path) as f:
    print(f.read())
    print()

"""
リストの要素ごとに改行して書き込みたい場合は、
改行コードと join() メソッドで改行込みの文字列を作成し、
write() メソッドで書き込む
"""
with open(path, mode='w') as f:
    f.write('\n'.join(lst_lines))

with open(path) as f:
    print(f.read())
    print()

# --- 空の新規ファイルを作成するか、既存ファイルを空にするだけ ---

new_file_name = 'new.txt'
with open(new_file_name, mode="w"):
    pass

os.remove(new_file_name)

# === 新規作成のみ ===

# --- 新規作成専用でファイルオープン: mode='x' ---

def create_new_1(new_path):
    try:
        with open(new_path, mode='x') as f:
            f.write('New File Created !!!')
        with open(new_path) as f:
            print(f.read())
    except FileExistsError as e:
        print(e)

new_file_name = 'new.txt'
create_new_1(new_file_name)
create_new_1(new_file_name)
print()

os.remove(new_file_name)

# --- ファイルが存在しなければオープン ---

def create_new_2(new_path):
    if not os.path.isfile(new_path):
        with open(new_path, mode='w') as f:
            f.write('New File Created !!!')
        with open(new_path) as f:
            print(f.read())
    else:
        print('File does exist !!!')

new_file_name = 'new.txt'
create_new_2(new_file_name)
create_new_2(new_file_name)
print()

os.remove(new_file_name)

# === 上書きのみ ===

def over_write(existing_file_path):
    if os.path.isfile(existing_file_path):
        with open(existing_file_path, mode='w') as f:
            f.write('Overwritten !!!')
        with open(existing_file_path) as f:
            print(f.read())
    else:
        print('File doesn\'t exists !!!')

over_write(path)
over_write('new.txt')
print()

# === 新規作成・追記: mode='a' ===

with open(path, mode='a') as f:
    f.write('\nAppended !!!')

with open(path) as f:
    print(f.read())

os.remove(path)

# === 存在しないフォルダを作成しファイルを新規作成する関数 ===

def save_file_at_new_dir(new_dir_path, new_filename, new_file_content, mode='w'):
    os.makedirs(new_dir_path, exist_ok=True)
    with open(os.path.join(new_dir_path, new_filename), mode) as f:
        f.write(new_file_content)
