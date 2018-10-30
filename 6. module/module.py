def func1():
    print('func1')


def func2():
    print('func2')


def func3(greeting):
    print(greeting, 'This is module file.')


# このファイルが直接実行された時の処理

if __name__ == '__main__':
    a = 'Hello!'
    func3(a)
