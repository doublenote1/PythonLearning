from user import print_newline as print_newline
from user import print_serial as print_serial

# ====== イテレータ ======

l = [
    'おはよう',
    'こんにちわ',
    'こんばんわ',
]

# イテレータ作成
i = iter(l)
print(type(i))

# イテレート実行
print(next(i))  # next() 関数
print(i.__next__())  # __next__ メソッド
print(next(i))
try:
    print(i.__next__())
except StopIteration:
    print('Run out of iteration !')

# ループ処理
i = iter(l)
for text in i:
    print_serial(text)
print()
print()

# ====== ジェネレータ ======

# --- ジェネレータ(有限) ---

# ジェネレータ関数を定義
def func_gen():
    yield 'おはよう'
    yield 'こんにちは'
    yield 'こんばんわ'

# ジェネレータを生成する
gen = func_gen()
print(type(gen))

# イテレート実行
while True:
    try:
        print(gen.__next__())
    except StopIteration:
        print('Run out of iteration !')
        break

# ループ処理
gen = func_gen()
for text in gen:
    print_serial(text)
print()
print()

# --- ジェネレータ(無限) ---

# Sample 1

def func_gen_fibo():
    f0, f1 = 0, 1
    while True:
        yield f0
        f0, f1 = f1, f0 + f1

gen = func_gen_fibo()  # ジェネレータオブジェクトを生成する

for i in range(15):  # 15回イテレートする
    num = next(gen)
    print_serial(num)
print()
print()

# Sample2

def quiz(word):
    hint = ""
    for letter in word:
        hint += letter
        yield hint

ans = 'Python'
quiz = quiz(ans)
while True:
    try:
        hint = next(quiz)
        print(hint)
        print('Python')
        word = 'Python'
        if ans.lower() == word.lower():
            point = len(ans) - len(hint)
            print(f"正解。得点は{point}です。")
            break
        else:
            print("間違い\n")
    except:
        print("終了です。0点です。")
        break
print()

# ====== その他 ======

# --- send() ---

def func_gen_counter():
    n = 0
    while True:
        received = yield n
        if received is not None:
            n = received
        else:
            n = n + 1

gen = func_gen_counter()

for text in range(3):
    print_serial(next(gen))
print_newline(gen.send(10))
for text in range(4):
    print_serial(next(gen))
print_newline(gen.send(2))
for text in range(4):
    print_serial(next(gen))
print()
print()

# --- ジェネレータ内包表記 ---

def func_gen_sample():
    for i in range(5):
        yield i ** 2

gen = func_gen_sample()
print(list(gen))

gen = (i ** 2 for i in range(5))
print(list(gen))
print()

# --- サブジェネレータ ---

def gen_1():
    for i in range(4):
        yield i ** 2

def gen_2():
    for i in range(100, 104):
        yield i ** 2

def gen_wrapper(gen_func1, gen_func2):
    yield from gen_func1
    yield from gen_func2

gen = gen_wrapper(gen_1(), gen_2())

print(list(gen))
print()

# --- class としての、イテレータ ---

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')

print(''.join([i for i in rev]))

