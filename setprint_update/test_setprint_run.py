
# 実行コード
import pickle
from demo_setprint_0_3_0 import SetPrint

import os

# pickleファイルからデータを読み込む
file_name = 'ocr_txtdata.pkl'
with open(file_name, "rb") as file:
      loaded_data = pickle.load(file)

# keyを指定してテキストデータを取得
txt_data = loaded_data["Alltxtdatas"]

# list_data = SetPrint(txt_data)
#list_data = SetPrint(list)

arguments = (
    
   (("Collections" , 
        { 'image'   : {'list'     :'►list',
                        'tuple'   :'▷tuple',
                        'ndarray' :'>numpy',
                        'dict'    :'◆dict'}}),  # < New
    ("bracket"     , 
        { 'partially': {'list'    :('{',')'),                 
                        'tuple'   :('<','>'),
                        'ndarray' :('(','}'),
                        'dict'    :('/','/'),   # < New
                        'None'    :('`','`')}}),
                                        
    ("empty"       , { 'style' : ' '}),
    ("padding"     , { 'style' : '-'}),

    ("settings"    , { 'print' : False }),

    ("progress"    , { 'print' : False ,
                       'len'   : 20}))
)

arguments = (
    
   (("Collections" , 
        { 'image'   : {'list'     :'►',
                        'tuple'   :'▷',
                        'ndarray' :'>',
                        'dict'    :'◆'}}),  # < New
    ("bracket"     , 
        { 'partially': {'list'    :('{',')'),                 
                        'tuple'   :('<','>'),
                        'ndarray' :('(','}'),
                        'dict'    :('/','/'),   # < New
                        'None'    :('`','`')}}),
                                        
    ("empty"       , { 'style' : ' '}),
    ("padding"     , { 'style' : '-'}),

    ("settings"    , { 'print' : True }),

    ("progress"    , { 'print' : False ,
                       'len'   : 20}))
)

# インデックスで引数のチェックを行う為、この配列の通りに指定してください。
# 制限の範囲内ではなかった値は表示され、デフォルトの値が代入されます。

# set_datas = list_data.set_list(guide=True, keep_start=1, keep_range='all')

list_data = SetPrint(arguments)

list_data.set_text_style(arguments) # set_listの前

# ３次元目に各テキストデータが格納されているので、keep_start=3にして実行
set_datas = list_data.set_list(guide=True,keep_start=1,keep_range='all') 

# スクリプトが存在するディレクトリを基準にする
base_dir = os.path.dirname(os.path.abspath(__file__))
set_data_write = os.path.join(base_dir, './output_txtfile/set_data.txt')

with open(set_data_write,'w') as f:
    for line in set_datas['grid_slice']:
        f.write(line)


# スクリプトが存在するディレクトリを基準にする
base_dir = os.path.dirname(os.path.abspath(__file__))
pick_guide = os.path.join(base_dir, './output_txtfile/pick_guide.txt')
list_data.pick_guideprint(pick_guide)


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

