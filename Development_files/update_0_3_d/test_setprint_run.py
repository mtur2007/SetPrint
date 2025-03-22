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
      # test_data = [
      #     [[1,2,3], [4,5,6]],
      #     [[7,8,9], [10,11,12]]
      # ]
      # test_data = [
      # np.random.randint(0, 256, (3, 3, 3)),  # RGB画像 (3x3x3)
      # np.random.randint(0, 256, (3, 3)),  # グレースケール画像 (3x3) → ここだけ次元が異なる
      # np.random.randint(0, 256, (3, 3, 3)),  # RGB画像 (3x3x3)

      # None  # データの欠落
      # ]
      
      test_data = [[[0,[0,0],0],[0,0,0,0]],[[1,[1,1],1],[1,1,1,1]]]

      test_data = [np.array([[[ 57, 233, 198],
         [122, 193,  78],
         [ 87,  68,  15]],

        [[ 21,  45,  99],
         [154, 214, 132],
         [243, 128,  56]],

        [[ 72,  94,  45],
         [187,  29,  67],
         [124, 232, 190]]]),

      np.array([[ 58, 167, 205],
            [134,  77,  49],
            [ 72,  98,  36]]),

      np.array([[[201,  86,  52],
            [ 27, 123, 111],
            [ 78, 239, 194]],

            [[ 94, 208, 193],
            [234,  98,  72],
            [ 43,  57,  65]],

            [[  9,  14, 186],
            [  8, 129, 244],
            [168,  55, 210]]]),

      None]
      
      test_data = [
                [[1,2,3], [4,5,6]],
                [[7,8,9], [10,11,12]]
            ]
      # test_data = {1:'x',2:'y',3:'x',4:'x'}
      # test_data = [[[[0,[0,0,0]],0,0],[[0,[0,0]],0,0]],[[[0,[0,0]],0,0,0],[0,0,0]],[[0,0,0],[0,0,0,0]],{'zero':[0,{'zero':[0,0,0,0],'one':[0,0,0,0],},0,0],'one':[0,0,0,0],}]

      keep_settings = {1:'yf'}

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
format_texts = list_data.set_collection ( route='maintenance', keep_settings=keep_settings )
# format_texts = list_data.set_list ( route=True, keep_settings=keep_settings )

with open('/Users/matsuurakenshin/WorkSpace/development/setprint_package/Development_files/format_data/output.txt','w') as f:
      for line in format_texts:
            f.write(line+'\n')
