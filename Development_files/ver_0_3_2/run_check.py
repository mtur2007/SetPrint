# / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test /
#print('\n'+'/ \033[38;2;255;165;0m\033[1mtest\033[0m / \033[38;5;27mtest\033[0m '*10+'/\n')

# / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict /
#print('\n'+'/ \033[38;5;27mdemo\033[0m / \033[38;2;255;165;0m\033[1mdict\033[0m '*10+'/\n')

# 実行コード
from setprint import SetPrint
# from development_ver_0_3_2 import SetPrint
import numpy as np

import sys
import os

# 親ディレクトリをimportパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Nadarray_SideBySide_Layout import combine_blocks_with_block_titles

def cut_blocks_from_index(blocks, start=2):
    """
    各ブロック（リスト）の start番目以降だけを取り出す。
    """
    return [block[start:] for block in blocks]

def print_set_collection(test_array,style_settings,keep_settings):
      # インスタンスを生成
      list_data = SetPrint(test_array)

      if style_settings != None:
            list_data.update_data_with_arguments(style_settings)

      # 整形
      format_texts = list_data.set_collection ( route='SLIM', y_axis=True, keep_settings=keep_settings)
      # format_texts = list_data.set_list ( route=True, keep_settings=keep_settings )
    #   for line in format_texts:
    #        print(line)
      
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

style_settings = (

      ("Collections" ,
       {  'image'   : { 'list'    : '►list' ,
                        'tuple'   : '▷tuple' ,
                        'ndarray' : '>ndarray' ,
                        'dict'    : '◆dict' }}),
      
      ("route",
       {  'image'   : { '┣' : '├' ,
                        '┳' : '┬' ,

                        '┃' : '│' ,
                        '━' : '─' ,

                        '┗' : '└' ,
                        '┓' : '┐' }})

      )

if False:
      
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
      

      x_Y = {1:'x',2:'y'}              # yでの正常動作テスト
      #              ^^^
      y_X = {1:'y',2:'x'}              # xでの正常動作テスト
      #              ^^^
      x_YF = {1:'x',2:'yf'}            # yfでの正常動作テスト
      #               ^^^^

      yf_F = {1:'yf',2:'f'}            # fでの正常動作テスト, 
      #                ^^^
      yf_F_Y = {1:'yf',2:'f' , 3:'y'}  # fでの正常動作テスト, 末端指定
      #                  ^^^   *****

      keep_settings = x_Y
      # keep_settings = y_X
      # keep_settings = x_YF
      # keep_settings = yf_F
    #   keep_settings = yf_F_Y
      
      format_txt = [
            print_set_collection(sq_sq,style_settings,keep_settings),
            print_set_collection(sq_mp,style_settings,keep_settings),
            print_set_collection(mp_sq,style_settings,keep_settings),
            print_set_collection(mp_mp,style_settings,keep_settings)
      ]

