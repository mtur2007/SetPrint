import numpy as np
import pickle
from scipy.ndimage import zoom

def find_numpy_arrays_recursive(data):
    """
    再帰的に探索し、NumPy配列を含むすべてのデータを取得する。
    """
    if isinstance(data, list):
        return [find_numpy_arrays_recursive(item) for item in data]
    elif isinstance(data, np.ndarray) and data.ndim <= 2:
        return data.astype(np.uint8)  # 整数型に変換
    else:
        return data

def resize_binary_matrices(matrices, scale: float):
    """
    画像が2次元の形状 (H, W) で格納されている場合の縮小処理を行う関数。
    
    Parameters:
        matrices: 入れ子のリスト構造またはNumPy配列
        scale (float): 縮小率 (0.0 < scale <= 1.0)

    Returns:
        縮小されたデータ構造（NumPy配列）
    """
    if isinstance(matrices, list):
        return [resize_binary_matrices(item, scale) for item in matrices]
    elif isinstance(matrices, np.ndarray) and matrices.ndim == 2:
        resized = zoom(matrices, zoom=scale, order=0)
        resized = np.clip(resized, 0, 1)  # 0-1の範囲を維持
        return resized.astype(np.uint8)  # 整数型に変換
    else:
        return matrices

# pklファイルを読み込む関数
def load_pkl_file(filename: str):
    """
    pklファイルから"Alltxtdatas"を再帰的に探索し、NumPy配列として返す。
    
    Parameters:
        filename (str): pklファイルのパス

    Returns:
        入れ子のリストまたはNumPy配列
    """
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return find_numpy_arrays_recursive(data["Alltxtdatas"])

# pklファイルからデータを読み込み、縮小したデータを保存する
def process_and_save_binary_pkl(pkl_filename: str, scale_factor: float, output_filename: str):
    """
    pklファイルをロードし、データを縮小して新しいpklファイルとして保存する。
    
    Parameters:
        pkl_filename (str): 入力pklファイルのパス
        scale_factor (float): 縮小率
        output_filename (str): 保存するpklファイルのパス
    """
    matrices = load_pkl_file(pkl_filename)
    resized_matrices = resize_binary_matrices(matrices, scale_factor)
    
    with open(output_filename, 'wb') as f:
        pickle.dump({"Alltxtdatas": resized_matrices}, f)

# 使用例
pkl_filename = "/Users/matsuurakenshin/WorkSpace/development/setprint_package/Development_files/format_data/ocr_txtdata.pkl"
scale_factor = 0.4
output_filename = "/Users/matsuurakenshin/WorkSpace/development/setprint_package/Development_files/format_data/resized_ocr_txtdata.pkl"

process_and_save_binary_pkl(pkl_filename, scale_factor, output_filename)

# 保存したファイルを開いて変数に格納
with open(output_filename, 'rb') as f:
    processed_data = pickle.load(f)["Alltxtdatas"]
