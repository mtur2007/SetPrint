# / maintenance / maintenance / maintenance / maintenance / maintenance / maintenance / maintenance / maintenance / maintenance / maintenance /
# print('\n'+'/ \033[38;2;255;165;0m\033[1mmaintenance\033[0m / \033[38;5;27mmaintenance\033[0m '*5+'/\n')


# 実行コード
from run_image_print import image_print
from to_maintenance_setprint import insert_text_after_match_with_indent
import os


def file_relative_access(relative_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join(base_dir, relative_path)
    return relative_path


style_settings = (

   (("Collections" ,
     {  'image'   : { 'list'    : '►list' ,
                      'tuple'   : '▷tupl' ,
                      'ndarray' : '>Ndry' ,
                      'dict'    : '◆dect'}}),

    ("bracket"     ,
     { 'partially': { 'list'    : ( '\\' , '/' ),
                      'tuple'   : ( '<' , '>' ),
                      'ndarray' : ( '≤' , '≥' ),
                      'dict'    : ( '{' , ')' ),
                      'None'    : ( '`' , '`' )}}),

    ("empty"       , {  'key'   : (' ',':') ,  'value' : ' ' }),
    ("padding"     , {  'key'   : ('*','`') ,  'value' : '-' }),


    ("settings"    , { 'print'  : False }),
    ("progress"    , { 'print'  : False  ,
                       'len'    : 20  }))
)


def replace_hash_with_custom_indices(lst, path=[]):
    
    for i, item in enumerate(lst):
        current_path = path + [i]  # 現在のインデックス経路を保存
        
        if isinstance(item, list):  # ネストされたリストなら再帰呼び出し
            replace_hash_with_custom_indices(item, current_path)

        elif item == '#':  # `'#'` を検出したらその位置をフォーマットに置き換え
            path_txt = ''

            pin_deep = max([deep for deep in parent_point if deep < len(current_path)])

            for indes in current_path[:pin_deep-1]:
                path_txt += str(indes) + '-'

            if len(current_path) >= pin_deep:
                path_txt += '{' + str(current_path[pin_deep-1]) + '}'
            
            for indes in current_path[pin_deep:]:
                path_txt += '-' + str(indes)

            lst[i] = path_txt[:]

'''
---------------------------------------------------------------------------------------------------------------------------------------------
'''

input_file = "/Users/matsuurakenshin/WorkSpace/development/setprint_package/setprint_update/test_setprint_0_3_0.py"  # 開発用ソースファイル
output_file = "/Users/matsuurakenshin/WorkSpace/development/setprint_package/setprint_maintenance/maintenance_setprint.py"  # 出力用

# 開発用コードからメンテナンス用コードの挿入場所を検出し、挿入する。
# tracking_image : 処理のASCIIアート的なトラッキング (キー操作で処理の流れを確認する)
# tracking_rog   : 処理の時系列順のログ

insert_text_after_match_with_indent(input_file, output_file, keep_index=True, tracking_image=False, tracking_rog=False)


# メンテナンス用 データの整形
from maintenance_setprint import SetPrint

test_data = [
    [  [ ['#','#'],['#','#'] ], [ ['#','#'],['#','#'] ]  ],
    [  [ ['#',[['#','#'],['#','#']]],['#','#'] ], [ ['#','#'],['#','#'] ]  ],
    [  [ ['#','#'],['#','#'] ] ],
]

keep_setting={1:'y',2:'x',3:'yf',5:'y',10:'x'}


# '#'部分のインデックスを自動追加 - 親インデックスを自動強調
parent_point = [0] + [ deep-1 if deep_setting == 'yf' else deep for deep, deep_setting in keep_setting.items() ]

replace_hash_with_custom_indices(test_data)

# インスタンスを生成
list_data = SetPrint(test_data)

list_data.set_text_style(style_settings) # set_listの前
keep_tracking = list_data.set_list(guide=True,keep_start=keep_setting)

if keep_tracking != None:
    image_print(keep_tracking)

'''

all_deep_settings
 ['y', 'x', 'yf', 'f', 'y', 'y', 'y', 'y', 'y', 'x']

X_keep_index
('y',) []
('y', 0) []
('y', 0, 'yf') [[-1], [0], [1], [2]]
('y', 1) []
('y', 1, 'yf') [[-1], [0], [1], [2]]
('y', 0, 'yf', 1, 'y') []
('y', 0, 'yf', 1, 'y', 'y') []

flat_X_keep_index
[[5, [[5, [[5, [9, [9, [[5, [13]]]]]]]], [5, [[5, [9, 9]]]]]]]

Y_keep_index
(0,) [[[], [[0]]]]
(0, 0) [[[0], [[0]]], [[0], [[1]]]]
(0, 0, 0) [[[0, 0, 0], [[], [0], [1]]], [[0, 1, 0], [[], [0], [1]]]]
(0, 0, 1) [[[0, 0, 1], [[], [0], [1]]], [[0, 1, 1], [[], [0], [1]]]]
(1,) [[[], [[1]]]]
(1, 0) [[[1], [[0]]], [[1], [[1]]]]
(1, 0, 0) [[[1, 0, 0], [[], [0], [1]]], [[1, 1, 0], [[], [0], [1]]]]
(1, 0, 0, 0, 0) [[[1, 0, 0, 1], [[0]]]]
(1, 0, 0, 0, 0, 0) [[[1, 0, 0, 1, 0], [[0]]]]
(1, 0, 0, 0, 0, 1) [[[1, 0, 0, 1, 0], [[1]]]]
(1, 0, 0, 0, 1) [[[1, 0, 0, 1], [[1]]]]
(1, 0, 0, 0, 1, 0) [[[1, 0, 0, 1, 1], [[0]]]]
(1, 0, 0, 0, 1, 1) [[[1, 0, 0, 1, 1], [[1]]]]
(1, 0, 1) [[[1, 0, 1], [[], [0], [1]]], [[1, 1, 1], [[], [0], [1]]]]
(2,) [[[], [[2]]]]
(2, 0) [[[2], [[0]]]]
(2, 0, 0) [[[2, 0, 0], [[], [0], [1]]]]
(2, 0, 1) [[[2, 0, 1], [[], [0], [1]]]]


out_put
-----------------------------------------------------------------------------------------

::::: 
      :::::                                               ::::: 
            ::::: 0-{0}-0-0 0-{0}-0-1                           ::::: 0-{1}-0-0 0-{1}-0-1 
            ::::: 0-{0}-1-0 0-{0}-1-1                           ::::: 0-{1}-1-0 0-{1}-1-1 
::::: 
      :::::                                               ::::: 
            ::::: 1-{0}-0-0 :::::::::                           ::::: 1-{1}-0-0 1-{1}-0-1 
                                      ::::: 
                                            1-0-0-1-{0}-0 
                                            1-0-0-1-{0}-1 
                                      ::::: 
                                            1-0-0-1-{1}-0 
                                            1-0-0-1-{1}-1 
            ::::: 1-{0}-1-0 1-{0}-1-1                           ::::: 1-{1}-1-0 1-{1}-1-1 
::::: 
      ::::: 
            ::::: 2-{0}-0-0 2-{0}-0-1 
            ::::: 2-{0}-1-0 2-{0}-1-1 

-----------------------------------------------------------------------------------------

'''