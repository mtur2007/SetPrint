# / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test / test /
# print('\n'+'/ \033[38;2;255;165;0m\033[1mtest\033[0m / \033[38;5;27mtest\033[0m '*10+'/\n')

# setpirnt (ver 0.3.0)

import numpy as np
from pynput import keyboard


# 数値の int部分を見た目的に表示させる様にする自作関数
def Myint(num):
    num = str(num)
    for line in range(len(num)):
        if num[line] == ".":
            return int(num[:line])
    return int(num)

'''
=============================================================================================================================================================
・配列の下調べ・簡易的なアクセスを行う関数
'''

# 配列の文字列、数列がどこの次元に位置しているかを調べる関数。(オート機能の処理)
def check_matching_elements(mapping_point, collection_index):

    max_match_count = 0  # 最大連続一致数
    max_match_index = -1  # 最大連続一致数を持つ1次元目のインデックス

    collection_len = len(collection_index)

    for row_index, row in enumerate(mapping_point):
        current_match_count = 0  # 現在の行での連続一致数
        if collection_len >= len(row):
            for i, elem in enumerate(row):
                if i < len(collection_index) and elem == collection_index[i]:
                    current_match_count += 1  # 一致した場合カウントを増やす
                else:
                    break  # 一致が途切れたら終了

            # 最大連続一致数を更新
            if (len(row) == current_match_count) and (current_match_count > max_match_count):
                max_match_count = current_match_count
                max_match_index = row_index

    return max_match_index  # 最大連続一致数を持つ行のインデックス

# リストに格納されている最大要素数とその次元を求める関数
def find_max_elements_and_level(data, depth=0, level_counts=None):
    """
    Find the maximum number of elements and the corresponding depth in a nested list.

    Args:
        data (list): The nested list to analyze.
        depth (int): The current depth in the recursion (default is 0).
        level_counts (dict): A dictionary to track the number of elements at each depth.

    Returns:
        tuple: (max_count, max_depth) where:
               - max_count is the maximum number of elements.
               - max_depth is the depth at which max_count was found.
    """
    if level_counts is None:
        level_counts = {}

    if isinstance(data, (list,tuple,np.ndarray)):
        # Count elements at the current depth
        level_counts[depth] = level_counts.get(depth, 0) + len(data)

        # Recursively check sublists
        for item in data:
            find_max_elements_and_level(item, depth + 1, level_counts)

    # Find the depth with the maximum count
    max_depth = max(level_counts, key=level_counts.get)
    max_count = level_counts[max_depth]

    return max_count, max_depth

# 配列の値にインデックスを格納したリスト配列を使ってアクセスする
def access_nested_collection(nested_list,indices):
    
    for i,index in enumerate(indices):

        if type(nested_list) == dict:
            if not(index in nested_list):
                return None
            
        else:
            if not(0 <= index < len(nested_list)):     
                return None # インデックスが範囲外の場合はNoneを返す
            
        # int または str の場合、最後のインデックスでない場合はNoneを返す
        if not isinstance(nested_list[index], (list, tuple, np.ndarray, dict)):
            if i == len(indices) - 1:
                value = nested_list[index]
                return value
        
            else:
                return None # インデックスが範囲外の場合はNoneを返す
            
        nested_list = nested_list[index]
        
    # 最終的な要素がリストまたは配列の場合
    else:
        value = nested_list
        return value

def access_nested_keep_index(nested_list,indices):

    for index in indices:
        nested_list = nested_list[index][1]
        
    else:
        value = nested_list
        return value

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# 配列の型変換を行う関数
# tuple,dict > list, dict
def convert_tuple_to_list(data):
    """
    ネストされたデータ構造内のタプルをリストに変換し、
    辞書型はそのまま保持します。

    Parameters:
        data: 入力データ（リスト、タプル、辞書など）

    Returns:
        タプルをリストに変換したデータ構造
    """
    if isinstance(data, tuple):
        # タプルをリストに変換し、再帰的に要素を処理
        return [convert_tuple_to_list(item) for item in data]
    elif isinstance(data, list):
        # リスト内の要素を再帰的に処理
        return [convert_tuple_to_list(item) for item in data]
    elif isinstance(data, dict):
        # 辞書はそのまま保持し、値を再帰的に処理
        return {key: convert_tuple_to_list(value) for key, value in data.items()}
    else:
        # 基本データ型はそのまま返す
        return data
    
# list, dict ▷ tuple,dict
def convert_list_to_tuple(data):
    """
    ネストされたデータ構造内のリストをタプルに変換し、
    辞書型はそのまま保持します。

    Parameters:
        data: 入力データ（リスト、タプル、辞書など）

    Returns:
        リストをタプルに変換したデータ構造
    """
    if isinstance(data, list):
        # リストをタプルに変換し、再帰的に要素を処理
        return tuple(convert_list_to_tuple(item) for item in data)
    elif isinstance(data, dict):
        # 辞書はそのまま保持し、値を再帰的に処理
        return {key: convert_list_to_tuple(value) for key, value in data.items()}
    elif isinstance(data, tuple):
        # タプル内の要素を再帰的に処理
        return tuple(convert_list_to_tuple(item) for item in data)
    else:
        # 基本データ型はそのまま返す
        return data

'''
=============================================================================================================================================================
配列をフラット化・整形するクラス
'''

