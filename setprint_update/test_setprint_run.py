# / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test /
#print('\n'+'/ \033[38;2;255;165;0m\033[1mtest\033[0m / \033[38;5;27mtest\033[0m '*10+'/\n')

# / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict /
#print('\n'+'/ \033[38;5;27mdemo\033[0m / \033[38;2;255;165;0m\033[1mdict\033[0m '*10+'/\n')

# 実行コード
import pickle
from test_setprint_0_3_0 import SetPrint
#from demo_setprint_0_3_0 import SetPrint

import os

def file_relative_access(relative_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join(base_dir, relative_path)
    return relative_path

# pickleファイルからデータを読み込む
# file_name = 'ocr_txtdata.pkl'
# with open(file_name, "rb") as file:
#       loaded_data = pickle.load(file)

# keyを指定してテキストデータを取得
# txt_data = loaded_data["Alltxtdatas"]

# list_data = SetPrint(txt_data)
#list_data = SetPrint(list)

# インデックスで引数のチェックを行う為、この配列の通りに指定してください。
# 制限の範囲内ではなかった値は表示され、デフォルトの値が代入されます。

# set_datas = list_data.set_list(guide=True, keep_start=1, keep_range='all')

style_settings = (

   (("Collections" ,
     {  'image'   : { 'list'    : '►list' ,
                      'tuple'   : '▷tuple' ,
                      'ndarray' : '>nadarray' ,
                      'dict'    : '◆dect' }}),

    ("bracket"     ,
     { 'partially': { 'list'    : ( '{' , ')' ),
                      'tuple'   : ( '<' , '>' ),
                      'ndarray' : ( '(' , '}' ),
                      'dict'    : ( '{' , ')' ),
                      'None'    : ( '`' , '`' )}}),

    ("padding"     , {  'key'   : (' ', ':') , 'value'  : ' ' }),
    ("empty"       , {  'key'   : ('*', ' ') , 'value'  : '-' }),


    ("settings"    , { 'print'  : True }),
    ("progress"    , { 'print'  : False  ,
                       'len'    : 20  }))
)

test_dict = [ [0,(0,1,2),2], (0,1,2), {'a':0, 'b':{'zero':0, 'frst':1, 'twe':2}, 'c':2}, {'zero':0, 'frst':1, 'twe':2} ]

list_data = SetPrint(test_dict)

style_settings = (

   (("Collections" ,
     {  'image'   : { 'list'    : '►list' ,
                      'tuple'   : '▷tuple' ,
                      'ndarray' : '>nadarray' ,
                      'dict'    : '◆dect'}}),

    ("bracket"     ,
     { 'partially': { 'list'    : ( '｢' , '｣' ),
                      'tuple'   : ( '<' , '>' ),
                      'ndarray' : ( '(' , '}' ),
                      'dict'    : ( '/' , '/' ),
                      'None'    : ( '`' , '`' )}}),

    ("empty"       , {  'key'   : (' ',':') ,  'value' : ' ' }),
    ("padding"     , {  'key'   : ('*',' ') ,  'value' : '-' }),


    ("settings"    , { 'print'  : True }),
    ("progress"    , { 'print'  : False  ,
                       'len'    : 20  }))
)
list_data.set_text_style(style_settings) # set_listの前

# ３次元目に各テキストデータが格納されているので、keep_start=3にして実行
set_datas = list_data.set_list(guide=True,keep_start=1,keep_range='all') 

# スクリプトが存在するディレクトリを基準にする
set_data_write = file_relative_access('./output_txtfile/set_data.txt')

with open(set_data_write,'w') as f:
    for line in set_datas['grid_slice']:
        f.write(line)

# pick表示を行う
#list_data.pick_guideprint(file_relative_access('./output_txtfile/pick_guide.txt'))


# style_settings = (

#    (("Collections" ,
#      {  'image'   : { 'list'    : '►list' ,
#                       'tuple'   : '▷tuple' ,
#                       'ndarray' : '>numpy' ,

#     ("bracket"     ,
#      { 'partially': { 'list'    : ( '{' ・ ')' ),
#                       'tuple'   : ( '<' ・ '>' ),
#                       'ndarray' : ( '(' ・ '}' ),
#                       'None'    : ( '`' ・ '`' ),

#     ("empty"       , { 'style'  : ' ' ),
#     ("padding"     , { 'style'  : '-' ),

#     ("progress"    , { 'print'  :  False  ,
#                        'len'    :  20  }))
# )
