import numpy as np

def convert_numpy_scalars(obj):
    """
    オブジェクト obj 内に含まれる NumPy のスカラー値（0次元配列や np.generic）を
    通常の Python のスカラーに変換して返す関数。
    """
    # NumPy配列の場合
    if isinstance(obj, np.ndarray):
        # 0次元配列（スカラー）の場合は変換
        if obj.ndim == 0:
            return obj.item()
        else:
            # 多次元配列の場合は、そのまま返す（または必要に応じて element-wise 変換も可能）
            return obj
    # NumPy のスカラー型の場合
    elif isinstance(obj, np.generic):
        return obj.item()
    
    # リストやタプルの場合は各要素に対して変換を適用
    elif isinstance(obj, (list, tuple)):
        return type(obj)(convert_numpy_scalars(item) for item in obj)
    
    # 辞書の場合は値側に対して変換を適用
    elif isinstance(obj, dict):
        return {k: convert_numpy_scalars(v) for k, v in obj.items()}
    
    else:
        return obj

def max_dimension(obj):
    """
    オブジェクト obj の最大ネスト深度を返す関数。
    
    ・NumPy配列の場合：
      - 0次元（スカラー）の場合は 0 を返し、
      - それ以外の場合は obj.ndim を返す。
    
    ・リスト、タプルの場合：内部の各要素の最大深度を計算し、現在の階層1を加算。
    
    ・辞書の場合：値側に対して同様に計算。
    
    ・その他の型の場合は、コンテナではないとみなし 0 を返す。
    """
    # まず NumPy のスカラーが含まれている場合、変換を試みる
    obj = convert_numpy_scalars(obj)
    
    # NumPy配列の場合
    if isinstance(obj, np.ndarray):
        if obj.ndim == 0:
            return 0
        return obj.ndim

    # リストやタプルの場合
    elif isinstance(obj, (list, tuple)):
        if not obj:  # 空の場合
            return 1
        return 1 + max(max_dimension(item) for item in obj)

    # 辞書の場合（ここでは値に対して再帰的に計算）
    elif isinstance(obj, dict):
        if not obj:
            return 1
        return 1 + max(max_dimension(v) for v in obj.values())

    # その他の型（コンテナではないもの）は 0 次元とみなす
    else:
        return 0

# テスト例
if __name__ == "__main__":
    # 例1: NumPy のスカラー（0次元配列）
    scalar_array = np.array(42)  # 0次元
    converted_scalar = convert_numpy_scalars(scalar_array)
    print("scalar_array:", scalar_array, "->", converted_scalar, type(converted_scalar))
    print("max_dimension(scalar_array):", max_dimension(scalar_array))  # 結果は0

    # 例2: リスト内に NumPy のスカラーが含まれる場合
    nested_list = [1, np.array(3.14), [2, [np.array(100)]]]
    converted_list = convert_numpy_scalars(nested_list)
    print("converted_list:", converted_list)
    print("max_dimension(nested_list):", max_dimension(nested_list))
    # 内部のネストはリストの構造に依存（NumPy のスカラーは 0 次元と扱われる）

    # 例3: 辞書内に NumPy のスカラーおよび多次元配列が含まれる場合
    arr = np.array([[1, 2], [3, 4]])  # ndimは2
    nested_dict = {"a": np.array(10), "b": {"c": arr}}
    converted_dict = convert_numpy_scalars(nested_dict)
    print("converted_dict:", converted_dict)
    print("max_dimension(nested_dict):", max_dimension(nested_dict))
    # 辞書の場合、"a" は 0 次元、"b" は 1 + 2 = 3 (辞書レベル+配列の ndim)


    # 例1: NumPy のスカラー（0次元配列）
    scalar_array = np.array(42)  # 0次元
    converted_scalar = convert_numpy_scalars(scalar_array)
    print("scalar_array:", scalar_array, "->", converted_scalar, type(converted_scalar))
    print("max_dimension(scalar_array):", max_dimension(scalar_array))  # 結果は0
