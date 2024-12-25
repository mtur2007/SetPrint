import numpy as np
"""
所属先のインデックスを調べてリストの情報量を大幅に削減するための関数の試作ファイル
"""

def access_nested_collection(nested_list,indices):
    
    for i,index in enumerate(indices):

        if type(nested_list) == dict:
            if not(index in nested_list):
                return None
            
        else:
            if not(0 <= index < len(nested_list)):     
                return None # インデックスが範囲外の場合はNoneを返す
            
        # int または str の場合、最後のインデックスでない場合はNoneを返す
        if not isinstance(nested_list[index], (list, tuple, np.ndarray, dict)):
            if i == len(indices) - 1:
                value = nested_list[index]
                return value
        
            else:
                return None # インデックスが範囲外の場合はNoneを返す
            
        nested_list = nested_list[index]
        
    # 最終的な要素がリストまたは配列の場合
    else:
        value = nested_list
        return value

def check_matching_elements(mapping_point, collection_index):
    """
    keep_index(キープ時のx方向のインデックス) の要素が 辞書型が格納されている暫定インデックス(keep_index) にインデックス順で一致するかを確認。
    各2次元目の要素を調べ、連続一致数が最大となるインデックスを返す。
    """
    max_match_count = 0  # 最大連続一致数
    max_match_index = -1  # 最大連続一致数を持つ1次元目のインデックス

    for row_index, row in enumerate(mapping_point):
        current_match_count = 0  # 現在の行での連続一致数

        for i, elem in enumerate(row):
            if i < len(collection_index) and elem == collection_index[i]:
                current_match_count += 1  # 一致した場合カウントを増やす
            else:
                break  # 一致が途切れたら終了

        # 最大連続一致数を更新
        if current_match_count > max_match_count:
            max_match_count = current_match_count
            max_match_index = row_index

    return max_match_index  # 最大連続一致数を持つ行のインデックス

# テスト配列
test_collection = [

   { 'table1':
        ([1,  2,  3],
         [4,  5,  6],
         [7,  8,  9]),
    'table2':
        ([1,  2,  3],
         [4,  5,  6],
         [7,  8,  9]),
     },
    
    [
        ([1,  2,  3],
         [4,  5,  6],
         [7,  8,  9]),
    ]

]

# keep_index/keep_key
mapping_point = [[0,0]   ,[0,2]]
mapping_key   = [[1,'table1'],[1,'table2']]

# 配列のインデックス
collection_index = [0,1,0]
#collection_index = [0,2,0]

#collection_index = [1,2,0]

# 関数の実行
matching_index = check_matching_elements(mapping_point, collection_index)

# 出力
print(f"最大連続一致数を持つ1次元目のインデックス: {matching_index}")

if matching_index != -1:
    parent_keep_index = mapping_point[matching_index]
    parent_mapping_key = mapping_key[matching_index]
    print(f'所属 keep_index/key : {parent_keep_index}')
    print(f'所属 mapping_key    : {parent_mapping_key}')

    parent_keep_index[parent_mapping_key[0]] = parent_mapping_key[1]
    print(f'復元 index          : {parent_keep_index}')
else:
    print(f'結果は-1の為、このインデックスに辞書型のキーを使う場所はありません。')
    print(f'所属 keep_index/key : {collection_index}')