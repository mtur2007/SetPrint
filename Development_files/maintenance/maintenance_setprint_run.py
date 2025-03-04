# / maintenance / maintenance / maintenance / maintenance / maintenance / maintenance / maintenance / maintenance / maintenance / maintenance /
# print('\n'+'/ \033[38;2;255;165;0m\033[1mmaintenance\033[0m / \033[38;5;27mmaintenance\033[0m '*5+'/\n')


# 実行コード
from run_image_print import image_print
from to_maintenance_setprint import insert_text_after_match_with_indent
import os

import numpy as np


def file_relative_access(relative_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join(base_dir, relative_path)
    return relative_path


style_settings = (

   (("Collections" ,
     {  'image'   : { 'list'    : '++@_fter' ,
                      'tuple'   : '-@_fter' ,
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
        
        if isinstance(item, (list,np.ndarray,tuple,dict)):  # ネストされたリストなら再帰呼び出し
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

input_file = "/Users/matsuurakenshin/WorkSpace/development/setprint_package/Development_files/update_0_3_d/test_setprint_0_3_0.py"  # 開発用ソースファイル
output_file = "/Users/matsuurakenshin/WorkSpace/development/setprint_package/Development_files/maintenance/maintenance_setprint.py"  # 出力用

# 開発用コードからメンテナンス用コードの挿入場所を検出し、挿入する。
# tracking_image : 処理のASCIIアート的なトラッキング (キー操作で処理の流れを確認する)
# tracking_rog   : 処理の時系列順のログ
keep_index=True
tracking_image=True
tracking_rog=False

insert_text_after_match_with_indent(input_file, output_file, keep_index, tracking_image, tracking_rog)

# メンテナンス用 データの整形
from maintenance_setprint import SetPrint

test_sequence = [
    [
        [
            '-before',
            '++@_fter',
        ],

        [
            '++before',
            '-@_fter'
        ]
    ],
    #------------------------
    [
        [
            '-before',
            ['++@_fter']
        ],

        [
            '++before',
            ('-@_fter',)
        ]
    ],
    #------------------------
    [
        [
            ('-before',),
            ['++@_fter']
        ],

        [
            ['++before'],
            ('-@_fter',)
        ],
    ],
    # /f/ ==================================
    [
        [
            ('-before',('-before',)),
            ['++@_fter',['++@_fter']]
        ],

        [
            ['++before',['++@_fter']],
            ('-@_fter',('-before',))
        ],
    ],

]

test_mapping = [
    [
        {
            '-before':'--',
            '++@_fter':'++++',
        },

        {
            '++before':'++++',
            '-@_fter':'--'
        }
    ],
    #------------------------
    [
        {
            '-before':'--',
            '++@_fter':{'++@_fter':'++++'}
        },

        {
            '++before':'++++',
            '-@_fter':{'-@_fter':'--'}
        }
    ],
    #------------------------
    [
        {
            '-before':{'-before':'--'},
            '++@_fter':{'++@_fter':'++++'}
        },

        {

            '++before':{'++before':'++++'},
            '-@_fter':{'-@_fter':'--'}
        },
    ],
    # /f/ ==================================
    [
        {
            '-before':{'-before':{'-before':'--'}},
            '++@_fter':{'++@_fter':{'++@_fter':'++++'}}
        },

        {
            '++before':{'++before':{'++before':'++++'}},
            '-@_fter':{'-@_fter':{'-@_fter':'--'}}
        },
    ]
]

# keep_setting={1:'x',3:'x',100:'y'}
# keep_setting={1:'x',3:'y',100:'y'}
keep_settings={1:'x',3:'yf',100:'y'}


# '#'部分のインデックスを自動追加 - 親インデックスを自動強調
parent_point = [0] + [ deep-1 if deep_setting == 'yf' else deep for deep, deep_setting in keep_settings.items() ]

test_data = test_sequence if 0 == 0 else test_mapping

replace_hash_with_custom_indices(test_data)

# インスタンスを生成
list_data = SetPrint(test_data)

list_data.set_text_style(style_settings) # set_listの前
return_data = list_data.set_list(route='maintenance',keep_settings=keep_settings)

if tracking_image:
    with open('/Users/matsuurakenshin/WorkSpace/development/setprint_package/Development_files/format_data/output_maintenance.txt','w') as f:
        for line in return_data[0]:
                f.write(line+'\n')
    image_print(return_data[1])

else:
    with open('/Users/matsuurakenshin/WorkSpace/development/setprint_package/Development_files/format_data/output_maintenance.txt','w') as f:
        for line in return_data:
                f.write(line+'\n')
