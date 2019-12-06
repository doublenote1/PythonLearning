import os

path = 'grep_like.txt'
text = """\
XXX YYY ZZZ
YYY
aaa
XXX
ZZZ XXX
xxx
"""

with open(path, 'w') as f:
    f.write(text)

with open(path) as f:
    text = f.read()
    print(text)
print()

def grep(path: str, string: str, *, re: bool = False, case: bool = True):
    with open(path) as f:
        lst_f = list(f)
    if not re:
        if case:
            dummy_lst = lst_f
        else:
            dummy_lst = [x.lower() for x in lst_f]
            string = string.lower()
        lines = [(i, x.strip()) for i, x in enumerate(lst_f) if string in dummy_lst[i]]
    else:
        import re
        if case:
            flag = 0
        else:
            flag = re.IGNORECASE
        lines = [(i, x.strip()) for i, x in enumerate(lst_f) if re.search(string, x, flags=flag)]
    return lines

print(grep(path, 'ZZZ'))
print(grep(path, 'XXX', case=False))
print(grep(path, r'(?:.{3} )+', re=True))

os.remove(path)
