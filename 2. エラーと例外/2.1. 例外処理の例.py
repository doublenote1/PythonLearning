import os
import re
import sys


class MyError(Exception):
    pass


class Over4DigitsError(MyError):
    pass


def div_and_write(div_num1, div_num2, file=None):
    global success_count, total_count
    total_count += 1
    exp = str(div_num1) + ' / ' + str(div_num2) + ' = '
    err_msg = 'success!'
    result = '???'
    try:
        div_num1 = float(div_num1)
        div_num2 = float(div_num2)
        result = str(div_num1 / div_num2)
        # 第一引数か第二引数が４桁以上ならエラー
        if div_num1 >= 10000 or div_num2 >= 10000:
            raise Over4DigitsError('Over 4 digits')
        # 第三引数が指定されていれば、ファイルに結果を出力する
        if file is not None:
            # 第三引数がファイル名の書式になっていなければ、エラー起動
            if re.match(r'^[a-zA-Z][a-zA-Z0-9]*\.([a-z]+|[A-Z]+)$', file):
                with open(file, 'x') as f:
                    f.write(str(result))
            else:
                raise NameError('Invalid file name')
    # 想定できるエラーの種類を列挙
    except Over4DigitsError as e:
        err_msg = 'Over4DigitsError: ' + str(e)
    except (ZeroDivisionError, ValueError) as e:
        err_msg = 'ZeroDivisionError or ValueError: ' + str(e)
    except FileExistsError as e:
        err_msg = 'FileExistsError: ' + str(e)
    except NameError as e:
        err_msg = 'NameError: ' + str(e)
    # 想定外のエラーが起きた時の処理(Exception)
    except Exception as e:
        err_msg = ''
        err_msg += 'ERROR: Unexpected' + '\n'
        err_msg += '\t' + str(type(e)) + '\n'
        err_msg += '\t' + str(e.args) + '\n'
        err_msg += '\t' + str(e.args[0]) + '\n'
        err_msg += '\t' + str(e) + '\n'
        err_msg += '\n'
        err_msg += '\t' + str(sys.exc_info()) + '\n'
        err_msg += '\t' + str(sys.exc_info()[0]) + '\n'
        err_msg += '\t' + str(sys.exc_info()[1]) + '\n'
        err_msg += '\t' + str(sys.exc_info()[2])
    else:
        success_count += 1
    finally:
        print(exp + result)
        print(err_msg)
        print()


def trim_err(e):
    return str(type(e)).replace('<class \'', '').replace('\'>', '')


path = 'test.txt'
invalid_path = 'test'
total_count = 0
success_count = 0

# === 正常実行 ===

div_and_write(6, 2)
# -> 6 / 2 = 3.0
# -> success!

div_and_write(6.134, 2.345)
# -> 6.134 / 2.345 = 2.615778251599147
# -> success!

div_and_write('１', '２')
# -> １ / ２ = 0.5
# -> success!

div_and_write(1, 2, path)
# -> 1 / 2 = 0.5
# -> success!

# === エラー発生 ===

div_and_write(1, 0)
# -> 1 / 0 = ???
# -> ZeroDivisionError or ValueError: float division by zero

div_and_write('one', 'two')
# -> one / two = ???
# -> ZeroDivisionError or ValueError: could not convert string to float: 'one'

div_and_write(50000, 5)
# -> 50000 / 5 = 10000.0
# -> Over4DigitsError: Over 4 digits

div_and_write(30, 20, path)
# -> 30 / 20 = 1.5
# -> FileExistsError: [Errno 17] File exists: 'test.txt'

div_and_write(50, 20, invalid_path)
# -> 50 / 20 = 2.5
# -> NameError: Invalid file name

div_and_write(100, 20, True)
# -> 100 / 20 = 5.0
# -> ERROR: Unexpected
# ->    str(type(e)) = <class 'TypeError'>
# ->    str(e.args) = ('expected string or bytes-like object',)
# ->    str(e.args[0]) = expected string or bytes-like object
# ->    str(e) = expected string or bytes-like object

# ->    str(sys.exc_info()) = (<class 'TypeError'>, TypeError('expected string or bytes-like object'), <traceback object at 0x000000000394F548>)
# ->    str(sys.exc_info()[0]) = <class 'TypeError'>
# ->    str(sys.exc_info()[1]) = expected string or bytes-like object
# ->    str(sys.exc_info()[2]) = <traceback object at 0x000000000394F548>

print('- Succeeded ' + str(success_count) + ' times. -')
# -> - Succeeded 4 times. -
print('- Became an error ' + str(total_count - success_count) + ' times. -')
# -> - Became an error 6 times. -
os.remove(path)