elif True:

    '''
    2, スカラー型の可変表示 & 空文字の1文字化確認(max_1)
    '''
    # < sq : sq >

    # sq : sq
    sq_sq_str = (
                  (('++++','--',''),
                   ('--','++++',''))
                )
    
    # # [ str : str ]
    # MAX = '++++'
    # min = '--'    
    
    # sq_sq = (((MAX,min,''),
    #           (min,MAX,'')),((min,MAX,''),
    #                          (MAX,min,'')))


    # int : int
    sq_sq_int = (
                  ((1000, 10,''),
                   (10 , 1000,''))
                 )
    
    # flot : flot
    sq_sq_flot = (
                   ((1000.0, 10.0,''),
                    (10.0 , 1000.0,''))
                  )

    # int : flot
    sq_sq_int_flot = ( # [ > ]
                       (( 1000, 1.0,  ''),
                        ( 1.0,  1000, '')),
                       # [ < ]
                       (( 1000.0, 10, ''),
                        ( 10, 1000.0, ''))
                      )
    
    # str : int
    sq_sq_str_int = ( # [ > ]
                      (( '++++', 10,  ''),
                       ( 10 , '++++', '')),
                      # [ < ]
                      (( 1000, '--', ''),
                       ( '--', 1000, ''))
                     )
    
    # str : int
    sq_sq_str_flot = ( # [ > ]
                       (( '++++', 1.0,  ''),
                        ( 1.0 , '++++', '')),
                       # [ < ]
                       (( 1000.0, '--', ''),
                        ( '--', 1000.0, ''))
                      )
        
    #=======================================================
    # < sq : mp > 

    # / sq > mp /

    # str : str
    sq_mp_str = (
                  (( ('++++',),{'two':'--'},{'len_0':''}),
                   ( {'one':'--'},('++++',),('',)))
                 )
    
    # int : int
    sq_mp_int = (
                  (( (1000,),{'two':10},{'len_0':''}),
                   ( {'one':10},(1000,),('',)))
                 )
    
    # flot : flot
    sq_mp_flot = (
                   (((1000.0,),{'two':10.0},{'len_0':''}),
                    ({'one':10.0},(1000.0,),('',)))
                  )
    
    # int : flot
    sq_mp_int_flot = ( # >
                       (( (1000,),{'two':1.0}, {'len_0':''}),
                        ( {'one':1.0},(1000,), ('',))),

                       # <
                       (( (1000.0,),{'two':10} ),
                        ( {'one':10},(1000.0,) ))
                      )
    
    # str : int
    sq_mp_str_int = ( # >
                      (( ('++++',),{'two':10}, {'len_0':''}),
                       ( {'one':10},('++++',), ('',)  )),

                      # <
                      (( (1000,),{'one':'--'}),
                       ( {'one':'--'},(1000,)))
                     )
    
    # str : flot
    sq_mp_str_flot = ( # >
                       (( ('++++',),{'two':10.0}, {'len_0':''} ),
                        ( {'one':10.0},('++++',), ('',)        )),

                       # < 
                       (( (1000.0,),{'twe':'--'}),
                        ( {'one':'--'},(1000.0,)))
                      )

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    
    # \ mp > sq \

    # str : str
    mp_sq_str = (
                  (({'one':'++++'},('--',),('',)),
                   (('--',),{'two':'++++'},{'len_0':''}))
                 )
    
    # int : int
    mp_sq_int = (
                  (({'one':1000},(10,),('',)),
                   ((10,),{'two':1000},{'len_0':''}))
                 )
    
    # flot : flot
    mp_sq_flot = (
                   (({'one':1000.0},(10.0,),('',)),
                    ((10.0,),{'two':1000.0},{'len_0':''}))
                  )
    
    # int : flot
    mp_sq_int_flot = ( # >
                       (( {'one':1000},(1.0,), ('',)),
                        ( (1.0,),{'two':1000}, {'len_0':''})),

                       # <
                       (( {'one':1000.0},(10,)),
                        ( (10,),{'two':1000.0}))
                      )
    
    # str : int
    mp_sq_str_int = ( # >   
                      (( {'one':'++++'},(10,), ('',)),
                       ( (10,),{'two':'++++'}, {'len_0':''})),

                      # <
                      (( {'one':1000},('--',), ('',)),
                       ( ('--',),{'two':1000}, {'len_0':''}))
                     )
    
    # str : flot
    mp_sq_str_flot = ( # >    
                       (( {'one':'++++'},(1.0,), ('',)),
                        ( (1.0,),{'two':'++++'}, {'len_0':''})),

                       # <
                       (( {'one':1000.0},('--',), ('',)),
                        ( ('--',),{'two':1000.0}, {'len_0':''}))
                     )

    #=======================================================
    # < mp : mp >

    # str : str
    mp_mp_str = (
                  (({'one':'++++'},{'two':'--'},{'len_0':''}),
                   ({'two':'--'},{'two':'++++'},{'len_0':''}))
                 )
    
     # int : int
    mp_mp_int = (
                  (({'one':1000},{'two':10},{'len_0':''}),
                   ({'two':10},{'two':1000},{'len_0':''}))
                 )
    
    # flot: flot
    mp_mp_flot = (
                   (({'one':1000.0},{'two':10.0},{'len_0':''}),
                    ({'two':10.0},{'two':1000.0},{'len_0':''}))
                  )
    
    # int : flot
    mp_mp_int_flot = ( # [ > ]
                       (( {'one':1000},{'two':1.0},{'len_0':''}),
                        ( {'two':1.0},{'two':1000},{'len_0':''})),
                       # [ < ]
                       (( {'one':10},{'two':1000.0},{'len_0':''}),
                        ( {'two':1000.0},{'two':10},{'len_0':''}))
                      )
    
    # str : int
    mp_mp_str_int = ( # [ > ]
                      (( {'one':'++++'},{'two':10},{'len_0':''}),
                       ( {'two':10},{'two':'++++'},{'len_0':''})),
                      # [ < ]
                      (( {'one':1000},{'two':'--'},{'len_0':''}),
                       ( {'two':'--'},{'two':1000},{'len_0':''}))
                     )
    
    # str : flot
    mp_mp_str_flot = ( # [ > ]
                       (( {'one':'++++'},{'two':1.0},{'len_0':''}),
                        ( {'two':1.0},{'two':'++++'},{'len_0':''})),
                       # [ < ]
                       (( {'one':1000.0},{'two':'--'},{'len_0':''}),
                        ( {'two':'--'},{'two':1000.0},{'len_0':''}))
                      )
    

    x_Y = {1:'x',2:'y'}              # yでの正常動作テスト
    #              ^^^
    y_X = {1:'y',2:'x'}              # xでの正常動作テスト
    #              ^^^
    x_YF_sq = {1:'x',2:'yf'}         # yfでの正常動作テスト(シーケンス型用)
    x_YF_mp = {1:'x',2:'y',3:'yf'}   # yfでの正常動作テスト(マッピング型用)
    #                        ^^^^

    yf_F = {1:'yf',2:'f'}            # fでの正常動作テスト, 
    #                ^^^
    yf_F_Y = {1:'yf',2:'f' , 3:'y'}  # fでの正常動作テスト, 末端指定
    #                  ^^^   *****

    # x
    # original = {1:'y',2:'x'}
    # original_1 = {1:'x',2:'y',3:'x'}
    
    # f
    # original = {1:'yf'}
    # original_1 = {1:'x',2:'yf'}

    # y
    # original = {1:'x',2:'y'}
    # original_1 = {1:'x',2:'x',3:'y'}
    
    # yf
    original = {1:'x',2:'yf',3:'yf'}
    original_1 = {1:'x',2:'y',3:'yf',4:'yf'}

    keep_settings = original
    keep_settings_1 = original_1

    sq_sq_format_txt = [

            print_set_collection(sq_sq_str,style_settings,keep_settings),
            print_set_collection(sq_sq_int,style_settings,keep_settings),
            print_set_collection(sq_sq_flot,style_settings,keep_settings),
            print_set_collection(sq_sq_int_flot,style_settings,keep_settings_1),
            print_set_collection(sq_sq_str_int,style_settings,keep_settings_1),
            print_set_collection(sq_sq_str_flot,style_settings,keep_settings_1)
      ]
    
    sq_mp_format_txt = [

            print_set_collection(sq_mp_str,style_settings,keep_settings),
            print_set_collection(sq_mp_int,style_settings,keep_settings),
            print_set_collection(sq_mp_flot,style_settings,keep_settings),
            print_set_collection(sq_mp_int_flot,style_settings,keep_settings_1),
            print_set_collection(sq_mp_str_int,style_settings,keep_settings_1),
            print_set_collection(sq_mp_str_flot,style_settings,keep_settings_1)
      ]
    
    mp_sq_format_txt = [

            print_set_collection(mp_sq_str,style_settings,keep_settings),
            print_set_collection(mp_sq_int,style_settings,keep_settings),
            print_set_collection(mp_sq_flot,style_settings,keep_settings),
            print_set_collection(mp_sq_int_flot,style_settings,keep_settings_1),
            print_set_collection(mp_sq_str_int,style_settings,keep_settings_1),
            print_set_collection(mp_sq_str_flot,style_settings,keep_settings_1)
      ]
    
    mp_mp_format_txt = [

            print_set_collection(mp_mp_str,style_settings,keep_settings),
            print_set_collection(mp_mp_int,style_settings,keep_settings),
            print_set_collection(mp_mp_flot,style_settings,keep_settings),
            print_set_collection(mp_mp_int_flot,style_settings,keep_settings_1),
            print_set_collection(mp_mp_str_int,style_settings,keep_settings_1),
            print_set_collection(mp_mp_str_flot,style_settings,keep_settings_1)
      ]
    
    '''
    keep_settings
    ['x', 'yf']
    -------------------------------

    ▷tuple ──┬───────────┐     ┊   
           ▷tuple  ┊   ▷tuple  ┊   
             ├─── ++++   ├───  --  
             ├───  --    ├─── ++++ 
             └───        └───      

    -------------------------------
    '''


    sq_sq = cut_blocks_from_index(sq_sq_format_txt, start=1)
    sq_mp = cut_blocks_from_index(sq_mp_format_txt, start=1)
    mp_sq = cut_blocks_from_index(mp_sq_format_txt, start=1)
    mp_mp = cut_blocks_from_index(mp_mp_format_txt, start=1)


