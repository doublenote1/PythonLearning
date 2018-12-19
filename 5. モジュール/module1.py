def func1():
    print('module1.func1')


def func2():
    print('module1.func2')


def func3(text):
    print(text)


# このファイルが直接実行された時の処理

if __name__ == '__main__':
    func3('Hello!')
