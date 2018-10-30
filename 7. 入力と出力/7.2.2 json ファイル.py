import json
import pprint


# ****** 辞書型へ変換 ******

# JSON 文字列から

json_str = '{ "う": ["abc", "efg"], "あ": { "b": [1, 2], "a": 1 }, "い": { "d": [10, 20], "c": 10 }, "え": "last" }'

json_dict = json.loads(json_str)
print(json_dict)
print()

# JSON 形式でファイルへ保存

with open('sample.json', 'w', encoding="utf-8") as f:
    json.dump(json_dict, f,
              separators=(', ', ': '),
              indent=2,
              sort_keys=True,
              ensure_ascii=False
              )

# JSON ファイルから

with open('sample.json', 'r', encoding="utf-8") as f:
    json_dict = json.load(f)
print(json_dict)
print()

# JSON 文字列から順番付辞書型へ変換

from collections import OrderedDict

od_json_dict = json.loads(json_str, object_pairs_hook=OrderedDict)
print(od_json_dict)
print()

# ****** 値の取得・変更・削除・追加 ******

# 値の取得
print(json_dict['あ']['a'])
print(json_dict['い']['d'][1])
print(json_dict.get('Odde'))
print()

# 値の変更
print('-Change value [\'う\'][1] -> \'xyz\'-')
json_dict['う'][1] = 'xyz'
pprint.pprint(json_dict, width=60)
print()

# 値の削除
print('-Extracted \'え\': \'' + json_dict.pop('え') + '\'-')
print('-Deleted [\'う\'][0]-')
del json_dict['う'][0]
pprint.pprint(json_dict, width=60)
print()

# 値の追加
print('-Added [\'い\'][\'e\'] = "added"-')
json_dict['い']['e'] = 'added'
pprint.pprint(json_dict, width=60)
print()

# ****** 整形 ******

print('-文字列-')
print(json_str)
print()

# 辞書へ変換
json_dict = json.loads(json_str)
print('-辞書形式-')
print(json_dict)
print()

# 辞書をJSON形式文字列として出力
json_dumps = json.dumps(json_dict,
                        separators=(', ', ': '),
                        indent=2,
                        sort_keys=True,
                        ensure_ascii=False
                        )
print('-JSON形式（整形済み）-')
print(json_dumps)