#     with open ('/Users/matsuurakenshin/WorkSpace/development/setprint_package/Development_files/ver_0_3_2/output.txt','w') as f:

#         line = '-' * 300
#         f.write(combine_blocks_with_block_titles(*sq_sq) + '\n\n'+line+'\n\n')        
#         f.write(combine_blocks_with_block_titles(*sq_mp) + '\n\n'+line+'\n\n')
#         f.write(combine_blocks_with_block_titles(*mp_sq) + '\n\n'+line+'\n\n')        
#         f.write(combine_blocks_with_block_titles(*mp_mp) + '\n\n'+line+'\n\n')

elif False:
      
      '''
      2,
         次元の合致 & 空配列へのアクセス防止機能(stop) & 空文字の1文字化 確認
         順序の合致 & 空配列へのアクセス防止機能(stop) & 空文字の1文字化 確認
      '''

      # 合致            
      # ネストの深さ sq : sq 
      Match_sq_sq = (( ['0-0'], ['1-0'],2,       3,       4),
                     (0,       1,        ['2-0'], ['3-0'],4),
                     (0,       1,       2,       3,       4),
                     (0,        ['1-0'],2,        ['3-0'],4))

      # 合致            
      # ネストの深さ mp : mp 
      Match_mp_mp = ({'zero':{'+1':'0-0'}, 'one':{'+1':'1-0'}, 'two':2,            'three':3,            'four':4},
                     {'zero':0,            'one':1,            'two':{'+1':'2-0'}, 'three':{'+1':'3-0'}, 'four':4},
                     {'zero':0,            'one':1,            'two':2,            'three':3,            'four':4},
                     {'zero':0,            'one':{'+1':'1-0'}, 'two':2,            'three':{'+1':'3-0'}, 'four':4})


      # 合致            
      # ネストの深さ mp > sq 
      Match_mp_sq = (( {'+1':'0-0'}, {'+1':'1-0'},2,            3,            4),
                     (0,            1,             {'+1':'2-0'}, {'+1':'3-0'},4),
                     (0,            1,            2,            3,            4),
                     (0,                  ['1-0'],2,                  ['3-0'],4))
      
      # 合致            
      # ネストの深さ mp : mp 
      Match_sq_mp = ({'zero':['0-0'], 'one':['1-0'], 'two':2,       'three':3,       'four':4},
                     {'zero':0,       'one':1,       'two':['2-0'], 'three':['3-0'], 'four':4},
                     {'zero':0,       'one':1,       'two':2,       'three':3,       'four':4},
                     {'zero':0,       'one':['1-0'], 'two':2,       'three':['3-0'], 'four':4})


      # 合致 & 空配列へのアクセス防止機能(stop)
      match_sq_stop = (( [], [],     2,  3,         {},{},     6,  7,        8),
                       (0,  1,         [], [],     4, 5,         {}, {},     8),
                       (0,   ['1-0'],2,    ['3-0'],4,  ['5-0'],6,    ['7-0'],8))
      
      match_mp_stop = ({'zero':[], 'one':[],      'two':2,  'three':3,       'four':{}, 'five':{},      'six':6,  'seven':7,       'eight':8},
                       {'zero':0,  'one':1,       'two':[], 'three':[],      'four':4,  'five':5,       'six':{}, 'seven':{},      'eight':8},
                       {'zero':0,  'one':1,       'two':2,  'three':3,       'four':4,  'five':5,       'six':6,  'seven':7,       'eight':8},
                       {'zero':0,  'one':['1-0'], 'two':2,  'three':['3-0'], 'four':4,  'five':['5-0'], 'six':6,  'seven':['7-0'], 'eight':8})

      # 合致 & 空配列へのアクセス防止機能(stop)
      match_sq_max1 = (( [''], [''],   2,     3,        {'+1':''},  {'+1':''},6,        7,          8),
                       (0,    1,         [''], [''],   4,          5,          {'+1':''}, {'+1':''},8),
                       (0,     ['1-0'],2,      ['3-0'],4,           ['5-0'],  6,          ['7-0'],  8))
      
      match_mp_max1 = ({'zero':[''], 'one':[''],    'two':2,    'three':3,       'four':{'+1':''}, 'five':{'+1':''}, 'six':6,         'seven':7,         'eight':8},
                       {'zero':0,    'one':1,       'two':[''], 'three':[''],    'four':4,         'five':5,         'six':{'+1':''}, 'seven':{'+1':''}, 'eight':8},
                       {'zero':0,    'one':1,       'two':2,    'three':3,       'four':4,         'five':5,         'six':6,         'seven':7,         'eight':8},
                       {'zero':0,    'one':['1-0'], 'two':2,    'three':['3-0'], 'four':4,         'five':['5-0'],   'six':6,         'seven':['7-0'],   'eight':8})

      x_Y = {1:'x',2:'y'}              # yでの正常動作テスト
      #              ^^^
      y_X = {1:'y',2:'x'}              # xでの正常動作テスト
      #              ^^^
      x_YF_sq = {1:'x',2:'yf'}         # yfでの正常動作テスト(シーケンス型用)
      x_YF_mp = {1:'x',2:'yf',3:'yf'}   # yfでの正常動作テスト(マッピング型用)
      #                        ^^^^

      yf_F = {1:'yf',2:'f'}            # fでの正常動作テスト, 
      #                ^^^
      yf_F_Y = {1:'yf',2:'f' , 3:'y'}  # fでの正常動作テスト, 末端指定
      #                  ^^^   *****

      keep_settings = x_YF_mp

      format_txt = [

            print_set_collection(Match_sq_sq,style_settings,keep_settings),
            print_set_collection(Match_mp_mp,style_settings,keep_settings),
            print_set_collection(Match_mp_sq,style_settings,keep_settings),
            print_set_collection(Match_sq_mp,style_settings,keep_settings),

            print_set_collection(match_sq_stop,style_settings,keep_settings),
            print_set_collection(match_mp_stop,style_settings,keep_settings),

            print_set_collection(match_sq_max1,style_settings,keep_settings),
            print_set_collection(match_mp_stop,style_settings,keep_settings)

      ]

