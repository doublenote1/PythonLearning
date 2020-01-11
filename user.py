def make_entry(paths, root='temp'):

    import os
    import re
    import shutil

    if root == '' or root == 'temp':
        root_path = os.path.join(os.getcwd(), 'temp')
    else:
        root_path = os.path.join(os.getcwd(), 'work_space', root)
    if os.path.exists(root_path):
        shutil.rmtree(root_path)
    if type(paths) is str:
        paths = [paths]
    for path in paths:
        match = re.match(r'(.+)\\([^\\]*)$', path)
        if match:
            folder = os.path.join(root_path, match.group(1))
            has_file = match.group(2)
        else:
            folder = root_path
            has_file = True
        os.makedirs(folder, exist_ok=True)
        if has_file:
            with open(os.path.join(root_path, path), 'w') as f:
                pass
    return root_path


def create_folder(path='temp'):
    import os
    import shutil

    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)


def show_entry(path='temp', cut=None):
    import glob
    import os

    if not os.path.isdir(path):
        print('Not Exists!')
        return
    if not os.listdir(path):
        print('Empty!')
        return
    if not cut:
        cut = path + '\\'
    lst = [x.replace(cut, '')
           for x in glob.glob(path + '\\**', recursive=True)
           if x != path + '\\' and (os.path.isfile(x) or not os.listdir(x))]
    if lst:
        print(', '.join(lst))

