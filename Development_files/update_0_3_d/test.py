import numpy as np

if type(test_data) == np.ndarray:

    # 0次元 (スカラー) の場合、要素を直接判定
    if np.ndim == 0:
        value = np.item() # スカラー値を取得

        if isinstance(value, int):
            return "int"
        elif isinstance(value, str):
            return "str"
        elif isinstance(value, float):
            return "float"
        else:
            return "other"

print(test_data,type(test_data))