else:
    # test = ['test',[[[]]]]

    # keep_settings = {1:'yf',3:'yf',4:'f'}

    # format_txt = print_set_collection(test,style_settings,keep_settings)

    nest_num = 0
    
    test_array = [[],[]]

    y_nomal = {1: 'y', 2: 'x', 3: 'y', 4: 'x', 5: 'y', 6: 'x'}
    y_flat = {1: 'yf', 2: 'f', 3: 'yf', 4: 'f', 5: 'yf', 6: 'f'}
    y_nomal_flat = {1: 'y', 2: 'x', 3: 'yf', 4: 'f', 5: 'y', 6: 'x'}
    y_flat_nomal = {1: 'yf', 2: 'f', 3: 'y', 4: 'x', 5: 'yf', 6: 'f'}
    
    x_nomal = {1: 'x', 2: 'y', 3: 'x', 4: 'y', 5: 'x', 6: 'y'}
    x_flat = {1: 'x', 2: 'yf', 3: 'f', 4: 'yf', 5: 'f', 6: 'yf'}
    x_nomal_flat = {1: 'x', 2: 'y', 3: 'x', 4: 'yf', 5: 'f', 6: 'y'}
    x_flat_nomal = {1: 'x', 2: 'yf', 3: 'f', 4: 'y', 5: 'x', 6: 'yf'}

    # 辞書型で置き換える入れ子数目
    dict_type = [0,2]

    for num in range(3):
        access_array = test_array
        for i in range(((num) * 2)):
            if type(access_array) == dict:
                access_array = access_array['two']
            else:
                access_array = access_array[1]
        else:
            nest_num += 1

            if num in dict_type:
                
                test_2d = { 'one':[nest_num,nest_num,nest_num],
                            'two':[nest_num,nest_num,nest_num],
                            'three':[nest_num,nest_num,nest_num]}
            else:
                test_2d = [[nest_num,nest_num,nest_num],
                           [nest_num,nest_num,nest_num],
                           [nest_num,nest_num,nest_num]]
            
            access_array[1] = test_2d # copy.deepcopy(test_2d)
                 
    else:
        test_array = test_array[1]

    # インスタンスを生成
    list_data = SetPrint(test_array)
    # 整形
    format_txt = [
        list_data.set_collection ( route='SLIM', y_axis=False, keep_settings=x_nomal ),
        list_data.set_collection ( route='SLIM', y_axis=False, keep_settings=x_flat ),
        list_data.set_collection ( route='SLIM', y_axis=False, keep_settings=x_nomal_flat ),
        list_data.set_collection ( route='SLIM', y_axis=False, keep_settings=x_flat_nomal )
    ]

# cut_format_txt = cut_blocks_from_index(format_txt, start=1)
# # # ✅ 使用例（3ブロック）
# print(combine_blocks_with_block_titles(*cut_format_txt))
