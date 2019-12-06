def a():
    """b関数を呼び出す"""
    b()

def b():
    """c関数を呼び出す"""
    c()

def c():
    """例外が発生する"""
    char = None
    char.format('hello')  # ここで例外発生

# a関数から呼び出してみる
a()
