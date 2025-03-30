# / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test /
#print('\n'+'/ \033[38;2;255;165;0m\033[1mtest\033[0m / \033[38;5;27mtest\033[0m '*10+'/\n')

# / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict /
#print('\n'+'/ \033[38;5;27mdemo\033[0m / \033[38;2;255;165;0m\033[1mdict\033[0m '*10+'/\n')

# 実行コード
# from test_setprint_0_3_0 import SetPrint
from demo_setprint_0_3_0 import SetPrint

import numpy as np
import pickle

from PIL import Image

if False:
      def load_pkl_file(filename: str) -> np.ndarray:
            """
            pklファイルから"Alltxtdatas"を抽出し、NumPy配列として返す。
            
            Parameters:
                  filename (str): pklファイルのパス

            Returns:
                  np.ndarray: 2値化マトリックスデータ
            """
            with open(filename, 'rb') as f:
                  data = pickle.load(f)
            return data["Alltxtdatas"]

      # pklファイルからデータを取得
      pkl_filename = '/Users/matsuurakenshin/WorkSpace/development/setprint_package/Development_files/format_data/resized_ocr_txtdata.pkl'
      #pkl_filename = '/Users/matsuurakenshin/WorkSpace/development/setprint_package/Development_files/format_data/ocr_txtdata.pkl'
      test_data = load_pkl_file(pkl_filename)

      keep_settings = ({1:'y',2:'x',3:'yf',4:'f'},{1:'x',2:'yf',3:'f'},{1:'yf',2:'f'})
      indexs = [0]
      for index in indexs:
            test_data = test_data[index]
      keep_settings = keep_settings[len(indexs)]
      
