# === 名前空間とは？ ===

# 名前空間: 変数や関数が所属している領域(関数)

# スコープ: 変数や関数が有効である範囲
# ビルトインスコープ: 組込変数や関数の有効範囲
# モジュールスコープ(グローバルスコープ): python スクリプトファイル内のトップレベルで定義した時の有効範囲
# ローカルスコープ: 関数・クラス内を有効範囲とするスコープ

# 参照の順番:
# 1. L: Local
# 2. E: Enclosing function local
# 3. G: Global
# 4. B: Built-in


def a():
    # 関数a内部の名前空間
    l = 0
    s = 'apple'

    def b():
        # 関数b内部の名前空間
        m = 1
        t = 'banana'
        print(dir())
        print(globals().keys())

    print(dir())
    b()


# globalの名前空間

n = 2
u = 'cake'

a()
# ['b', 'l', 's']
# ['m', 't']
# dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'a', 'n', 'u'])

print(globals().keys())
# dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'a', 'n', 'u'])


# === 明示的なScopeの指定 ===

spam = 0


def a():
    # globalを変更しようとしても、localに新しく変数ができてしまう
    spam = 1


a()
print(spam)  # -> 0


def b():
    # globalを指定すれば、globalの変数に代入することが可能
    global spam
    spam = 1


b()
print(spam)  # -> 1

spam = 0


def a():
    spam = 1

    def b():
        # global を指定することで、通常優先度が高いnonlocalではなくglobalの変数を使うことができる
        global spam
        return spam

    return b()


print(a())  # -> 0


# Python チュートリアルより

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam

print("In global scope:", spam)
# -> In global scope: global spam
