# / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test /
#print('\n'+'/ \033[38;2;255;165;0m\033[1mtest\033[0m / \033[38;5;27mtest\033[0m '*10+'/\n')

# / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict /
#print('\n'+'/ \033[38;5;27mdemo\033[0m / \033[38;2;255;165;0m\033[1mdict\033[0m '*10+'/\n')

# 実行コード
# from test_setprint_0_3_0 import SetPrint
from demo_setprint_0_3_0 import SetPrint

import numpy as np
import pickle

if True:
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

      keep_settings = ({1:'y',2:'x',3:'yf',10:'y'},{1:'x',2:'yf',10:'y'},{1:'yf',10:'y'})
      indexs = []
      for index in indexs:
            test_data = test_data[index]
      keep_settings = keep_settings[len(indexs)]
      # keep_settings = {1:'y',10:None}
      print(keep_settings)

else:
      test_data = [
          [[1,2,3], [4,5,6]],
          [[7,8,9], [10,11,12]]
      ]

      keep_settings = {1:'yf',10:'y'}

      # test_data = [
      #     [[1,2,3], [4,5,6]],
      #     [[7,8,9], [10,11,12]]
      # ]

# keep_settings = {1:'x',2:'yf',10:'y'}
# keep_settings = {1:'y',2:'x',3:'yf',10:'y'}


# インスタンスを生成
list_data = SetPrint(test_data)

# 整形
format_texts = list_data.set_list ( route='maintenance', keep_settings=keep_settings )

with open('/Users/matsuurakenshin/WorkSpace/development/setprint_package/Development_files/format_data/output.txt','w') as f:
      for line in format_texts:
            f.write(line+'\n')

'''

data 

[
    [  [ ['(0)-{0}-0','(0)-{0}-1'],['(0)-{0}-2','(0)-{0}-3'] ], [ ['(0)-{1}-0','(0)-{1}-1'],['(0)-{1}-2','(0)-{1}-3'] ]  ],
    [  [ ['(1)-{0}-0','(1)-{0}-1'],[

                                     [['(1)-(0)-{0}-0','(1)-(0)-{0}-1'],['(1)-(0)-{0}-2','(1)-(0)-{0}-3'] ]
                                       
                                               ,'(1)-{0}-3'] ], [ ['(1)-{1}-0','(1)-{1}-1'],['(1)-{1}-2','(1)-{1}-3'] ]  ],
]
                                               
keep_settings
{1:'x',2:'y',3:'yf',5:'yf',10:'x'}

    all_deep_settings
    ['x', 'y', 'yf', 'f', 'yf', 'f', 'f', 'f', 'f', 'x']    
    
X_keep_index
(0,) []
(0, 'y') []
(0, 'y', 'yf') [[-1], [0], [1], [2]]
(1,) []
(1, 'y') []
(1, 'y', 'yf') [[-1], [0], [1], [2]]
(1, 'y', 'yf', 0, 'yf') [[-1], [0], [1], [2]]
(2,) []
(2, 'y') []
(2, 'y', 'yf') [[-1], [0], [1], [2]]

flat_X_keep_index
[[5, [[5, [[5, [9, 9]]]]]], [5, [[5, [[5, [[9, [[5, [13, 13]]]], 9]]]]]], [5, [[5, [[5, [9, 9]]]]]]]

Y_keep_index
(0,) [[[], [[0]]], [[], [[1]]], [[], [[2]]]]
(0, 0) [[[0], [[0]]], [[1], [[0]]], [[2], [[0]]]]
(0, 0, 0) [[[0, 0, 0], [[], [0], [1]]], [[1, 0, 0], [[], [0], [1]]], [[2, 0, 0], [[], [0], [1]]]]
(0, 0, 1) [[[0, 0, 1], [[], [0], [1]]], [[1, 0, 1], [[], [0], [1]]], [[2, 0, 1], [[], [0], [1]]]]
(0, 1) [[[0], [[1]]], [[1], [[1]]]]
(0, 1, 0) [[[0, 1, 0], [[], [0], [1]]], [[1, 1, 0], [[], [0], [1]]]]
(0, 1, 1) [[[0, 1, 1], [[], [0], [1]]], [[1, 1, 1], [[], [0], [1]]]]
(0, 0, 1, 0, 0) [[[1, 0, 1, 0, 0], [[], [0], [1]]]]
(0, 0, 1, 0, 1) [[[1, 0, 1, 0, 1], [[], [0], [1]]]]

run_tracking
[[5], [6], [[5], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [8]], [9], [6], [[5], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 2], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [2, 4], [2, 1], [2, 3], [4]], [9], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [8]], [9], [6], [[5], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [8]], [9], [8]]


out_put
---------------------------------------------------------------------------------------------------------------------------------------------------------

***** 
      :::::                                 :::::                                                                   ::::: 
            :::::                                 :::::                                                                   ::::: 
                  ::::: (0)-{0}-0 (0)-{0}-1             ::::: (1)-{0}-0                                   (1)-{0}-1             ::::: (2)-{0}-0 (2)-{0}-1 
                  ::::: (0)-{0}-2 (0)-{0}-3             ::::: :::::::::                                   (1)-{0}-3             ::::: (2)-{0}-2 (2)-{0}-3 
                                                                        ::::: (1)-(0)-{2}-0 (1)-(0)-{2}-1 
                                                                        ::::: (1)-(0)-{2}-2 (1)-(0)-{2}-3 
            :::::                                 ::::: 
                  ::::: (0)-{1}-0 (0)-{1}-1             ::::: (1)-{1}-0                                   (1)-{1}-1 
                  ::::: (0)-{1}-2 (0)-{1}-3             ::::: (1)-{1}-2                                   (1)-{1}-3 

---------------------------------------------------------------------------------------------------------------------------------------------------------


out_put / with_route
---------------------------------------------------------------------------------------------------------------------------------------------------------

***** ━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
      :::::                                 :::::                                                                   ::::: 
        ┣━━ :::::                             ┣━━ :::::                                                               ┗━━ ::::: 
        ┃     ┣━━ ::::: (0)-{0}-0 (0)-{0}-1   ┃     ┣━━ ::::: (1)-{0}-0                                   (1)-{0}-1         ┣━━ ::::: (2)-{0}-0 (2)-{0}-1 
        ┃     ┗━━ ::::: (0)-{0}-2 (0)-{0}-3   ┃     ┗━━ ::::: :::::::::                                   (1)-{0}-3         ┗━━ ::::: (2)-{0}-2 (2)-{0}-3 
        ┃                                     ┃                   ┣━━━━ ::::: (1)-(0)-{2}-0 (1)-(0)-{2}-1 
        ┃                                     ┃                   ┗━━━━ ::::: (1)-(0)-{2}-2 (1)-(0)-{2}-3 
        ┗━━ :::::                             ┗━━ ::::: 
              ┣━━ ::::: (0)-{1}-0 (0)-{1}-1         ┣━━ ::::: (1)-{1}-0                                   (1)-{1}-1 
              ┗━━ ::::: (0)-{1}-2 (0)-{1}-3         ┗━━ ::::: (1)-{1}-2                                   (1)-{1}-3 

---------------------------------------------------------------------------------------------------------------------------------------------------------

'''