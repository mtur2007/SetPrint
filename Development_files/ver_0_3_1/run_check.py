# / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test /
#print('\n'+'/ \033[38;2;255;165;0m\033[1mtest\033[0m / \033[38;5;27mtest\033[0m '*10+'/\n')

# / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict /
#print('\n'+'/ \033[38;5;27mdemo\033[0m / \033[38;2;255;165;0m\033[1mdict\033[0m '*10+'/\n')

# 実行コード
# from test_setprint_0_3_0 import SetPrint
import setprint
from development_ver_0_3_1 import SetPrint

import importlib

import numpy as np

def print_set_collection(test_array,style_settings,keep_settings):
      importlib.reload(setprint)
      # インスタンスを生成
      list_data = SetPrint(test_array)

      if style_settings != None:
            list_data.update_data_with_arguments(style_settings)

      # 整形
      format_texts = list_data.set_collection ( route=True, y_axis=True, keep_settings=keep_settings )
      # format_texts = list_data.set_list ( route=True, keep_settings=keep_settings )
      for line in format_texts:
           print(line)
      
      return format_texts

x_Y = {1:'x',2:'y'}
#              ^^^
y_X = {1:'y',2:'x'}
#              ^^^
x_YF = {1:'x',2:'yf'}
#               ^^^^

yf_F = {1:'yf',2:'f'}
#                ^^^
yf_F_Y = {1:'yf',2:'f' , 4:'y'}
#                  ^^^   *****

if True:
      
      '''
      1, 配列型の可変表示 & 空配列へのアクセス防止機能確認
      '''

      #=======================================================
      # < sq : sq >
      
      # シーケンス型同士での可変表示調査
      sq_sq = [([],()),
               ((),[])]
      
      #=======================================================
      # < sq : mp >
      
      # sq > mp [ シーケンス型の値が最大長になるか ]
      sq_mp = [([],{}),
               ({},[])]
      
      # mp > sq [ マッピング型の値が最大長になるか ]
      mp_sq = [({},()),
               ((),{})]
      
      #=======================================================
      # < mp : mp >

      # マッピング型同士での可変表示調査
      mp_mp = [({},{}),
               ({},{})]
      
      #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      
      style_settings = (

        ("Collections" ,
                {'image': { 'list'  : '++++++' ,
                            'tuple' : '---',}}),
        )
      
      keep_settings = x_YF
      print_set_collection(sq_sq,style_settings,keep_settings)
      print_set_collection(sq_mp,style_settings,keep_settings)
      print_set_collection(mp_sq,style_settings,keep_settings)
      print_set_collection(mp_mp,style_settings,keep_settings)

elif False:

      '''
      2, 文字列の可変表示 & 空文字の1文字化確認
      '''

      # < sq : sq > 
      sq_sq = (('++++','--',''),
               ('--','++++',''))
    
      #=======================================================
      # < sq : mp > 

      # sq > mp
      sq_mp = ((('++++',),{'one':'--'},{'len_0':''}),
               ({'two':'--'},('++++',),('',)))
      # sq > mp
      sq_mp = ((('++++',),{'one':'--'},{'len_0':''}),
               ({'two':'--'},('++++',),('',)))

      # mp > sq
      mp_sq = (({'one':'++++'},('--',),('',)),
               (('--',),{'two':'++++'},{'len_0':''}))
      
      #=======================================================
      # < mp : mp >
      mp_mp = (({'one':'++++'},{'two':'--'},{'len_0':''}),
               ({'two':'--'},{'two':'++++'},{'len_0':''}))
      
      style_settings = None
      keep_settings = {1:'yf'}
      print_set_collection(sq_sq,style_settings,keep_settings)
      print_set_collection(sq_mp,style_settings,keep_settings)
      print_set_collection(mp_sq,style_settings,keep_settings)
      print_set_collection(mp_mp,style_settings,keep_settings)

else:
      
      '''
      2,
         次元の合致 & 空配列へのアクセス防止機能(stop) & 空文字の1文字化 確認
         順序の合致 & 空配列へのアクセス防止機能(stop) & 空文字の1文字化 確認
      '''
      
      # 合致            
      # ネストの深さ    |     mp > sq     |  　 sq > m p    |
      Match =      ((0,{'nest+1':'1-0'},'2',('3-0',),'4',  5),
                    (0,'1',{'nest+1':'2-0'},'3',  ('4-0',),5),
                    (0,1,       2,       3,       4,       5),
                    (0,('1-0',),('2-0',),('3-0',),('4-0',),5))
    
      # 合致 & 空配列へのアクセス防止機能(stop)
      match_stop = ((0,    {},  '2',         (),  '4',     5),
                    (0,'1',         {},  '3',        (),   5),
                    (0,1,       2,       3,       4,       5),
                    (0,('1-0',),('2-0',),('3-0',),('4-0',),5))
    
      # 合致 & 空文字の1文字化
      match_max1 = ((0,  {'+1':''},'2',  ('',),   '4',      5),
                    (0,'1',      {'+1':''},'3',     ('',),  5),
                    (0,1,        2,       3,       4,       5),
                    (0, ('1-0',),('2-0',),('3-0',),('4-0',),5))

      style_settings = None
      keep_settings = yf_F

      format_txt = print_set_collection(Match,style_settings,keep_settings)
      format_txt = print_set_collection(match_stop,style_settings,keep_settings)
      format_txt = print_set_collection(match_max1,style_settings,keep_settings)

