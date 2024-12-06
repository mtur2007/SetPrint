def generate_constraints_recursive(data, placeholder='#', current_index=()):
    """
    ネストされたデータ構造を再帰的に探索し、
    placeholderに一致する値のインデックスを収集してconstraintsテンプレートを生成する。

    Parameters:
        data: 入力データ（リスト・辞書・タプルを含む構造）
        placeholder: 検索対象の値（デフォルト: '#'）
        current_index: 現在のインデックス（再帰的に構築）

    Returns:
        constraintsテンプレート（辞書形式）
    """
    constraints = {}

    if isinstance(data, dict):
        # 辞書を探索
        for key, value in data.items():
            new_index = current_index + (key,)
            constraints.update(generate_constraints_recursive(value, placeholder, new_index))
    elif isinstance(data, (list, tuple)):
        # リストやタプルを探索
        for i, value in enumerate(data):
            new_index = current_index + (i,)
            constraints.update(generate_constraints_recursive(value, placeholder, new_index))
    else:
        # 値がplaceholderと一致する場合
        if data == placeholder:
            constraints[current_index] = '{}'

    return constraints

def convert_tuple_to_list(data):
    """
    ネストされたデータ構造内のタプルをリストに変換し、
    辞書型はそのまま保持します。

    Parameters:
        data: 入力データ（リスト、タプル、辞書など）

    Returns:
        タプルをリストに変換したデータ構造
    """
    if isinstance(data, tuple):
        # タプルをリストに変換し、再帰的に要素を処理
        return [convert_tuple_to_list(item) for item in data]
    elif isinstance(data, list):
        # リスト内の要素を再帰的に処理
        return [convert_tuple_to_list(item) for item in data]
    elif isinstance(data, dict):
        # 辞書はそのまま保持し、値を再帰的に処理
        return {key: convert_tuple_to_list(value) for key, value in data.items()}
    else:
        # 基本データ型はそのまま返す
        return data

def update_data_with_arguments(data, arguments, constraints, current_index=()):

    if isinstance(arguments, dict):
        # 辞書を探索
        for key, value in arguments.items():
            new_index = current_index + (key,)
            update_data_with_arguments(data, value, constraints, new_index)
    elif isinstance(arguments, (list, tuple)):
        # リストやタプルを探索
        for i, value in enumerate(arguments):
            new_index = current_index + (i,)
            update_data_with_arguments(data, value, constraints, new_index)
    else:
        # 値がplaceholderと一致する場合
        if current_index in constraints:
            
            target = data
            # 最後のキー以外でデータ構造を掘り下げる
            for key in current_index[:-1]:
                target = target[key]
            
            new_value = arguments
            constraint = constraints[current_index]

            update_True = True

            # データ型のチェック
            if 'type' in constraint and not isinstance(new_value, constraint['type']):
                print(f"Value '{new_value}' at index {current_index} must be of type {constraint['type'].__name__}.")
                update_True = False

            # 許可された値のチェック
            if 'allowed_values' in constraint and new_value not in constraint['allowed_values']:
                print(f"Value '{new_value}' at index {current_index} is not in allowed values {constraint['allowed_values']}.")
                update_True = False

            # 範囲チェック
            if 'min' in constraint and new_value < constraint['min']:
                print(f"Value '{new_value}' at index {current_index} is less than the minimum value {constraint['min']}.")
                update_True = False
            if 'max' in constraint and new_value > constraint['max']:
                print(f"Value '{new_value}' at index {current_index} is greater than the maximum value {constraint['max']}.")
                update_True = False

            # 文字列の長さチェック
            if isinstance(new_value, str):  # 文字列型の場合のみ適用
                if 'max_length' in constraint and len(new_value) > constraint['max_length']:
                    print(f"Value '{new_value}' at index {current_index} exceeds maximum length of {constraint['max_length']}.")
                    update_True = False
                if 'min_length' in constraint and len(new_value) < constraint['min_length']:
                    print(f"Value '{new_value}' at index {current_index} is shorter than minimum length of {constraint['min_length']}.")
                    update_True = False

            if update_True:
                target = data
                # 最後のキー以外でデータ構造を掘り下げる
                for key in current_index[:-1]:
                    target = target[key]
                
                # 最後のキーで値を更新
                target[current_index[-1]] = new_value

    return constraints

'''
=========================================================================================
管理場所
'''

# 入力データ('#'は引数の受け取り箇所)
data = [
    ("list", {'style': '#'}),
    ("empty", {'style': '#'}),
    ("padding", {'style': '#'}),
    ("bracket", {'partially': ('#', '#'), 'not': ('#', '#')}),
    ("progress", {'len': '#'}),
]

# 制限('#'の箇所をまとめて管理)
constraints = {
    (0, 1, 'style')        : {'type': str},
    (1, 1, 'style')        : {'type': str, 'min_length':1},
    (2, 1, 'style')        : {'type': str, 'min_length':1},
    (3, 1, 'partially', 0) : {'type': str, 'min_length':1},
    (3, 1, 'partially', 1) : {'type': str, 'min_length':1},
    (3, 1, 'not', 0)       : {'type': str, 'min_length':1},
    (3, 1, 'not', 1)       : {'type': str, 'min_length':1},
    (4, 1, 'len')          : {'type': int, 'min':0},
}

'''
制限設定のオプション
=====================================
制限は `constraints` 辞書で指定し、以下のオプションが利用可能です。

1. `type`
   - 値のデータ型を指定します。
   - 対応可能な型: int, str, float, bool など任意のPython標準型。
   例: {'type': str}  # 値は文字列型でなければならない

2. `allowed_values`
   - 許可される具体的な値のリストを指定します。
   例: {'allowed_values': ['A', 'B', 'C'], 'type': str}
        # 値は 'A', 'B', 'C' のいずれかでなければならない

3. `min`
   - 数値の最小値を指定します（`type` が int または float の場合に有効）。
   例: {'type': int, 'min': 0}  # 値は 0 以上でなければならない

4. `max`
   - 数値の最大値を指定します（`type` が int または float の場合に有効）。
   例: {'type': int, 'max': 100}  # 値は 100 以下でなければならない

5. `max_length`
   - 文字列の最大文字数を指定します（`type` が str の場合に有効）。
   例: {'type': str, 'max_length': 10}  # 文字列型で最大 10 文字

6. `min_length`
   - 文字列の最小文字数を指定します（`type` が str の場合に有効）。
   例: {'type': str, 'min_length': 3}  # 文字列型で 3 文字以上

入力データ変更
'''

arguments = (
    ("list"    , {'style': '►'}),
    ("empty"   , {'style': ' '}),
    ("padding" , {'style': ' '}),
    ("bracket" , {'partially':('{',')'),'not':(' ',' ')}),
    ("progress", {'len'  : 100})
)

# constraintsテンプレートを生成
constraints_template = generate_constraints_recursive(data)

#結果を表示
print("Generated constraints template:")
print()
print('constraints = {')
for key, value in constraints_template.items():
    print(f"    {key}: {value},")
print('}')

data = convert_tuple_to_list(data)
update_data_with_arguments(data, arguments, constraints, current_index=())

for line in data:
    print(line)