y = 1
z = 0
try:
    x1 = 1 / y #例外が生じる可能性があると考えているコード
    x2 = 2 / z #想定外の例外
except ZeroDivisionError:
    print('分母がゼロ')
print('プログラムの終了')
