import os


def display(e):
    print(str(type(e))
          .replace('<class ', '')
          .replace('>', '')
          .replace("'", '')
          + ': ', e)


dir_path = 'test'
os.mkdir(dir_path)

try:
    import mathmatics
except Exception as e:
    display(e)

try:
    from math import COS
except Exception as e:
    display(e)

try:
    import math

    print(math.PI)
except Exception as e:
    display(e)

try:
    l = 100
    l.append(200)
except Exception as e:
    display(e)

try:
    n = '100'
    print(n + 200)
except Exception as e:
    display(e)

try:
    print(float(['1.23E-3']))
except Exception as e:
    display(e)

try:
    print(float('float number'))
except Exception as e:
    display(e)

try:
    print(100 / 0)
except Exception as e:
    display(e)

try:
    my_number = 100
    print(myNumber)
except Exception as e:
    display(e)

try:
    l = [0, 1, 2]
    print(l[100])
except Exception as e:
    display(e)

try:
    d = {'a': 1, 'b': 2, 'c': 3}
    print(d['x'])
except Exception as e:
    display(e)

try:
    with open('not_exist_file.txt') as f:
        print(f.read())
except Exception as e:
    display(e)

try:
    os.mkdir(dir_path)
except Exception as e:
    display(e)

os.rmdir(dir_path)
