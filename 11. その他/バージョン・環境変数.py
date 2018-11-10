import os
import platform
import sys

import jinja2
import pip


# ====== Python Version ======

print(sys.version)
print(sys.version_info)
if sys.version_info.major == 3:
    print('python3')
else:
    print('python2')
print(platform.python_version())
print(platform.python_version_tuple())
print()

# パッケージの Version

print(pip.__version__)
print(jinja2.__version__)

# ====== 環境変数 ======

env = os.environ

# 環境変数を取得

print(type(env))
for k, v in env.items():
    print(k, '=', v, end='\n')
print()
print(env['APPDATA'])
print(env.get('COMSPEC'))
print(env.get('NEW_KEY'))
print(env.get('NEW_KEY', 'default'))
print(os.getenv('NEW_KEY', 'default'))
print()

# 環境変数を設定(追加・上書き)

env['NEW_KEY'] = 'test'
print(env['NEW_KEY'])
env['NEW_KEY'] = 'test2'
print(env['NEW_KEY'])
print()

# 環境変数を削除

print(env.pop('NEW_KEY'))
print(env.pop('NEW_KEY', 'None'))

env['NEW_KEY'] = '100'
print(os.getenv('NEW_KEY'))
del env['NEW_KEY']
print(os.getenv('NEW_KEY'))
