# / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test /
#print('\n'+'/ \033[38;2;255;165;0m\033[1mtest\033[0m / \033[38;5;27mtest\033[0m '*10+'/\n')

# / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict /
#print('\n'+'/ \033[38;5;27mdemo\033[0m / \033[38;2;255;165;0m\033[1mdict\033[0m '*10+'/\n')

# 実行コード
# from test_setprint_0_3_0 import SetPrint
from development_ver_0_3_1 import SetPrint
# from setprint import SetPrint

import numpy as np
import pickle

from PIL import Image

if True:

      style_settings = (

            ("Collections" ,
                  {  'image'   : { 'list'    : '++++++' ,
                              'tuple'   : '---' ,
                              'ndarray' : '>nadarray' ,
                              'dict'    : '◆dict' }}),

            )
      
      test_data = [
      
      # 1. 設定値 y の配列型テキストイメージ、可変表示の確認
      (['+'],('-')),(('-'),['+']),
      
      # 2. 格納値、可変表示の確認
      (['++'],['-']),(['-'],['++']),

      # 3. 空文字の1文字化確認
      (('',0,''),
       ('',0),
       ('',0,'')),
      
      # 4. 空配列へのアクセス防止機能確認
      ((0,0),
       ((),({},),),
       (({},),())),
      
      # 5. 順序の整合化、正常動作確認
      ((2,2),
       ((3,),2),
       (2,(3,)),
       ((3,),(3,))),

      # 6. 設定値 f の配列型テキストイメージ、可変表示の確認
      ((['+'],('-')),
       (('-'),['+']))

      ]

      keep_settings = {1:'x',2:'yf',5:'x'}

'''
keep_settings
['x', 'yf', 'f', 'f', 'x']
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       ✅ (1)           ✅ (1)           ✅ (2)            ✅ (2)            ✅ (3)          ✅ (4)                                  ✅ (5)                          ✅ (6)
++++++ ━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
       ---              ---              ---               ---               ---             ---                                     ---                             --- 
        ┣━ ++++++ [ + ]  ┣━   -           ┣━ ++++++ [ ++ ]  ┣━ ++++++ [ -  ]  ┣━ --- (  0  )  ┣━ --- (  0             0            )  ┣━ --- (  2         2        )  ┣━ --- ( ++++++ [ + ]   -          ) 
        ┗━   -           ┗━ ++++++ [ + ]  ┗━ ++++++ [ -  ]  ┗━ ++++++ [ ++ ]  ┣━ --- (  0  )  ┣━ --- ( --- (       ) --- ( ◆dict ) )  ┣━ --- ( --- ( 3 )  2        )  ┗━ --- (   -          ++++++ [ + ] ) 
                                                                              ┗━ --- (  0  )  ┗━ --- ( --- ( ◆dict ) --- (       ) )  ┣━ --- (  2        --- ( 3 ) ) 
                                                                                                                                      ┗━ --- ( --- ( 3 ) --- ( 3 ) ) 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

# インスタンスを生成
list_data = SetPrint(test_data)

list_data.update_data_with_arguments(style_settings)

# 整形
format_texts = list_data.set_collection ( route=True, keep_settings=keep_settings )
# format_texts = list_data.set_list ( route=True, keep_settings=keep_settings )

with open('/Users/matsuurakenshin/WorkSpace/development/setprint_package/Development_files/ver_0_3_1/output.txt','w') as f:
      for line in format_texts:
            f.write(line+'\n')