else:
      if True:
            test_data = [
                [[1,2,3], [4,5,6]],
                [[7,8,9], [10,11,12]]
            ]

            # test_data = np.random.randint(0, 256, (4, 4, 3)),  # RGB画像 (3x3x3)
            
            # print(test_data)

            test_data = np.array([[[ 57, 245,  60],
                  [ 84,   0,  11],
                  [217,  36, 184],
                  [ 14,  73, 147]],

                  [[ 64,  21,  51],
                  [ 42,  68, 161],
                  [228, 210,  56],
                  [144, 134, 200]],

                  [[ 15, 169,  72],
                  [103, 161,  76],
                  [ 76, 121, 105],
                  [172,  31, 100]],

                  [[231, 171,  46],
                  [246,  28, 200],
                  [ 44, 176, 183],
                  [ 58, 115, 217]]])
            
            test_data = [
    
                  # RGB画像 (3x3x3) # サンプルの配列 
                  np.array([[[255,   0,   4],
                              [255,  85,   0],
                              [255, 170,   0]],

                              [[170, 255,   0],
                              [ 85, 255,   0],
                              [  0, 255,   4]],

                              [[  0, 170, 255],
                              [  0,  85, 255],
                              [  4,   0, 255]]]),
                  
                  # サンプルの形式違い BGR画像
                  np.array([[[  4,   0, 255],
                              [  0,  85, 255],
                              [  0, 170, 255]],

                              [[  0, 255, 170],
                              [  0, 255,  85],
                              [  4, 255,   0]],

                              [[255, 170,   0],
                              [255,  85,   0],
                              [255,   0,   4]]]),

                  # グレースケール画像 (3x3) → ここだけ次元が異なる
                  np.array([[ 77, 126, 176],
                              [200, 175, 150],
                              [129,  79,  29]]),

                  None

                  ]


            # test_data = np.array([[[197,   1, 169],
            #       [136,  33, 159],
            #       [116, 217, 153],
            #       [156, 132, 140],
            #       [ 18, 195,  76],
            #       [249, 152,  56],
            #       [108,  59, 149],
            #       [ 55, 151, 157],
            #       [ 63,  81, 190],
            #       [ 84, 119, 119]],

            #       [[109,  97, 102],
            #       [138,  84, 254],
            #       [253,  23, 249],
            #       [ 45, 138, 102],
            #       [130, 166, 196],
            #       [143,  20, 100],
            #       [151,  78, 207],
            #       [106,  96, 145],
            #       [124, 129,  27],
            #       [132,  63, 181]],

            #       [[184,  42, 198],
            #       [  8,  32, 227],
            #       [155, 216,  40],
            #       [238,  13, 197],
            #       [ 17, 106, 186],
            #       [157,  28, 244],
            #       [ 52, 211, 241],
            #       [ 80,   3, 140],
            #       [ 24, 143,  54],
            #       [ 19, 143, 222]]])

            # test_data = [[0,[0,0],0],[0,0,0,0]]

            # test_data = np.array([[[ 57, 233, 198],
            #    [122, 193,  78],
            #    [ 87,  68,  15]],

            #   [[ 21,  45,  99],
            #    [154, 214, 132],
            #    [243, 128,  56]],

            #   [[ 72,  94,  45],
            #    [187,  29,  67],
            #    [124, 232, 190]]]),

            # np.array([[ 58, 167, 205],
            #       [134,  77,  49],
            #       [ 72,  98,  36]]),

            # np.array([[[201,  86,  52],
            #       [ 27, 123, 111],
            #       [ 78, 239, 194]],

            #       [[ 94, 208, 193],
            #       [234,  98,  72],
            #       [ 43,  57,  65]],

            #       [[  9,  14, 186],
            #       [  8, 129, 244],
            #       [168,  55, 210]]]),

            # None]
            
            test_data = [{'a':0},1,2,3,[''],4]
            keep_settings = {1:'x'}

      else:

            test_data = {
                  'template':[[1,2,3]],   #見本
                  'bug':[[4,{'bug':5},6], [7,8,9]], #バグあり配列
                  'bul':[]

            }
            # test_data = [['{0}-0', '{0}-1', '{0}-2'], ['{1}-0', ['1-{1}-0', ['1-{1}-1-0']], '{1}-2'], ['{2}-0', ['2-{1}-0', '2-{1}-1'], '{2}-2']]
            # test_data = {1:'x',2:'y',3:'x',4:'x'}
            # test_data = [[[[0,[0,0,0]],0,0],[[0,[0,0]],0,0]],[[[0,[0,0]],0,0,0],[0,0,0]],[[0,0,0],[0,0,0,0]],{'zero':[0,{'zero':[0,0,0,0],'one':[0,0,0,0],},0,0],'one':[0,0,0,0],}]

            
            # 親要素別での配列の順序の合致を調べる。

            '''全ての格納値の配列の順序の合致を調べる。
            配列の順序/全要素 : 配列の次元/ーー'''
            keep_settings = {1:'y'}

            '''親要素毎に格納値の配列の順序の合致を調べる。
            親要素毎に格納値の配列の次元の合致を調べる。
            配列の順序/親要素毎 : 配列の次元/親要素毎'''
            keep_settings = {1:'x',2:'y'}

            '''親要素毎に格納値の配列の次元の合致を調べる。
            親要素毎に格納値の配列の順序の合致を調べる。
            配列の順序/親要素毎 : 配列の次元/親要素毎'''
            keep_settings = {1:'y',2:'x'}

            keep_settings = {1:'y',2:'x',3:'y'}
            # keep_settings = {1:'x'}
            '''全ての格納値の配列の次元の合致を調べる。
            配列の順序/全要素 : 配列の次元/ーー'''
            # keep_settings = {1:'x'}
            
      # keep_settings = {1:'y',2:'x',4:'f'}

      # test_data = [
      #     [[1,2,3], [4,5,6]],
      #     [[7,8,9], [10,11,12]]
      # ]

      # 画像ファイルのパスを指定
      # image_path ='/Users/matsuurakenshin/WorkSpace/kekyu.jpeg'
      # # 画像を読み込む
      # image = Image.open(image_path)

      # # NumPy 配列に変換
      # np_array = np.array(image)

      # print(np_array)

# keep_settings = {1:'x',2:'yf',10:'y'}
# keep_settings = {1:'y',2:'x',3:'yf',10:'y'}


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

with open('/Users/matsuurakenshin/WorkSpace/development/setprint_package/Development_files/format_data/output.txt','w') as f:
      for line in format_texts:
            f.write(line+'\n')
