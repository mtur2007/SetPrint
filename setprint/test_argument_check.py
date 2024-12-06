# 入力データ（'#'を含むデータ）
data = [
    ("list", {'style': '#'}),
    ("empty", {'style': '#'}),
    ("padding", {'style': '#'}),
    ("bracket", {'partially': ('#', '#'), 'not': ('#', '#')}),
    ("progress", {'len': '#'})
]

# 制限を設定
constraints = {
    (0, 'style'): {'allowed_values': ['A', 'B', 'C'], 'type': str},           # 文字列のみ許可
    (3, 'partially', 0): {'allowed_values': ['{', '['], 'type': str},         # '{' または '[' のみ許可
    (3, 'partially', 1): {'allowed_values': [')', ']'], 'type': str},         # ')' または ']' のみ許可
    (3, 'not', 0): {'type': str},                                            # 任意の文字列許可
    (3, 'not', 1): {'type': str},                                            # 任意の文字列許可
    (4, 'len'): {'type': int, 'min': 0, 'max': 100},                         # 整数型で0～100
    (1, 'style'): {'type': str, 'max_length': 1},                            # 1文字の文字列のみ許可
    (2, 'style'): {'type': str, 'max_length': 10}                            # 新たに追加（例: 文字列型で最大10文字）
}

# 制限設定のオプション
# =====================================
# 制限は `constraints` 辞書で指定し、以下のオプションが利用可能です。
#
# 1. `type`
#    - 値のデータ型を指定します。
#    - 対応可能な型: int, str, float, bool など任意のPython標準型。
#    例: {'type': str}  # 値は文字列型でなければならない
#
# 2. `allowed_values`
#    - 許可される具体的な値のリストを指定します。
#    例: {'allowed_values': ['A', 'B', 'C'], 'type': str}
#         # 値は 'A', 'B', 'C' のいずれかでなければならない
#
# 3. `min`
#    - 数値の最小値を指定します（`type` が int または float の場合に有効）。
#    例: {'type': int, 'min': 0}  # 値は 0 以上でなければならない
#
# 4. `max`
#    - 数値の最大値を指定します（`type` が int または float の場合に有効）。
#    例: {'type': int, 'max': 100}  # 値は 100 以下でなければならない
#
# 5. `max_length`
#    - 文字列の最大文字数を指定します（`type` が str の場合に有効）。
#    例: {'type': str, 'max_length': 10}  # 文字列型で最大 10 文字
#
# 6. `min_length`
#    - 文字列の最小文字数を指定します（`type` が str の場合に有効）。
#    例: {'type': str, 'min_length': 3}  # 文字列型で 3 文字以上
#
# 使用例:
# constraints = {
#     (0, 'style'): {'allowed_values': ['A', 'B', 'C'], 'type': str},  # 値は 'A', 'B', 'C' のいずれか
#     (1, 'style'): {'type': str, 'max_length': 1},                   # 1 文字の文字列
#     (2, 'style'): {'type': str, 'min_length': 3, 'max_length': 10


# 更新処理の関数
def update_data_with_arguments(data, arguments, constraints):
    for arg_key, arg_value in arguments:
        # data内の該当エントリを見つける
        for i, (data_key, data_value) in enumerate(data):
            if data_key == arg_key:  # キーが一致
                # 制限を確認しながら更新
                for sub_key, sub_value in arg_value.items():
                    if isinstance(data_value[sub_key], tuple):
                        # タプルの場合は要素ごとに更新
                        for j, item in enumerate(sub_value):
                            index = (i, sub_key, j)
                            assign_with_constraints(data, index, item, constraints)
                    else:
                        # 単一値の場合
                        index = (i, sub_key)
                        assign_with_constraints(data, index, sub_value, constraints)

# 制限付きチェックと代入関数
def assign_with_constraints(data, index, value, constraints):
    # 制限の探索: 子インデックスが見つからない場合、親の制限を探す
    constraint = constraints.get(index)
    if constraint is None:
        # インデックスを遡って親を探索
        for i in range(len(index) - 1, 1, -1):  # ネストの深さを順に短く
            parent_index = index[:i]
            if parent_index in constraints:
                constraint = constraints[parent_index]
                break
        if constraint is None:
            raise KeyError(f"No constraints found for index {index} or its parent indices.")

    # データ型のチェック
    if 'type' in constraint and not isinstance(value, constraint['type']):
        raise TypeError(f"Value '{value}' at index {index} must be of type {constraint['type'].__name__}.")

    # 許可された値のチェック
    if 'allowed_values' in constraint and value not in constraint['allowed_values']:
        raise ValueError(f"Value '{value}' at index {index} is not in allowed values {constraint['allowed_values']}.")

    # 範囲チェック
    if 'min' in constraint and value < constraint['min']:
        raise ValueError(f"Value '{value}' at index {index} is less than the minimum value {constraint['min']}.")
    if 'max' in constraint and value > constraint['max']:
        raise ValueError(f"Value '{value}' at index {index} is greater than the maximum value {constraint['max']}.")

    # 値の代入
    i, key, *nested_indices = index
    target = data[i][1][key]  # 指定されたキーのデータ

    # ネストを掘り進めて値を設定
    for idx in nested_indices[:-1]:
        target = target[idx]
    target[nested_indices[-1]] = value


# 引数として指定されたデータ
arguments = [
    ('list', {'style': 'C'}),
    ('empty', {'style': ' '}),
    ('padding', {'style': 'Short'}),
    ('bracket', {'partially': ('{', ')'), 'not': (' ', ' ')}),
    ('progress', {'len': 10})
]

# 更新処理
update_data_with_arguments(data, arguments, constraints)

# 結果を表示
for line in data:
    print(line)