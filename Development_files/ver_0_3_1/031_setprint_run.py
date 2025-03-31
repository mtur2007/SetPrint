# / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test /
#print('\n'+'/ \033[38;2;255;165;0m\033[1mtest\033[0m / \033[38;5;27mtest\033[0m '*10+'/\n')

# 実行コード
# from setprint import SetPrint
from development_ver_0_3_1 import SetPrint

import numpy as np

if False:
      test_data    = [{'bug':0},[['cen|ter']]]
      keep_settings = {1:'yf'}

      # 辞書型との整合性が取れないバグ
      # > デバック済みpythonファイルを間違えたことが原因

      '''
      デバック前                            デバック後
      ------------------------------  ->  ------------------------------
                                      ->  
      ►list                           ->  ►list
        ┣━━ ◆dict                     ->    ┣━━ ◆dict
        ┃     ┗━━   bug  :  0         ->    ┃     ┗━━ bug:  0   
        ┗━━ ►list                     ->    ┗━━ ►list 
              ┗━━ ---.►list           ->          ┗━━ ---.►list 
                      ┗━━━━ cen|ter   ->                  ┗━━━━ cen|ter 
                                      ->  
      ------------------------------  ->  ------------------------------
      '''

elif False:
           
      test_data = [[''],1]
      #             ^^

      keep_settings = {1:'x',2:'x'}
      
      '''
      デバック前             デバック後
      ---------------  ->  ----------------
                       -> 
      ►list ━━┳━━━━┓   ->  ►list ━━┳━━━━━┓
            ►list┓┳ 1  ->        ►list ┓ 1 
                       ->
                       ->
      ---------------  ->  ----------------
      '''
      
      """
      :原因:
      ルートを入れた場合 文字数が0の部分に('┳':文字数1)のものを追加してしまい、差分が+1となってしまう為。
      > 表示する最低文字数を1と設定することで差分が0となり、解消できる。
      """

elif False:

      test_data    = [[[[0,0,0]],[['1--',1,1]],[[2,2,[]]]],[{'one':[0,0,[[0,'',0],[0,0]]]},[[1,1,1]],[[2,2,[]]]],[]]
      keep_settings = {1:'y',2:'x',4:'x',5:'yf'}

      '''

                 インデックスエラー
      
      v v v v v v v v v v v v v v v v v v 

      keep_settings
      ['yf', 'f', 'f', 'x']
      ------------------------------------

      ►list 
        ┣━━ ►list [ ►list [ 0 0   0   ] ] 
        ┣━━ ►list [ ►list [ 1 1   1   ] ] 
        ┣━━ ►list [ ►list [ 2 2 ►list ] ] 
        ┗━━ ►list [                     ] 

      ------------------------------------
      '''

      # 原因
      # ルートの表示の際、空配列にアクセスしようとしてインデックスエラーを引き起こしていた

else:
      test_data = {
      'template':[0,1,2],
      'Expected':[0,['1-0','1-1'],2]
      }
      keep_settings = {1:'x',2:'x'}

# インスタンスを生成
list_data = SetPrint(test_data)

style_settings = (

          ("Collections" ,
            {  'image'   : { 'list'    : '►list' ,
                             'tuple'   : '▷tuple' ,
                             'ndarray' : '>nadarray' ,
                             'dict'    : '◆dict' }}),

        )

list_data.update_data_with_arguments(style_settings)

# 整形
format_texts = list_data.set_collection ( route=True, keep_settings=keep_settings )
# format_texts = list_data.set_list ( route=True, keep_settings=keep_settings )

with open('/Users/matsuurakenshin/WorkSpace/development/setprint_package/Development_files/ver_0_3_1/output.txt','w') as f:
      for line in format_texts:
            f.write(line+'\n')
