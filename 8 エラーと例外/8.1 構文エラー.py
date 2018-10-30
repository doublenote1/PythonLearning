import re
import sys

def div_and_write(div_num1, div_num2, file=None):
    exp = str(div_num1) + ' / ' + str(div_num2) + ' = '
    try:
        result = float(div_num1) / float(div_num2)
        print(exp + str(result))
        if file is not None:
            if re.match(r'^[a-zA-Z][a-zA-Z0-9]*\.([a-z]+|[A-Z]+)$', file):
                with open(file, 'x') as f:
                    f.write(str(result))
            else:
                raise NameError('Invalid file name')
    except FileExistsError:
        print('error: ファイルが存在します')
    except (ZeroDivisionError, ValueError) as e:
        if trim_err(e) == 'ZeroDivisionError':
            print(exp + '???')
            print('error: 第２引数を\'0\'以外の物してください')
        if trim_err(e) == 'ValueError':
            print(exp + '???')
            print('error: 数値を入力してください')
    except Exception as e:
        print('想定外エラー:')
        print('\t' + str(type(e)))
        print('\t' + str(e.args))
        print('\t' + str(e.args[0]))
        print('\t' + str(e))
        print()
        print('\t' + str(sys.exc_info()))
        print('\t' + str(sys.exc_info()[0]))
        print('\t' + str(sys.exc_info()[1]))
        print('\t' + str(sys.exc_info()[2]))
    else:
        print('Success.')
    finally:
        print('done.')
        print()

def trim_err(e):
    return str(type(e)).replace('<class \'', '').replace('\'>', '')

def file_output(file_name):
    with open(file_name) as f:
        print(f.read())

path = 'test.txt'
invalid_path = 'test'

# 正常実行
div_and_write(6, 2)
div_and_write(6.134, 2.345)
div_and_write('１', '２')
div_and_write(1, 2, path)

# エラー発生
div_and_write(1, 0)
div_and_write('one', 'two')
div_and_write(30, 20, path)
div_and_write(30, 20, invalid_path)

import os

os.remove(path)
