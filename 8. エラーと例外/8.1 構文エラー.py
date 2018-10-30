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
        if div_num1 >= 10000 or div_num2 >= 10000:
            raise Over4DigitsError('Over 4 digits')
        if file is not None:
            if re.match(r'^[a-zA-Z][a-zA-Z0-9]*\.([a-z]+|[A-Z]+)$', file):
                with open(file, 'x') as f:
                    f.write(str(result))
            else:
                raise NameError('Invalid file name')
    except FileExistsError as e:
        err_msg = 'ERROR: ' + str(e)
    except Over4DigitsError as e:
        err_msg = 'ERROR: ' + str(e)
    except NameError as e:
        err_msg = 'ERROR: ' + str(e)
    except (ZeroDivisionError, ValueError) as e:
        err_msg = 'ERROR: ' + str(e)
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

# 正常実行
div_and_write(6, 2)
div_and_write(6.134, 2.345)
div_and_write('１', '２')
div_and_write(1, 2, path)

# エラー発生
div_and_write(1, 0)
div_and_write('one', 'two')
div_and_write(50000, 5)
div_and_write(30, 20, path)
div_and_write(50, 20, invalid_path)
div_and_write(100, 20, True)
print('- Succeeded ' + str(success_count) + ' times. -')
print('- Became an error ' + str(total_count - success_count) + ' times. -')

import os

os.remove(path)
