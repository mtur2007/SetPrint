# / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test /
#print('\n'+'/ \033[38;2;255;165;0m\033[1mtest\033[0m / \033[38;5;27mtest\033[0m '*10+'/\n')

# / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict /
#print('\n'+'/ \033[38;5;27mdemo\033[0m / \033[38;2;255;165;0m\033[1mdict\033[0m '*10+'/\n')

# 実行コード
from test_setprint_0_3_0 import SetPrint


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



test_data = [
    [  [ ['(0)-{0}-0','(0)-{0}-1'],['(0)-{0}-2','(0)-{0}-3'] ], [ ['(0)-{1}-0','(0)-{1}-1'],['(0)-{1}-2','(0)-{1}-3'] ]  ],
    [  [ ['(1)-{0}-0','(1)-{0}-1'],[

                                     [['(1)-(0)-{2}-0','(1)-(0)-{2}-1'],['(1)-(0)-{2}-2','(1)-(0)-{2}-3'] ]
                                       
                                               ,'(1)-{0}-3'] ], [ ['(1)-{1}-0','(1)-{1}-1'],['(1)-{1}-2','(1)-{1}-3'] ]  ],
    
    [  [ ['(2)-{0}-0','(2)-{0}-1'],['(2)-{0}-2','(2)-{0}-3'] ]]
]

'''

test_data = [
    [  [ ['(0)-{0}-0','(0)-{0}-1'],['(0)-{0}-2','(0)-{0}-3'] ], [ ['(0)-{1}-0','(0)-{1}-1'],['(0)-{1}-2','(0)-{1}-3'] ]  ],
    [  [ ['(1)-{0}-0','(1)-{0}-1'],['(1)-{0}-2','(1)-{0}-3'] ], [ ['(1)-{1}-0','(1)-{1}-1'],['(1)-{1}-2','(1)-{1}-3'] ]  ],
    [  [ ['(2)-{0}-0','(2)-{0}-1'],['(2)-{0}-2','(2)-{0}-3'] ]]
]

[  [ ['(__)-{0}-0','(__)-{0}-1'],['(__)-{0}-2','(__)-{0}-3'] ], [ ['(__)-{1}-0','(__)-{1}-1'],['(__)-{1}-2','(__)-{1}-3'] ]  ]


test_data = [
    [  [ ['(0)-{0}-0','(0)-{0}-1'],['(0)-{0}-2','(0)-{0}-3'] ], [ ['(0)-{1}-0','(0)-{1}-1'],['(0)-{1}-2','(0)-{1}-3'] ]  ],
    [  [ ['(1)-{0}-0','(1)-{0}-1'],[

                                     [['(1)-(0)-{0}-0','(1)-(0)-{0}-1'],['(1)-(0)-{0}-2','(1)-(0)-{0}-3'] ]
                                       
                                               ,'(1)-{0}-3'] ], [ ['(1)-{1}-0','(1)-{1}-1'],['(1)-{1}-2','(1)-{1}-3'] ]  ],
    
    [  [ ['(2)-{0}-0','(2)-{0}-1'],['(2)-{0}-2','(2)-{0}-3'] ]]
]

'''

# インスタンスを生成
list_data = SetPrint(test_data)

list_data.set_text_style(style_settings) # set_listの前

# データの整形
keep_tracking = list_data.set_list(guide=True,keep_start={1:'x',2:'y',3:'yf',5:'yf',10:'x'})


'''

data 

[
    [  [ ['(0)-{0}-0','(0)-{0}-1'],['(0)-{0}-2','(0)-{0}-3'] ], [ ['(0)-{1}-0','(0)-{1}-1'],['(0)-{1}-2','(0)-{1}-3'] ]  ],
    [  [ ['(1)-{0}-0','(1)-{0}-1'],[

                                     [['(1)-(0)-{0}-0','(1)-(0)-{0}-1'],['(1)-(0)-{0}-2','(1)-(0)-{0}-3'] ]
                                       
                                               ,'(1)-{0}-3'] ], [ ['(1)-{1}-0','(1)-{1}-1'],['(1)-{1}-2','(1)-{1}-3'] ]  ],
]
                                               
keep_settings
{1:'x',2:'y',3:'yf',5:'yf',10:'x'}

    all_deep_settings
    ['x', 'y', 'yf', 'f', 'yf', 'f', 'f', 'f', 'f', 'x']    
    
X_keep_index
(0,) []
(0, 'y') []
(0, 'y', 'yf') [[-1], [0], [1], [2]]
(1,) []
(1, 'y') []
(1, 'y', 'yf') [[-1], [0], [1], [2]]
(1, 'y', 'yf', 0, 'yf') [[-1], [0], [1], [2]]
(2,) []
(2, 'y') []
(2, 'y', 'yf') [[-1], [0], [1], [2]]

flat_X_keep_index
[[5, [[5, [[5, [9, 9]]]]]], [5, [[5, [[5, [[9, [[5, [13, 13]]]], 9]]]]]], [5, [[5, [[5, [9, 9]]]]]]]

Y_keep_index
(0,) [[[], [[0]]], [[], [[1]]], [[], [[2]]]]
(0, 0) [[[0], [[0]]], [[1], [[0]]], [[2], [[0]]]]
(0, 0, 0) [[[0, 0, 0], [[], [0], [1]]], [[1, 0, 0], [[], [0], [1]]], [[2, 0, 0], [[], [0], [1]]]]
(0, 0, 1) [[[0, 0, 1], [[], [0], [1]]], [[1, 0, 1], [[], [0], [1]]], [[2, 0, 1], [[], [0], [1]]]]
(0, 1) [[[0], [[1]]], [[1], [[1]]]]
(0, 1, 0) [[[0, 1, 0], [[], [0], [1]]], [[1, 1, 0], [[], [0], [1]]]]
(0, 1, 1) [[[0, 1, 1], [[], [0], [1]]], [[1, 1, 1], [[], [0], [1]]]]
(0, 0, 1, 0, 0) [[[1, 0, 1, 0, 0], [[], [0], [1]]]]
(0, 0, 1, 0, 1) [[[1, 0, 1, 0, 1], [[], [0], [1]]]]

run_tracking
[[5], [6], [[5], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [8]], [9], [6], [[5], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 2], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [2, 4], [2, 1], [2, 3], [4]], [9], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [8]], [9], [6], [[5], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [8]], [9], [8]]


out_put

:::::                                 :::::                                                                   ::::: 
      :::::                                 :::::                                                                   ::::: 
            ::::: (0)-{0}-0 (0)-{0}-1             ::::: (1)-{0}-0                                   (1)-{0}-1             ::::: (2)-{0}-0 (2)-{0}-1 
            ::::: (0)-{0}-2 (0)-{0}-3             ::::: :::::::::                                   (1)-{0}-3             ::::: (2)-{0}-2 (2)-{0}-3 
                                                                  ::::: (1)-(0)-{0}-0 (1)-(0)-{0}-1 
                                                                  ::::: (1)-(0)-{0}-2 (1)-(0)-{0}-3 
      :::::                                 ::::: 
            ::::: (0)-{1}-0 (0)-{1}-1             ::::: (1)-{1}-0                                   (1)-{1}-1 
            ::::: (0)-{1}-2 (0)-{1}-3             ::::: (1)-{1}-2                                   (1)-{1}-3 

'''