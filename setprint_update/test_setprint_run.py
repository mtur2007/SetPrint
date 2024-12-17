
# 実行コード
import pickle
from test_setprint_0_3_0 import SetPrint

import os

# pickleファイルからデータを読み込む
file_name = 'ocr_txtdata.pkl'
with open(file_name, "rb") as file:
      loaded_data = pickle.load(file)

# keyを指定してテキストデータを取得
txt_data = loaded_data["Alltxtdatas"]

list_data = SetPrint(txt_data)

arguments = (
                    
    (("Collections" , 
        { 'image'    : {'list'   :'►list',
                        'tuple'  :'▷tuple',
                        'ndarray':'>numpy'}}),
    ("bracket"     , 
        { 'partially': {'list'   :('{',')'),                 
                        'tuple'  :('<','>'),
                        'ndarray':('(','}'),
                        'None'   :('`','`')}}),
                                        
    ("empty"       , { 'style' : ' '}),
    ("padding"     , { 'style' : '-'}),

    ("settings"    , { 'print' : True }), # <- New  True (display) / False (hide)

    ("progress"    , { 'print' : False ,   # <- New  True (display) / False (hide)
                        'len'   : 20 }))

    
)

list_data.set_text_style(arguments) # set_listの前

# ３次元目に各テキストデータが格納されているので、keep_start=3にして実行
set_datas = list_data.set_list(guide=True,keep_start=3,keep_range='all') 

# スクリプトが存在するディレクトリを基準にする
base_dir = os.path.dirname(os.path.abspath(__file__))
set_data_write = os.path.join(base_dir, './output_txtfile/set_data.txt')

with open(set_data_write,'w') as f:
    for line in set_datas['grid_slice']:
        f.write(line)


# # スクリプトが存在するディレクトリを基準にする
# base_dir = os.path.dirname(os.path.abspath(__file__))
# pick_guide = os.path.join(base_dir, './output_txtfile/pick_guide.txt')
# list_data.pick_guideprint(pick_guide)


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

