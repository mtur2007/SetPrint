import numpy as np

def update_numpy_scalars_and_get_depth(obj):
    """
    オブジェクト内の NumPy のスカラー値（np.generic または ndim==0 の ndarray）を
    通常の Python のスカラー値に変換し、かつ最大入れ子深度（次元数）を取得する関数。
    
    戻り値は (updated_obj, depth) のタプルです。
    depth は以下のルールに従って定義:
      - 基本型やスカラーの場合は 0
      - コンテナの場合は 1 + max(child depths)（空の場合は 1）
    """
    # NumPy のスカラー（np.generic）の場合
    if isinstance(obj, np.generic):
        return obj.item(), 0

    # NumPy 配列の場合
    if isinstance(obj, np.ndarray):
        # スカラー配列の場合 (ndim == 0)
        if obj.ndim == 0:
            return obj.item(), 0
        # 非 object 型の配列は更新不要。深度はそのまま ndim を用いる
        if obj.dtype != np.object_:
            return obj, obj.ndim
        else:
            # object 型の NumPy 配列の場合、各要素を再帰的に更新
            new_obj = obj.copy()
            max_sub_depth = 0
            for idx, value in np.ndenumerate(new_obj):
                updated_val, sub_depth = update_numpy_scalars_and_get_depth(value)
                new_obj[idx] = updated_val
                if sub_depth > max_sub_depth:
                    max_sub_depth = sub_depth
            # 空の場合は 1、要素があれば 1 + 子要素の最大深度
            return new_obj, 1 + max_sub_depth if new_obj.size > 0 else 1

    # 辞書の場合: 値を更新し再帰的に深度を取得
    if isinstance(obj, dict):
        if not obj:
            return obj, 1
        new_dict = {}
        max_sub_depth = 0
        for key, value in obj.items():
            updated_val, sub_depth = update_numpy_scalars_and_get_depth(value)
            new_dict[key] = updated_val
            if sub_depth > max_sub_depth:
                max_sub_depth = sub_depth
        return new_dict, 1 + max_sub_depth

    # リストの場合: 各要素を更新
    if isinstance(obj, list):
        if not obj:
            return obj, 1
        new_list = []
        max_sub_depth = 0
        for item in obj:
            updated_item, sub_depth = update_numpy_scalars_and_get_depth(item)
            new_list.append(updated_item)
            if sub_depth > max_sub_depth:
                max_sub_depth = sub_depth
        return new_list, 1 + max_sub_depth

    # タプルの場合: 各要素を更新してタプルに再構成
    if isinstance(obj, tuple):
        if not obj:
            return obj, 1
        new_tuple = []
        max_sub_depth = 0
        for item in obj:
            updated_item, sub_depth = update_numpy_scalars_and_get_depth(item)
            new_tuple.append(updated_item)
            if sub_depth > max_sub_depth:
                max_sub_depth = sub_depth
        return tuple(new_tuple), 1 + max_sub_depth

    # その他の型はコンテナではないとみなし、更新せず深度は 0
    return obj, 0

# --- テスト例 ---
if __name__ == '__main__':
    data = {
        "a": np.array(5),  # NumPy のスカラー配列（ndim == 0）
        "b": [1, 2, np.array(3)],  # リスト内に NumPy スカラー
        "c": np.array([np.array(10), np.array([20, 30])], dtype=object),  # object 型配列内に NumPy 配列
        "d": np.array([[1, 2], [3, 4]]),  # 通常の NumPy 配列（更新不要）
        "#": [[1,2],[np.array(1)]],
        "e": np.float64(3.14),  # NumPy のスカラー（np.generic）
        "f": "text",  # 通常の文字列
        "g": (np.array("hello"), {"sub": np.array(100)}),  # タプルと辞書の入れ子構造
        "h": []  # 空のリスト
    }

    updated_data, max_depth = update_numpy_scalars_and_get_depth(data)
    
    print("=== 変換後のデータ ===")
    print(updated_data)
    print("\n=== 最大入れ子深度 ===")
    print(max_depth)
    
    # 型の確認
    print("\n型の確認:")
    print("a:", type(updated_data["a"]))         # 期待: int
    print("b[2]:", type(updated_data["b"][2]))     # 期待: int
    print("e:", type(updated_data["e"]))           # 期待: float
    print("g[0]:", type(updated_data["g"][0]))     # 期待: str
    print("g[1]['sub']:", type(updated_data["g"][1]["sub"]))  # 期待: int