class SetPrint:

    # 初期化
    def __init__(self, input_list):

        self.input_list = input_list

        self.int_type = (int)
        self.str_type = (str)
        self.sequence_type = (list,tuple,np.ndarray)
        self.mapping_type = (dict)
        #self.collection_type = self.sequence_type+self.mapping_type

        # 入力データ('#'は引数の受け取り箇所)
        self.style_settings = (

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

           ("padding"    ,  {  'key'   : (' ', ':') , 'value'  : ' ' }),
           ("empty"      ,  {  'key'   : ('*', ' ') , 'value'  : '-' }),


           ("settings"   ,  { 'print'  : True }),
           ("progress"   ,  { 'print'  : False  ,
                              'len'    : 20  }))
        )
        
        # 制限('#'の箇所をまとめて管理)
        self.constraints = {
            ( 0, 1,     'image',    'list'    ) : {'type': str},
            ( 0, 1,     'image',   'tuple'    ) : {'type': str},
            ( 0, 1,     'image', 'ndarray'    ) : {'type': str},
            ( 0, 1,     'image',    'dict'    ) : {'type': str},
            ( 1, 1, 'partially',    'list', 0 ) : {'type': str, 'min_length':1, 'max_length':1},
            ( 1, 1, 'partially',    'list', 1 ) : {'type': str, 'min_length':1, 'max_length':1},
            ( 1, 1, 'partially',   'tuple', 0 ) : {'type': str, 'min_length':1, 'max_length':1},
            ( 1, 1, 'partially',   'tuple', 1 ) : {'type': str, 'min_length':1, 'max_length':1},
            ( 1, 1, 'partially', 'ndarray', 0 ) : {'type': str, 'min_length':1, 'max_length':1},
            ( 1, 1, 'partially', 'ndarray', 1 ) : {'type': str, 'min_length':1, 'max_length':1},
            ( 1, 1, 'partially',    'dict', 0 ) : {'type': str, 'min_length':1, 'max_length':1},
            ( 1, 1, 'partially',    'dict', 1 ) : {'type': str, 'min_length':1, 'max_length':1},
            ( 1, 1, 'partially',    'None', 0 ) : {'type': str, 'min_length':1, 'max_length':1},
            ( 1, 1, 'partially',    'None', 1 ) : {'type': str, 'min_length':1, 'max_length':1},
            ( 2, 1,       'key',        0     ) : {'type': str, 'min_length':1, 'max_length':1},
            ( 2, 1,       'key',        1     ) : {'type': str, 'min_length':1, 'max_length':1},
            ( 2, 1,     'value'               ) : {'type': str, 'min_length':1, 'max_length':1},
            ( 3, 1,       'key',        0     ) : {'type': str, 'min_length':1, 'max_length':1},
            ( 3, 1,       'key',        1     ) : {'type': str, 'min_length':1, 'max_length':1},
            ( 3, 1,     'value'               ) : {'type': str, 'min_length':1, 'max_length':1},
            ( 4, 1,     'print'               ) : {'type': bool,},
            ( 5, 1,     'print'               ) : {'type': bool,},
            ( 5, 1,       'len'               ) : {'type': int, 'min':0}
        
        }
   
    # 表示スタイルの状態を視覚化する関数 
    def set_text_style(self,arguments):
        self.style_settings = convert_tuple_to_list(self.style_settings)
        self.update_data_with_arguments(arguments, current_index=())
        self.style_settings = convert_list_to_tuple(self.style_settings)

        if self.style_settings[4][1]['print']:
            # ANSIエスケープコードを色ごとに変数で定義
            g = "\033[38;5;46m"   # 緑 (Green)
            g2 = '\033[38;5;43m'
            b = "\033[38;5;27m"   # 青 (Blue)
            y = "\033[38;5;226m"  # 黄色 (Yellow)
            c = "\033[38;5;51m"   # シアン (Cyan)
            w = "\033[38;5;15m"   # 白 (White)
            l = "\033[38;5;45m"
            R = "\033[0m"         # 色のリセット
            quote = w+"'"+R

            list_settings = [
                'style_settings = (',
                '',
                f'   (({g}"Collections"{R} ,',
                "     {  'image'   : { "+f"'list'    {g}:{R} {quote}{c}{self.style_settings[0][1]['image']['list']}{quote} ,",
                f"                      'tuple'   {g}:{R} {quote}{c}{self.style_settings[0][1]['image']['tuple']}{quote} ,",
                f"                      'ndarray' {g}:{R} {quote}{c}{self.style_settings[0][1]['image']['ndarray']}{quote} ,",
                f"                      'dict'    {g}:{R} {quote}{c}{self.style_settings[0][1]['image']['dict']}{quote} }}}}),",
                '',
                f'    ({g}"bracket"{R}     ,',
                "     { 'partially': { "+f"'list'    {g}:{R} ( {quote}{y}{self.style_settings[1][1]['partially']['list'][0]}{quote}{b} , {R}{quote}{y}{self.style_settings[1][1]['partially']['list'][1]}{quote} ),",
                f"                      'tuple'   {g}:{R} ( {quote}{y}{self.style_settings[1][1]['partially']['tuple'][0]}{quote}{b} , {R}{quote}{y}{self.style_settings[1][1]['partially']['tuple'][1]}{quote} ),",
                f"                      'ndarray' {g}:{R} ( {quote}{y}{self.style_settings[1][1]['partially']['ndarray'][0]}{quote}{b} , {R}{quote}{y}{self.style_settings[1][1]['partially']['ndarray'][1]}{quote} ),",
                f"                      'dict'    {g}:{R} ( {quote}{y}{self.style_settings[1][1]['partially']['dict'][0]}{quote}{b} , {R}{quote}{y}{self.style_settings[1][1]['partially']['dict'][1]}{quote} ),",
                f"                      'None'    {g}:{R} ( {quote}{y}{self.style_settings[1][1]['partially']['None'][0]}{quote}{b} , {R}{quote}{y}{self.style_settings[1][1]['partially']['None'][1]}{quote} )}}}}),",
                '',                                       
                f'    ({g}"padding"{R}     ,'+" {  'key'  "+f" {g}:{R} {l}{self.style_settings[2][1]['key']}{R} ,  'value' "+f"{g}:{R} {quote}{l}{self.style_settings[2][1]['value']}{quote} }}),",
                f'    ({g}"empty"{R}       ,'+" {  'key'  "+f" {g}:{R} {l}{self.style_settings[3][1]['key']}{R} ,  'value' "+f"{g}:{R} {quote}{l}{self.style_settings[3][1]['value']}{quote} }}),",  
                '',
                '',
                f'    ({g2}"settings"{R}    ,'+" { 'print'  "+g2+":"+R+" \033[34m" + str(self.style_settings[4][1]['print']) + "\033[0m }),",
                f'    ({g2}"progress"{R}    ,'+" { 'print'  "+g2+":"+R+" \033[34m" + str(self.style_settings[5][1]['print']) + "\033[0m  ,",
                       '                    '+"   'len'    "+g2+":"+R+" \033[34m" + str(self.style_settings[5][1]['len'])   + "\033[0m  }))",
                ')',
            ]
            for line in list_settings:
                print(line)
    
    # 表示スタイルの変更を行う関数
    def update_data_with_arguments(self, arguments, current_index=()):

        if isinstance(arguments, self.mapping_type):
            # 辞書を探索
            for key, value in arguments.items():
                new_index = current_index + (key,)
                self.update_data_with_arguments(value, new_index)
        elif isinstance(arguments, self.sequence_type):
            # リストやタプルを探索
            for i, value in enumerate(arguments):
                new_index = current_index + (i,)
                self.update_data_with_arguments(value, new_index)
        else:
            # 値がplaceholderと一致する場合
            if current_index in self.constraints:
                
                new_value = arguments
                constraint = self.constraints[current_index]

                update_True = True

                # データ型のチェック
                if 'type' in constraint and not isinstance(new_value, constraint['type']):
                    print(f"Value '{new_value}' at index {current_index} must be of type {constraint['type'].__name__}.")
                    update_True = False

                # 許可された値のチェック
                if 'allowed_values' in constraint and new_value not in constraint['allowed_values']:
                    print(f"Value '{new_value}' at index {current_index} is not in allowed values {constraint['allowed_values']}.")
                    update_True = False

                # 範囲チェック
                if isinstance(new_value, self.int_type):  # 数列型の場合のみ適用
                    if 'min' in constraint and new_value < constraint['min']:
                        print(f"Value '{new_value}' at index {current_index} is less than the minimum value {constraint['min']}.")
                        update_True = False
                    if 'max' in constraint and new_value > constraint['max']:
                        print(f"Value '{new_value}' at index {current_index} is greater than the maximum value {constraint['max']}.")
                        update_True = False

                # 文字列の長さチェック
                if isinstance(new_value, self.str_type):  # 文字列型の場合のみ適用
                    if 'max_length' in constraint and len(new_value) > constraint['max_length']:
                        print(f"Value '{new_value}' at index {current_index} exceeds maximum length of {constraint['max_length']}.")
                        update_True = False
                    if 'min_length' in constraint and len(new_value) < constraint['min_length']:
                        print(f"Value '{new_value}' at index {current_index} is shorter than minimum length of {constraint['min_length']}.")
                        update_True = False

                if update_True:
                    target = self.style_settings
                    # 最後のキー以外でデータ構造を掘り下げる
                    for key in current_index[:-1]:
                        target = target[key]
                    
                    # 最後のキーで値を更新
                    target[current_index[-1]] = new_value

    '''
    =============================================================================================================================================================
    ・リストの中身やインデックスを調査し、整列させる関数。
    [→]...通常の関数
    [↺]...再帰関数
    [_:n]...関数の番号

    (P:n)...search_  処理の重要箇所
     - (P:0); キープ無しでブロック化
        # キープ範囲外の単独でのブロック化 ( ***** {キープ範囲} ##### )
        # ^^^ の処理                  [ ^^^^^            ^^^^^ ]

     - (P:1); キープブロック化 (キープデータの初期化)
     - (P:2); キープブロック化 (キープデータへ格納情報を格納)
    '''

    # <t:maintenance_run>
    
    def transform_keep_index(self,index):

        x_keep_index = index[:]
        y_keep_index = index[:]
        
        for deepnum in range(len(index)):
            set_type = self.keep_settings[deepnum]
            if set_type in ('y','yf'):
                x_keep_index[deepnum] = set_type
            else:
                y_keep_index[deepnum] = 0
           
        return tuple(x_keep_index),tuple(y_keep_index)
    
    # リストを整型する際の条件を整理 / １次元目の格納情報を整形 [→:#0]
    # [→:0] 中身は search_mapping / search_sequence とほぼ同じ
    def set_list(self, guide,keep_start):

        datas = self.input_list
        

        # if keep_start == False:
        #     self.keep_start = 0
        #     self.keep_finish = 0
        #     self.show_all = False
        
        # else:
        #     if type(keep_start) != int:
        #         if keep_start == 'auto':
        #             max_count, max_depth = find_max_elements_and_level(datas)  # 次元数を取得
        #             self.keep_start = max_depth
        #             self.show_all = True

        #         else:
        #             return
        #     else:
        #         self.keep_start = keep_start
        #     # if type(keep_range) != int:
        #     #     if keep_range == 'all':
        #     #         self.show_all = True
        #     #     else:
        #     #         return
        #     # else:
        #     #     self.show_all = False
        #     #     self.keep_finish = self.keep_start + keep_range
            
        self.keep_start = keep_start

        #初期化
        self.now_deep = 0 #now_deepはインデックスの次元測定
        self.now_index = [] # 調べている場所のインデックスを格納する。
        # self.now_key = [] # now_indexに辞書型のキーが必要な箇所とキーを格納
        # self.Xline_blocks = []
        # self.keep_txts_data = []
        self.keep_index = []

        # keep_liens_data = ['{n}']
        # All_blocks = []
        # keep_Ylines_data = []

        self.MAX_index = {} # X_keep_index(変更予定の変数名)
        self.Y_keep_index = {}
        self.keep_index = []
        self.range_idx = []
        self.y_flat_index = []
        self.X_keep_index = []

        now_keep_index = []

        # <t:初期化>

        #表示スタイルの更新
        self.collections = self.style_settings[0][1]['image']
        
        # 値を (値, 値の文字数) に変更
        self.collections = {key: (value, len(value)) for key, value in self.collections.items()}
        
        self.bracket = self.style_settings[1][1]['partially']

        self.padding_key = self.style_settings[2][1]['key'][0]
        self.padding_colon = ' '+self.style_settings[2][1]['key'][1]+' '
        self.padding_value = self.style_settings[2][1]['value']

        self.empty_key = self.style_settings[3][1]['key'][0]
        self.empty_colon = ' '+self.style_settings[3][1]['key'][1]+' '
        self.empty_value = self.style_settings[3][1]['value']
        
        # self.bracket_e = self.style_settings['bracket']['exists']
        self.ber_print = self.style_settings[5][1]['print']
        # ber_print(1)
        if self.ber_print:
            self.ber_len = self.style_settings[5][1]['len']
            self.line_ber_len = self.ber_len/len(datas)
            print()
            print('seach_collection...')
            print('{ '+' '*self.ber_len+' }')
        

        keep_deeps = list(self.keep_start.keys())
        self.min_keep_deep = min(keep_deeps)
        self.max_keep_deep = max(keep_deeps)

        keep_settings = []

        range_keep_type = None
        for deep in range(self.max_keep_deep):
            deep+=1
            if deep in self.keep_start.keys():
                range_keep_type = self.keep_start[deep]
                if range_keep_type == 'yf':
                    keep_settings.append('yf')
                else:
                    keep_settings.append(range_keep_type)

            else:
                if range_keep_type == 'yf':
                    keep_settings.append('f')
                else:
                    keep_settings.append(range_keep_type)
        
        print()
        print('all_deep_settings\n',keep_settings)

        self.keep_settings = keep_settings
        
        if isinstance(datas, self.mapping_type):
            self.search_mapping(datas)
        else:
            x_keep_index = self.search_sequence(datas,[])

        # ber_print(3)
        if self.ber_print:
            print('\033[F\033[F\033[KThe search_collection process has been successfully completed.\n' + '{ '+'='*self.ber_len+' }')
        
        # <a:keep_index>
        
        # <t:print>

        print()

        self.format_keep_data(x_keep_index,self.Y_keep_index)

        # <t:return>

        # print(self.tracking_data)
        
        # set_border_list = self.blocks_border_print(All_blocks = All_blocks, line_title = line_title, guide = guide)

        # set_data_dict = {

        # "input_list" : datas,
        # "grid_slice" : set_border_list,
        # 'grid_block' : All_blocks,

        # 'block_keep_data' : keep_Ylines_data

        # }

        # self.set_data_dict = set_data_dict
        
        # return set_data_dict,self.tracking_data

 
    # [↺:1] マッピング型を調べる
    def search_mapping(self, datas):
        
        self.now_deep += 1 #deepはインデックスの次元測定

        # if self.now_deep == self.min_keep_deep:
        #     self.MAX_index = {} # X_keep_index(変更予定の変数名)
        #     self.Y_keep_index = {}
        #     self.keep_index = []
        #     self.range_idx = []

        # (P:2)
        # キープ範囲内にある次元の配列から情報を取得する。
        if self.now_deep in self.keep_range:
            
            self.keep_index.append(-1)
            self.now_index.append('')
            # self.now_key.append('')
                
            insert_index = self.keep_index.copy()

            # self.keep_1line_data.append([insert_index,'{'])
            
            if (insert_index in self.range_idx) == False:
                self.range_idx.append(insert_index)
            #     self.MAX_indexlen.append([0,1])
            # else:
            #     if self.MAX_indexlen[self.MAX_index.index(insert_index)][1] < 1:
            #         self.MAX_indexlen[self.MAX_index.index(insert_index)][1] = 1

            # <p:範囲内>
            self.maintenance_run('start','In_range')

            for linenum, (key, line) in enumerate(datas.items()):

                self.keep_index[-1] = linenum
                self.now_index[-1] = linenum
                # self.now_key[-1] = [self.now_deep-1,key]
                
                # self.mapping_point.append(self.keep_line + self.keep_index)
                # self.mapping_key.append(self.now_key[self.pivot_value:])

                insert_index = self.keep_index.copy()
                
                if isinstance(line, self.sequence_type):

                    # <p:配列型>
                    self.maintenance_run('collection_type','In_range')
                    
                    value = self.collections[str(type(line).__name__)][0]
                    # self.keep_1line_data.append([insert_index,value,key])
                    
                    self.search_sequence(line)

                    self.maintenance_run('配列の調査結果の受け取り','In_range',)

                elif isinstance(line, self.mapping_type):

                    # <p:範囲内 int/str型>
                    self.maintenance_run('int/str_type','In_range')
                    
                    value = self.collections[str(type(line).__name__)][0]
                    # self.keep_1line_data.append([insert_index,value,key])
                    
                    self.search_mapping(line)

                    self.maintenance_run('配列の調査結果の受け取り','In_range')

                else:
                    value = str(line)
                    # self.keep_1line_data.append([insert_index,value,key])

                #存在するインデックスの情報の新規作成/更新
                if (insert_index in self.range_idx) == False:
                    self.range_idx.append(insert_index)

                    # self.MAX_indexlen.append([len(str(key)),len(value)])

                    # if isinstance(value,self.int_type):
                    #     int_len = len(str(int(value)))
                    #     float_len = (str(value))-int_len # 小数点を含める
                    #     self.MAX_indexlen.append([len(str(key)),len(value),int_len,float_len])
                    # else:
                    #     self.MAX_indexlen.append([len(str(key)),len(value),0,0])
                    
                #else:
                    #insert_index = self.range_idx.index(insert_index)
                    # if self.MAX_indexlen[insert_index][0] < len(str(key)):
                    #     self.MAX_indexlen[insert_index][0] = len(str(key))

                    # if self.MAX_indexlen[insert_index][1] < len(value):
                    #     self.MAX_indexlen[insert_index][1] = len(value)

            
            insert_index = self.keep_index.copy()
            insert_index[-1] += 1


            # self.keep_1line_data.append(['finish',insert_index,'}'])

            if (insert_index in self.range_idx) == False:
                self.range_idx.append(insert_index)
            #     self.MAX_indexlen.append([0,1])
            # else:
            #     if self.MAX_indexlen[self.MAX_index.index(insert_index)][1] < 1:
            #         self.MAX_indexlen[self.MAX_index.index(insert_index)][1] = 1

            # key = str(insert_index[:-1])
            # if (key in self.finish_index) == False:
            #     self.finish_index[key] = insert_index[-1]
            # else:
            #     if self.finish_index[key] < insert_index[-1]:
            #         self.finish_index[key] = insert_index[-1]

            del self.keep_index[-1]
        
            # <t:範囲内 配列の調査完了>
            self.maintenance_run('配列の調査完了','In_range')
        
        # (P:1)
        # キープする次元と現在の次元が同じなら、キープ用の処理に移る。
        elif self.now_deep in self.yf_point:

            # txt_index = ''
            # for i in self.now_index:
            #     txt_index += '['+str(i)+']'
            # txt_index += '{n}' 
            
            # self.yf_setup(datas,txt_index)

            
            parent_index = self.now_index.copy() + [0]
            #print(parent_index[3])
            print('p_range',len(parent_index)-1,self.now_deep)
            
            # インデックスのキープ化
            x_keep_index,y_keep_index = self.transform_keep_index(parent_index)

            if x_keep_index not in self.MAX_index:
                self.MAX_index[x_keep_index] = []
            
            if y_keep_index not in self.Y_keep_index:
                self.Y_keep_index[y_keep_index] = []

            self.yf_setup(datas,x_keep_index)
            

        # (P:0)
        else:

            # <t:範囲外>
            parent__keep_tracking = self.maintenance_run('start','Out_of_range')

            txt_index = ''
            for i in self.now_index:
                txt_index += '['+str(i)+']'
            txt_index += '{n}' 
        
            # keep_liens_data = [txt_index]
        
            # self.Xline_blocks.append('')
            # insert_index = len(self.Xline_blocks)-1

            # parent_key = self.now_key[:]
            parent_index = self.now_index.copy()
            parent_index[-1] = 'n'
            # for line in parent_key:
            #     parent_index[line[0]] = line[1]

            self.now_index.append('')
            # self.now_key.append('')

            max_keylen = 0
            max_txtlen = 0
            value_datas = []

            # mapping_point = []
            # mapping_key = []
            # # self.keep_txts_data.append('')

            for linenum, (key, line) in enumerate(datas.items()):

                self.now_index[-1] = linenum
                # self.now_key[-1] = [self.now_deep-1,key]

                # mapping_point.append([linenum])
                # mapping_key.append(self.now_key[:])
                
                if isinstance(line, (list, tuple, np.ndarray, dict)):

                    # <p:配列型>
                    self.maintenance_run('collection_type','Out_of_range')

                    if type(line) == dict:
                        self.search_mapping(line)
                    else:
                        self.search_sequence(line)

                    line = f'data_type: {type(line)}'

                    # <p:配列型>
                    self.maintenance_run('配列の調査結果の受け取り','Out_of_range')

                else:
                    # <p:配列型>
                    self.maintenance_run('int/str_type','Out_of_range')

                if self.min_keep_deep <= self.now_deep <= self.max_keep_deep:

                    parent_index = self.now_index.copy()
                    
                    # インデックスのキープ化
                    x_keep_index,y_keep_index = self.transform_keep_index(parent_index)

                    if x_keep_index not in self.MAX_index:
                        self.MAX_index[x_keep_index] = []
                    
                    if y_keep_index not in self.Y_keep_index:
                        self.Y_keep_index[y_keep_index] = []

                        
                value_datas.append([key,line])
                
                if max_keylen < len(str(key)):
                    max_keylen = len(str(key))
                if max_txtlen < len(str(line)):
                    max_txtlen = len(str(line))
                
            # for line in value_datas:
            #     key_air = (max_keylen - len(str(line[0]))) * ' '
            #     txt_air = (max_txtlen - len(str(line[1]))) * ' '
            #     keep_liens_data.append(key_air+str(line[0])+' : '+txt_air+str(line[1]))
            
            #中身のリスト作成
            # self.Xline_blocks[insert_index] = keep_liens_data
            
            # self.keep_txts_data[insert_index] = [parent_index,max_keylen+max_txtlen+3,mapping_point,mapping_key]

            # <t:配列の調査完了>
            self.maintenance_run('配列の調査完了','Out_of_range',parent__keep_tracking)

        del self.now_index[-1] #インデックスの調査が終わったら戻す
        # del self.now_key[-1]

        self.now_deep -= 1

    # [↺:2] シーケンス型を調べる
    def search_sequence(self, datas, Kdeep_index):

        self.now_deep += 1 #deepはインデックスの次元測定
        
        # if self.now_deep == self.min_keep_deep:
        #     self.MAX_index = {} # X_keep_index(変更予定の変数名)
        #     self.Y_keep_index = {}
        #     self.keep_index = []
        #     self.range_idx = []
    
        # (P:2)
        # キープ範囲内にある次元の配列から情報を取得する。
        
        set_keep_type = self.keep_settings[self.now_deep-1]
        if set_keep_type == 'f':
            
            self.keep_index.append(-1)
            self.now_index.append('')
       
            insert_index = self.keep_index[:]
           
            if (insert_index in self.range_idx) == False:
                self.range_idx.append(insert_index)
            
            len_Kdeep_index = len(Kdeep_index)-1

            # <t:start,In_range>

            for linenum in range(len(datas)):

                line = datas[linenum]

                self.keep_index[-1] = linenum
                self.now_index[-1] = linenum

                insert_index = self.keep_index[:]

                self.y_flat_index.append(self.keep_index[:])

                if len_Kdeep_index < linenum:
                    Kdeep_index.append(0)
               
                if isinstance(line, (list, tuple, np.ndarray, dict)):

                    if type(Kdeep_index[linenum]) != list:
                        
                        if Kdeep_index[linenum] < self.collections[type(line).__name__][1]:
                            Kdeep_index[linenum] = [self.collections[type(line).__name__][1],[]]
                        else:
                            Kdeep_index[linenum] = [Kdeep_index[linenum],[]]
                    
                    else:
                        
                        if Kdeep_index[linenum][0] < self.collections[type(line).__name__][1]:
                            Kdeep_index[linenum][0] = [self.collections[type(line).__name__][1],[]]

                    # <t:collection_type,In_range>
                                 
                    if type(line) == dict:
                        self.search_mapping(line)
                    else:
                        Kdeep_index[linenum][1] = self.search_sequence(line,Kdeep_index[linenum][1])

                    # <t:配列の調査結果の受け取り,In_range>
        
                else:
                    
                    if type(Kdeep_index[linenum]) != list:
                        if Kdeep_index[linenum] < len(str(line)):
                            Kdeep_index[linenum] = len(str(line))
                    else:
                        if Kdeep_index[linenum][0] < len(str(line)):
                            Kdeep_index[linenum][0] =  len(str(line))
                    
                    # <t:int/str_type,In_range>

                #存在するインデックスの情報の新規作成/更新
                if (insert_index in self.range_idx) == False:
                    self.range_idx.append(insert_index)
                
            insert_index = self.keep_index.copy()
            insert_index[-1] += 1

            if (insert_index in self.range_idx) == False:
                self.range_idx.append(insert_index)
            
            del self.keep_index[-1]

            # <t:配列の調査完了,In_range>

        
        # (P:1)
        # キープする次元と現在の次元が同じなら、キープ用の処理に移る。
            
        elif set_keep_type == 'yf':
            
            parent_index = self.now_index.copy() + [0]
            Kdeep_index = self.yf_setup(datas,parent_index,Kdeep_index)


        # (P:0)
        else:

            # <t:start,Out_of_range>

            txt_index = ''
            for i in self.now_index:
                txt_index += '['+str(i)+']'
            txt_index += '{n}' 
        
            keep_liens_data = [txt_index]

            self.now_index.append('')

            parent_index = self.now_index.copy()
            parent_index[-1] = 'n'

            keep_x = self.keep_settings[self.now_deep-1] in ('x','f')
            direction_index = 0
            
            if not keep_x:
                if len(Kdeep_index) == 0:
                    Kdeep_index = [0]
                    #Kdeep_index = ['y']
                    y_Kdeep_index = []

            len_Kdeep_index = len(Kdeep_index)-1

            for linenum in range(len(datas)):
                line = datas[linenum]

                self.now_index[-1] = linenum
                
                if keep_x:    
                    if len_Kdeep_index < linenum:
                        Kdeep_index.append(0)
                    direction_index = linenum
                
                if self.min_keep_deep <= self.now_deep <= self.max_keep_deep:

                    # インデックスのキープ化
                    x_keep_index,y_keep_index = self.transform_keep_index(self.now_index.copy())

                    if x_keep_index not in self.MAX_index:
                        self.MAX_index[x_keep_index] = []
                    
                    if y_keep_index not in self.Y_keep_index:
                        self.Y_keep_index[y_keep_index] = []

                    self.Y_keep_index[y_keep_index].append([self.now_index[:-1],[[linenum]]])

                
                if isinstance(line, (list, tuple, np.ndarray, dict)):

                    if type(Kdeep_index[direction_index]) != list:
                        if Kdeep_index[direction_index] < self.collections[type(line).__name__][1]:
                            Kdeep_index[direction_index] = [self.collections[type(line).__name__][1],[]]
                        else:
                            Kdeep_index[direction_index] = [Kdeep_index[direction_index],[]]
                    
                    else:
                        if Kdeep_index[direction_index][0] < self.collections[type(line).__name__][1]:
                            Kdeep_index[direction_index][0] = self.collections[type(line).__name__][1]

        
                    # <t:collection_type,Out_of_range>

                    if type(line) == dict:
                        self.search_mapping(line)
                    else:
                        Kdeep_index[direction_index][1] = self.search_sequence(line,Kdeep_index[direction_index][1])

                    # <t:配列の調査結果の受け取り,Out_of_range>
                    
                    keep_liens_data.append(f'data_type: {type(line)}')
                else:
                    if type(Kdeep_index[direction_index]) != list:
                        if Kdeep_index[direction_index] < len(str(line)):
                            Kdeep_index[direction_index] = len(str(line))
                    else:
                        if Kdeep_index[direction_index][0] < len(str(line)):
                            Kdeep_index[direction_index][0] = len(str(line))
                    
                    # <t:int/str_type,Out_of_range>

                    keep_liens_data.append(str(line))
            
            # <t:配列の調査完了,Out_of_range>


        del self.now_index[-1] #インデックスの調査が終わったら戻す
        self.now_deep -= 1

        return Kdeep_index


    # [→:3] キープデータの初期化/作成後の後処理
    def yf_setup(self,datas,parent_index,Kdeep_index):
        
        # 格納情報、次元情報、文字数を取得する為の処理

        # 格納情報の保存
        parent__keep_index = self.keep_index
        parent__range_idx = self.range_idx
        parent__y_flat_index = self.y_flat_index
        parent__X_keep_index = self.X_keep_index

        # 親キープインデックス
        parent_x_keep_index,parent_y_keep_index = self.transform_keep_index(parent_index)

        # インデックスのキープ化        
        if parent_x_keep_index not in self.MAX_index:
            self.MAX_index[parent_x_keep_index] = []
        
        if parent_y_keep_index not in self.Y_keep_index:
            self.Y_keep_index[parent_y_keep_index] = []

        # <t:キープ初期化>

        self.keep_index = []
        self.range_idx = self.MAX_index[parent_x_keep_index]
        
        # in_range_indices
        # self.MAX_indexlen  = [] # インデックスに格納されている配列の文字数を格納する。

        # parent_key         = self.now_key[:] # 親インデックスのキー
        # self.pivot_value   = len(parent_key) # 親インデックスのキー以降をmapping_keyに格納するための基準値設定。

        # self.mapping_point = [] # 辞書型が存在している場所を格納する。
        # self.mapping_key   = [] # keep_keyに対応するマッピング型のキー

        # keep_liens_data    = [] # 1列毎の配列情報を格納するリスト

        # self.finish_index = {} #リスト配列の最後尾のインデックスを格納

        """
        self.MAX_index
        拡張なし

        self.MAX_indexlen
        格納する値を [ key_len,   txt_len,   int_len, flot_len, ] に拡張する。
                     ~~~~~~~    ~~~~~~~    ~~~~~~~--~~~~~~~~
                   辞書型対応[0] 文字列用[1]    数列整形用[2,3]  

        keep_lies_data
        格納する値を [ self.keep_index,  collections_txt,  key ]
                                                         ~~~
                                                     辞書型対応[2]
        """
        
        self.now_index.append('')

        # <t:start,In_range>

        # print('start')
        # print(' < X.      ',self.range_idx)
        # print(' < Y.      ',self.Y_keep_index[parent_y_keep_index])
        # print(' < tracking',self.keep_tracking)

        if len(Kdeep_index) == 0:
            Kdeep_index = [[0,[]]]

        if type(datas) == dict:
            
            for linenum, (key, line) in enumerate(datas.items()):

                self.now_index[-1] = linenum
                self.keep_line = [linenum]
                self.keep_index = []

                # self.mapping_point.append(self.keep_line + self.keep_index)
                # self.mapping_key.append(self.now_key[self.pivot_value:])

                if isinstance(line, (list, tuple, np.ndarray, dict)):
                    
                    # <t:collection_type,In_range>

                    # 以降の格納要素についてのキープデータ作成は search_ mapping,sequence 関数を使用する。
                    if type(line) == dict:
                        self.search_mapping(line)
                    else:
                        self.search_sequence(line)
                    
                    # <t:配列の調査結果の受け取り,In_range>
                
                
                else:

                    # <t:int/str_type,In_range>

                    value_line = str(line)
                
                #存在するインデックスの情報の新規作成/更新
                if (self.keep_index in self.range_idx) == False:
                    self.range_idx.append(self.keep_index.copy())

                if self.ber_print:
                    if self.keep_start == 1:
                        now_len = int(self.line_ber_len*(linenum+1))
                        print('\033[F\033[K{ '+'-'*now_len+' '*(self.ber_len-now_len)+' }')
        
        else:
            for linenum in range(len(datas)):
                self.keep_line = [linenum]
                self.keep_index = []
                line = datas[linenum]
                
                self.now_index[-1] = linenum

                # インデックスのキープ化
                x_keep_index,y_keep_index = self.transform_keep_index(self.now_index)
                
                if y_keep_index not in self.Y_keep_index:
                    self.Y_keep_index[y_keep_index] = []
                
                self.y_flat_index = [[]]
                
                if isinstance(line, (list, tuple, np.ndarray, dict)):

                    if type(Kdeep_index[0]) != list:
                        if Kdeep_index[0] < self.collections[type(line).__name__][1]:
                            Kdeep_index[0] = self.collections[type(line).__name__][1]
                    else:
                        if Kdeep_index[0][0] < self.collections[type(line).__name__][1]:
                            Kdeep_index[0][0] = self.collections[type(line).__name__][1]
                
                    # <t:collection_type,In_range>


                    value_txt = self.collections[str(type(line).__name__)][0]
                    # 以降の格納要素についてのキープデータ作成は search_ mapping,sequence 関数を使用する。

                    if type(line) == dict:
                        self.search_mapping(line)
                    else:
                        Kdeep_index[0][1] = self.search_sequence(line,Kdeep_index[0][1])

                    # <t:配列の調査結果の受け取り,In_range>

                else:
                    
                    if type(Kdeep_index[0]) != list:
                        if Kdeep_index[0] < len(str(line)):
                            Kdeep_index[0] = len(str(line))
                    else:
                        if Kdeep_index[0][0] < len(str(line)):
                            Kdeep_index[0][0] = len(str(line))
                    
                    # <t:int/str_type,In_range>
                
                ''' 親インデックスの方に格納する
                #存在するインデックスの情報の新規作成/更新
                print(self.keep_index)
                if (self.keep_index in self.range_idx) == False:
                    self.range_idx.append(self.keep_index.copy())
                #     self.MAX_indexlen.append([0,len(value_txt)])
                # else:
                #     if self.MAX_indexlen[self.MAX_index.index(self.keep_index)][1] < len(value_txt):
                #         self.MAX_indexlen[self.MAX_index.index(self.keep_index)][1] = len(value_txt)
                '''

                self.Y_keep_index[y_keep_index].append([self.now_index[:],self.y_flat_index[:]])

                # ber_print(2)
                if self.ber_print:
                    if self.keep_start == 1:
                        now_len = int(self.line_ber_len*(linenum+1))
                        print('\033[F\033[K{ '+'-'*now_len+' '*(self.ber_len-now_len)+' }')

        # print('return')
        # print(' > X.      ',self.range_idx)
        # print(' > Y.      ',self.Y_keep_index[parent_y_keep_index])
        # print(' > tracking',self.keep_tracking)
        # print()

        # <t:キープ範囲調査完了>

        # ber_print(2)
        if self.ber_print:
            if self.keep_start == 1:
                print('\033[F\033[F\033[Kformat_keep_data...\n' + '{ '+'-'*self.ber_len+' }')

        # 取得し終えた、配列情報を、場所や長さで整える処理
        # format_txtdata = []
        # if len(datas) >= 1:
        #     format_txtdata,mismatch_indices = self.format_keep_data(keep_liens_data)


        # pick_guideprintで引き継ぐ 配列情報データから リストの '[', "]" 部分の情報を削除する
        # x_lens = [0]
        # total = 0
        # max_indexlen = []
        # for index_len in self.MAX_indexlen:

        #     if index_len[0] == 0:
        #         total += index_len[1] + 1
        #         max_indexlen.append(index_len[1])
        #     else:
        #         total += index_len[0] + index_len[1] +4
        #         max_indexlen.append(index_len[0] + index_len[1] +3)

        #     x_lens.append(total)
        
        # del x_lens[-1]

        # for line in parent_key:
        #     parent_index[line[0]] = line[1]

        # del_MAXindex = self.MAX_index.copy()
        # self.MAX_indexlen = max_indexlen
        
        # diff = len(parent_index[:-1])

        # for linenum in range(len(self.MAX_index)-1):
        #     line = self.MAX_index[linenum+1]
        #     if line[-1] == -1:
                
        #         if tuple(line[:-1]) in mismatch_indices:
                    
        #             mismatch_point = line[:-1]
               
        #             # 格納状況が異なる箇所の [] を　{) に変更しわかりやすくする。
        #             for txt_linenum in range(len(format_txtdata)):

        #                 search_index = [txt_linenum] + mismatch_point
                    
        #                 matching_index = check_matching_elements(self.mapping_point, search_index)
        #                 if matching_index != -1:
                            
        #                     key_data = self.mapping_key[matching_index]
                            
        #                     for key_line in key_data:
        #                         search_index[key_line[0]-diff] = key_line[1]
                        
        #                 search_index = parent_index[:-1] + search_index
                      
        #                 value = access_nested_collection(self.input_list,search_index)

        #                 if not isinstance(value, (list, tuple, np.ndarray, dict)):
        #                     bracket_image = self.bracket['None']
        #                 else:
        #                     bracket_image = self.bracket[str(type(value).__name__)]
                            

        #                 txt_line = format_txtdata[txt_linenum]

        #                 S_index = x_lens[del_MAXindex.index(line)]
        #                 txt_line = txt_line[:S_index] + bracket_image[0] + txt_line[S_index+1:]

        #                 search_line = line[:-1]
        #                 search_line.append(self.finish_index[str(search_line)])
        #                 F_index = x_lens[del_MAXindex.index(search_line)]
        #                 format_txtdata[txt_linenum] = txt_line[:F_index] + bracket_image[1] + txt_line[F_index+1:]
                        

        #         del_index = del_MAXindex.index(line)
        #         del del_MAXindex[del_index]
        #         del self.MAX_indexlen[del_index]
        #         del x_lens[del_index]

        #         search_line = line[:-1]
        #         search_line.append(self.finish_index[str(search_line)])
        #         del_index = del_MAXindex.index(search_line)
        #         del del_MAXindex[del_index]
        #         del self.MAX_indexlen[del_index]
        #         del x_lens[del_index]
        
        # # 整形したデータを全体のリストに挿入
        # format_txtdata.insert(0,txt_index)
        # self.Xline_blocks[insert_index] = format_txtdata

        # self.keep_txts_data[insert_index] = [parent_index,del_MAXindex,self.MAX_indexlen,x_lens,self.mapping_point,self.mapping_key]       

        # 情報更新
        self.MAX_index[parent_x_keep_index] = self.range_idx # 存在する インデックス now_index[1:] の値を使用し、1列毎での整列を可能にする。
        
        # 情報復元
        self.keep_index = parent__keep_index
        self.range_idx = parent__range_idx
        self.y_flat_index = parent__y_flat_index
        self.X_keep_index = parent__X_keep_index

        return Kdeep_index
        
        #self.MAX_indexlen = parent__MAX_indexlen + self.MAX_indexlen # インデックスに格納されている配列の文字数を格納する。
        # self.pivot_value = parent__pivot_value # 親インデックスのキー以降をmapping_keyに格納するための基準値設定。
        
        # self.mapping_point = parent__mapping_point + self.mapping_point # 辞書型が存在している場所を格納する。
        # self.mapping_key = parent__mapping_key + self.mapping_key# keep_keyに対応するマッピング型のキー
        
        # self.finish_index = parent__finish_index + self.finish_index #リスト配列の最後尾のインデックスを格納


    def flat_x_keep_index(self,x_keep_index,index=[],keep_index=[],keep_len=[]):

        for line,deep_data in enumerate(x_keep_index):
                
            if type(deep_data) == list:
                keep_index.append(index+[line])
                keep_len.append(deep_data[0])
                keep_index,keep_len = self.flat_x_keep_index(deep_data[1],index+[line],keep_index,keep_len)
            else:
                keep_index.append(index+[line])
                keep_len.append(deep_data)
            
        return keep_index,keep_len

    # [→:4] キープデータの整形
    def format_keep_data(self,X_keep_index,Y_keep_index):
        
        x_keep_index,keep_len = self.flat_x_keep_index(X_keep_index)

        print(X_keep_index)
        
        map_width = sum(keep_len) + len(keep_len) -1

        print()
        print('out_put')
        print('-'*map_width)
        print()

        # キーを辞書順（インデックス順）でソート
        Y_keep_index = {k: Y_keep_index[k] for k in sorted(Y_keep_index)}
        format_texts = []

        for y_keep_index,y_line_data in Y_keep_index.items():
            # print(y_keep_index)
            now_line = 0
            line_txt = ''
            for parent,y_x_indexs in y_line_data:

                keep_parent = parent[:]
                now_deep = len(parent)

                for deep in range(now_deep):
                    if self.keep_settings[deep] in ('y','yf'):
                        keep_parent[deep] = 0
               
                # print(keep_parent)
                
                # print(parent,y_x_indexs,now_line)
                
                #print(search_index)
                parent_list = access_nested_collection(self.input_list,parent)

                for y_x_index in y_x_indexs:

                    keep_y_x_index = y_x_index[:]
                    for deep in range(len(y_x_index)):
                        if self.keep_settings[now_deep+deep] in ('y','yf'):
                            keep_y_x_index[deep] = 0
                    
                    # print('search',keep_parent + keep_y_x_index)

                    while x_keep_index[now_line] != keep_parent + keep_y_x_index:
                        # print('False ',x_keep_index[now_line],keep_parent + y_x_index)
                        line_txt += keep_len[now_line]*' ' + ' '
                        now_line += 1

                    # print('True  ',x_keep_index[now_line],keep_parent + keep_y_x_index)
                    # print()
                    
                    value = access_nested_collection(parent_list,y_x_index)
                    if type(value) in (int,str):
                        line_txt += ' ' * (keep_len[now_line] - len(str(value))) + str(value) + ' '
                      
                    else:
                        line_txt += keep_len[now_line]*':' + ' '
                    now_line += 1

            print(line_txt)
            format_texts.append(line_txt)
        
        print()
        print('-'*map_width)
        print()

        print('b',X_keep_index)
        total_x_keep_data = self.total_x_keep_deata(X_keep_index)
        print('n',total_x_keep_data)

        self.format_texts=format_texts
        self.y_keep_line = [list(t) for t in Y_keep_index.keys()]

        # self.format_route(self.input_list, total_x_keep_deata[0])
        
        self.format_route(self.input_list, total_x_keep_data[0])

        print()
        print('out_put / with_route')
        print('-'*map_width)
        print()

        for line in self.format_texts:
            print(line)
         
        print()
        print('-'*map_width)
        print()
               
    #------------------------------------------------------------------------------------------------------------------------------------------------------------

    # def format_keep_data(self,X_keep_index):
    #     if isinstance(self.input_list, self.sequence_type):
    #         self.format_sequence( self.input_list, X_keep_index )

    # def format_sequence(self,datas,range_keep_x,now_deep=0,now_index=[],write_line):

    #     set_keep_type = self.keep_settings[now_deep]
    #     if set_keep_type == 'f':
    #         print('f')
    #     elif set_keep_type == 'yf':
    #         print('yf')

    #         for direction_index,line in enumerate(datas):

    #             if line_len < index:
    #                 format_texts.append('')                
                
    #             if isinstance(line, (list, tuple, np.ndarray, dict)):

    #                 if type(format_texts[direction_index]) != list:
    #                     format_texts[direction_index] = [format_texts[direction_index],['']]
                
    #                 if isinstance(self.input_list, self.sequence_type):
    #                     format_texts[direction_index] = self.format_sequence(datas,now_deep+1,range_keep_x[direction_index][1],now_index+[index],format_texts[direction_index])


    #     else:

    #         keep_y = self.keep_settings[now_deep] in ('y')

    #         direction_index = 0
    #         line_len = len(format_texts)-1

    #         for index,line in enumerate(datas):

    #             if keep_y:
    #                 direction_index = index
                
    #             if line_len < index:
    #                 format_texts.append('')

    #             if isinstance(line, (list, tuple, np.ndarray, dict)):

    #                 if type(format_texts[direction_index]) != list:
    #                     format_texts[direction_index] = [format_texts[direction_index],['']]
                
    #                 if isinstance(self.input_list, self.sequence_type):
    #                     format_texts[direction_index] = self.format_sequence(datas,now_deep+1,range_keep_x[direction_index][1],now_index+[index],format_texts[direction_index])
            
    #         return format_texts

    #------------------------------------------------------------------------------------------------------------------------------------------------------------


    def total_x_keep_deata(self,x_keep_data,total_len=0):

        x_keep_total_len = []
            
        for line,deep_data in enumerate(x_keep_data):

            if type(deep_data) == list:

                p_total_len = total_len
                x_range_total_len,total_len = self.total_x_keep_deata(deep_data[1],total_len + deep_data[0] + 1)
                x_keep_total_len.append([[p_total_len,deep_data[0]],x_range_total_len])
            else:
                x_keep_total_len.append([total_len,deep_data])
                total_len += deep_data +1
                # if total_len == 104:
                #     print('!!!')
        
        return x_keep_total_len,total_len
        

    '''
    total_x_keep_deata = self.total_x_keep_deata(self,x_keep_data)
    '''

    def format_route(self,datas,total_x_keep_data,parent_x=[0,0],now_deep=0,now_y_keep_index=[]):

        set_keep_type = self.keep_settings[now_deep]
        
        if set_keep_type == 'f':
            print('s_f')
            for index,line in enumerate(datas):
                    
                if isinstance(line, (list, tuple, np.ndarray, dict)):

                    if isinstance(line, self.sequence_type):
                        # self.format_texts[y_line] = self.format_route(datas,now_deep+1,now_y_keep_index+[index],total_x_keep_data[index][1])
                        self.format_route(line,total_x_keep_data[index][1],total_x_keep_data[index][0],now_deep+1,now_y_keep_index+[0])

            print('f_f')
      

        elif set_keep_type == 'yf':
            print('s_yf')

            parent_x = parent_x[0] + parent_x[1]//2 # + x_line[1]%2 中心より右側の場合

            for index,line in enumerate(datas):

                # y_line ,parent_x
                y_line = self.y_keep_line.index(now_y_keep_index+[index])

                line_text = self.format_texts[y_line]
                self.format_texts[y_line] = line_text[:parent_x] + '┣' + line_text[parent_x+1:]

                if isinstance(line, (list, tuple, np.ndarray, dict)):

                    if isinstance(line, self.sequence_type):
                        # self.format_texts[y_line] = self.format_route(datas,now_deep+1,now_y_keep_index+[0],total_x_keep_data[0][1])
                        self.format_route(line,total_x_keep_data[0][1],total_x_keep_data[0][0],now_deep+1,now_y_keep_index+[index])
            
            line_text = self.format_texts[y_line]
            self.format_texts[y_line] = line_text[:parent_x] + '┗' + line_text[parent_x+1:]
                        
            print('e_yf')


        else:

            keep_x = set_keep_type == 'x'

            x_keep = 0
            y_keep = 0

            parent_x = parent_x[0] + parent_x[1]//2 # + x_line[1]%2 中心より右側の場合
            parent_y = self.y_keep_line.index(now_y_keep_index+[0]) -1
        

            for index,line in enumerate(datas):
            
                if keep_x:

                    # parent_y ,x_line
                    x_keep = index
                    x_line = total_x_keep_data[index] if type(total_x_keep_data[index][0]) != list else total_x_keep_data[index][0]

                    x_line = x_line[0] + x_line[1]//2 # + x_line[1]%2 中心より右側の場合

                    line_text = self.format_texts[parent_y]
                    if len(line_text) <= x_line:
                        self.format_texts[parent_y] =  line_text[:x_line] + (x_line - (len(line_text))) * ' ' + '┳'
                    else:
                        self.format_texts[parent_y] = line_text[:x_line] + '┳' + line_text[x_line+1:]
        
                else:

                    # y_line ,parent_x
                    y_keep = index
                    y_line = self.y_keep_line.index(now_y_keep_index+[index])

                    line_text = self.format_texts[y_line]
                    self.format_texts[y_line] = line_text[:parent_x] + '┣' + line_text[parent_x+1:]
                

                # self.format_texts[y_line] = 

                if isinstance(line, (list, tuple, np.ndarray, dict)):

                    if isinstance(line, self.sequence_type):
                        # self.format_texts[y_line] = self.format_route(datas,now_deep+1,now_y_keep_index+[direction_index],total_x_keep_data[direction_index][1])

                        self.format_route(line,total_x_keep_data[x_keep][1],total_x_keep_data[x_keep][0],now_deep+1,now_y_keep_index+[y_keep])

            if keep_x:
                
                line_text = self.format_texts[parent_y]
                
                if len(line_text) <= x_line:
                    self.format_texts[parent_y] =  line_text[:x_line] + (x_line - (len(line_text))) * ' ' + '┓'
                else:
                    self.format_texts[parent_y] = line_text[:x_line] + '┓' + line_text[x_line+1:]
                    
            else:
                line_text = self.format_texts[y_line]
                self.format_texts[y_line] = line_text[:parent_x] + '┗' + line_text[parent_x+1:]