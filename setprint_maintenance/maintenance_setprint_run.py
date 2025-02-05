# / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test /
#print('\n'+'/ \033[38;2;255;165;0m\033[1mtest\033[0m / \033[38;5;27mtest\033[0m '*10+'/\n')

# / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict /
#print('\n'+'/ \033[38;5;27mdemo\033[0m / \033[38;2;255;165;0m\033[1mdict\033[0m '*10+'/\n')

# 実行コード
import pickle
import numpy as np
from run_image_print import image_print

from maintenance_setprint import SetPrint


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


test_data = [[[ [0,[[10,10],[10,10]]],[0,0] ], [[1,1],[1,1]]],[[ [2,2],[2,2] ], [[3,3],[[[33,33],[33,33]],3]]]]
# keep_tracking = list_data.set_list(guide=True,keep_start={1:'y',2:'x',3:'yf',5:'y',7:'x'})

# 他の配列
# test_data = [[[0,0],[['a',10],0]],[[0,0],[[0,0],0]]]
# keep_tracking = list_data.set_list(guide=True,keep_start={1:'x',2:'yf',4:'y'})


# インスタンスを生成
list_data = SetPrint(test_data)

list_data.set_text_style(style_settings) # set_listの前

# データの整形

# keep_tracking = list_data.set_list(guide=True,keep_start={1:'y',10:'x'})

keep_tracking = list_data.set_list(guide=True,keep_start={1:'y',2:'x',3:'yf',5:'yf',10:'x'})

image_print(keep_tracking)



'''

data
[[[ [0,[[10,10],[10,10]]],[0,0] ], [[1,1],[1,1]]],[[ [2,2],[2,2] ], [[3,3],[[[33,33],[33,33]],3]]]]

keep_settings
{1:'y',2:'x',3:'yf',5:'yf',10:'x'}

    all_deep_settings
    ['y', 'x', 'yf', 'f', 'yf', 'f', 'f', 'f', 'f', 'x']
    
    
X_keep_index
('y',) []
('y', 0) []
('y', 0, 'yf') [[-1], [0], [1], [2]]
('y', 0, 'yf', 1, 'yf') [[-1], [0], [1], [2]]
('y', 1) []
('y', 1, 'yf') [[-1], [0], [1], [2]]
('y', 1, 'yf', 0, 'yf') [[-1], [0], [1], [2]]


flat_X_keep_index
[[5, [[5, [[5, [1, [5, [[5, [2, 2]]]]]]]], [5, [[5, [[5, [[5, [2, 2]]]], 1]]]]]]]
    
    one_deep
    index : [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1], [0, 1], [0, 1, 0], [0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 1, 0, 1]]
    len   : [5, 5, 5, 1, 5, 5, 2, 2, 5, 5, 5, 5, 2, 2, 1]


Y_keep_index
(0,) [[[], [[0]]], [[0], [[0]]], [[0], [[1]]]]
(0, 0) [[[0, 0, 0], [[], [0], [1]]], [[0, 1, 0], [[], [0], [1]]]]
(0, 0, 0) [[[0, 0, 0, 1, 0], [[], [0], [1]]]]
(0, 0, 1) [[[0, 0, 0, 1, 1], [[], [0], [1]]]]
(0, 1) [[[0, 0, 1], [[], [0], [1]]], [[0, 1, 1], [[], [0], [1]]]]
(1,) [[[], [[1]]], [[1], [[0]]], [[1], [[1]]]]
(1, 0) [[[1, 0, 0], [[], [0], [1]]], [[1, 1, 0], [[], [0], [1]]]]
(1, 1) [[[1, 0, 1], [[], [0], [1]]], [[1, 1, 1], [[], [0], [1]]]]
(1, 1, 0) [[[1, 1, 1, 0, 0], [[], [0], [1]]]]
(1, 1, 1) [[[1, 1, 1, 0, 1], [[], [0], [1]]]]

run_tracking
[[5], [6], [[5], [6], [[0], [2], [2, 0], [2, 1], [2, 2], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [2, 4], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [8]], [9], [6], [[5], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 2], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [2, 4], [2, 1], [2, 3], [4]], [9], [8]], [9], [8]]


out_put

::::: :::::                           ::::: 
            ::::: 0 :::::                   :::::     1             1 
                          ::::: 10 10 
                          ::::: 10 10 
            ::::: 0     0                   :::::     1             1 
::::: :::::                           ::::: 
            ::::: 2     2                   :::::     3             3 
            ::::: 2     2                   ::::: :::::             3 
                                                        ::::: 33 33 
                                                        ::::: 33 33 

'''