def print_serial(text):
    print(text, end=', ')

def print_newline(text):
    print('\n', text, sep='', end=', ')

def print_err(e):
    print(type(e).__name__, e, sep=': ')

def save_file(new_dir_path, new_filename='', new_file_content='', mode='w'):
    import os
    os.makedirs(new_dir_path, exist_ok=True)
    if new_filename:
        with open(os.path.join(new_dir_path, new_filename), mode) as f:
            f.write(new_file_content)

def method_test():
    import re

    def reset():
        global containers
        containers = [
            list(range(3)),
            tuple(range(3)),
            set(range(3)),
            'abc',
        ]

    methods = [
        'append(100)',
        'add(100)',
        'insert(0,100)',
        'remove(0)',
        'discard(0)',
        'pop()',
        'clear()',
        'sort()',
        'reverse()',
        'index(1)',
    ]

    funcs = [
        'len'
    ]

    for method in methods:
        reset()
        print(re.match(r'\w+', method)[0])
        for container in containers:
            try:
                exec('container.' + method)
                print(container)
            except Exception as e:
                print(type(e))
        print()

    for func in funcs:
        reset()
        print(re.match(r'\w+', func)[0])
        for container in containers:
            try:
                exec('print(' + func + '(container))')
            except Exception as e:
                print(type(e))
        print()
