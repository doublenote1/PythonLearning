def func_1():
    print('mod_1.func1')


def func_2():
    print('mod_1.func2')


def func_3(text):
    print(text)


# このファイルが直接実行された時の処理

if __name__ == '__main__':
    func_3('mod1.main')
