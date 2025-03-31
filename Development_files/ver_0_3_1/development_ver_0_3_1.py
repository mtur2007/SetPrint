# / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict / demo / dict /
#print('\n'+'/ \033[38;5;27mdemo\033[0m / \033[38;2;255;165;0m\033[1mdict\033[0m '*10+'/\n')

# setpirnt (ver 0.3.0) [ demo ]

import numpy as np

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
def update_numpy_scalars_and_get_depth(obj):
    """
    オブジェクト内の NumPy のスカラー値（np.generic または ndim==0 の ndarray）を
    通常の Python のスカラー値に変換し、かつ最大入れ子深度（次元数）を取得する関数。
    
    戻り値は (updated_obj, depth) のタプルです。
    depth は以下のルールに従って定義:
      - 基本型やスカラーの場合は 0
      - コンテナの場合は 1 + max(child depths)（空の場合は 1）
    """
    # NumPy のスカラー（np.generic）の場合
    if isinstance(obj, np.generic):
        return obj.item(), 0

    # NumPy 配列の場合
    if isinstance(obj, np.ndarray):
        # スカラー配列の場合 (ndim == 0)
        if obj.ndim == 0:
            return obj.item(), 0
        # 非 object 型の配列は更新不要。深度はそのまま ndim を用いる
        if obj.dtype != np.object_:
            return obj, obj.ndim
        else:
            # object 型の NumPy 配列の場合、各要素を再帰的に更新
            new_obj = obj.copy()
            max_sub_depth = 0
            for idx, value in np.ndenumerate(new_obj):
                updated_val, sub_depth = update_numpy_scalars_and_get_depth(value)
                new_obj[idx] = updated_val
                if sub_depth > max_sub_depth:
                    max_sub_depth = sub_depth
            # 空の場合は 1、要素があれば 1 + 子要素の最大深度
            return new_obj, 1 + max_sub_depth if new_obj.size > 0 else 1

    # 辞書の場合: 値を更新し再帰的に深度を取得
    if isinstance(obj, dict):
        if not obj:
            return obj, 1
        new_dict = {}
        max_sub_depth = 0
        for key, value in obj.items():
            updated_val, sub_depth = update_numpy_scalars_and_get_depth(value)
            new_dict[key] = updated_val
            if sub_depth > max_sub_depth:
                max_sub_depth = sub_depth
        return new_dict, 1 + max_sub_depth

    # リストの場合: 各要素を更新
    if isinstance(obj, list):
        if not obj:
            return obj, 1
        new_list = []
        max_sub_depth = 0
        for item in obj:
            updated_item, sub_depth = update_numpy_scalars_and_get_depth(item)
            new_list.append(updated_item)
            if sub_depth > max_sub_depth:
                max_sub_depth = sub_depth
        return new_list, 1 + max_sub_depth

    # タプルの場合: 各要素を更新してタプルに再構成
    if isinstance(obj, tuple):
        if not obj:
            return obj, 1
        new_tuple = []
        max_sub_depth = 0
        for item in obj:
            updated_item, sub_depth = update_numpy_scalars_and_get_depth(item)
            new_tuple.append(updated_item)
            if sub_depth > max_sub_depth:
                max_sub_depth = sub_depth
        return tuple(new_tuple), 1 + max_sub_depth

    # その他の型はコンテナではないとみなし、更新せず深度は 0
    return obj, 0

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
        self.mapping_type = (dict,)
        self.collection_type = tuple(list(self.sequence_type) + list(self.mapping_type))

        # 入力データ('#'は引数の受け取り箇所)
        self.style_settings = (

          ("Collections" ,
            {  'image'   : { 'list'    : '►list' ,
                             'tuple'   : '▷tuple' ,
                             'ndarray' : '>ndarray' ,
                             'dict'    : '◆dict' }}),

        )
        
        # 制限('#'の箇所をまとめて管理)
        self.constraints = {
            ( 0, 1,     'image',    'list'    ) : {'type': str},
            ( 0, 1,     'image',   'tuple'    ) : {'type': str},
            ( 0, 1,     'image', 'ndarray'    ) : {'type': str},
            ( 0, 1,     'image',    'dict'    ) : {'type': str},
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
                f'   ({g}"Collections"{R} ,',
                "     {  'image'   : { "+f"'list'    {g}:{R} {quote}{c}{self.style_settings[0][1]['image']['list']}{quote} ,",
                f"                      'tuple'   {g}:{R} {quote}{c}{self.style_settings[0][1]['image']['tuple']}{quote} ,",
                f"                      'ndarray' {g}:{R} {quote}{c}{self.style_settings[0][1]['image']['ndarray']}{quote} ,",
                f"                      'dict'    {g}:{R} {quote}{c}{self.style_settings[0][1]['image']['dict']}{quote} }}}}),",
                '',
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

        y_keep_index = index[:]
        
        for deepnum in range(len(index)):
            set_type = self.keep_settings[deepnum]
            if set_type in ('x','f'):
                y_keep_index[deepnum] = 0
           
        return tuple(y_keep_index)
    
    # リストを整型する際の条件を整理 / １次元目の格納情報を整形 [→:#0]
    # [→:0] 中身は search_mapping / search_sequence とほぼ同じ
    def set_collection(self, route, y_axis, keep_settings):        
            
        dict_keep_settings = keep_settings

        #初期化
        self.now_deep = 0 #now_deepはインデックスの次元測定
        self.now_index = [] # 調べている場所のインデックスを格納する。
        self.keep_index = []

        self.Y_keep_index = {}
        self.X_keep_index = []

        self.keep_index = []
        self.y_flat_index = []
        
        # <t:初期化>

        #表示スタイルの更新
        self.collections = self.style_settings[0][1]['image']
        
        # 値を (値, 値の文字数) に変更
        self.collections = {key: (value, len(value)) for key, value in self.collections.items()}
        
        self.brackets = {'list': (('[', ']'), [1, 1]), 'tuple': (('(', ')'), [1, 1]), 'ndarray': (('[', ']'), [1, 1]), 'dict': (('{', '}'), [1, 1])}
        
        updated_data, max_depth = update_numpy_scalars_and_get_depth(self.input_list)
       
        keep_deeps = list(keep_settings.keys())
        max_keep_deep = max(keep_deeps)

        self.y_axis_image = '┊' if y_axis else ' '

        keep_settings = []

        range_keep_type = 'x'
        for deep in range(max_keep_deep):
            deep+=1
            if deep in dict_keep_settings.keys():
                range_keep_type = dict_keep_settings[deep]
                if range_keep_type == 'yf':
                    keep_settings.append(range_keep_type)
                    range_keep_type = 'f'
                else:
                    keep_settings.append(range_keep_type)

            else:
                keep_settings.append(range_keep_type)
        
        for deep in range(max_depth-len(keep_settings)):
            keep_settings.append(range_keep_type)
        
        print()
        print('all_deep_settings\n',keep_settings)

        self.keep_settings = keep_settings
        
        if isinstance(updated_data, self.mapping_type):
            x_keep_index = self.search_mapping(updated_data,[])
        else:
            x_keep_index = self.search_sequence(updated_data,[])

        # <a:keep_index>
        
        # <t:print>

        print()

        format_texts = self.format_keep_data(route,x_keep_index,self.Y_keep_index)

        # <t:return>

        return format_texts



    # [↺:1] マッピング型を調べる
    def search_mapping(self, datas, Kdeep_index):
        
        self.now_deep += 1 #deepはインデックスの次元測定
        
        # (P:2)
        # キープ範囲内にある次元の配列から情報を取得する。
        
        set_keep_type = self.keep_settings[self.now_deep-1]
        if set_keep_type == 'f':
            
            self.keep_index.append(-1)
            self.now_index.append('')
       
            # <t:start,In_range>
            
            len_Kdeep_index = len(Kdeep_index)

            if len_Kdeep_index == 0:
                Kdeep_index.append([0,self.brackets[type(datas).__name__][1][0],'a'])
                Kdeep_index.append([0,self.brackets[type(datas).__name__][1][1],'b'])
                len_Kdeep_index = 0
            else:
                if Kdeep_index[0][1] < self.brackets[type(datas).__name__][1][0]:
                    Kdeep_index[0][1] = self.brackets[type(datas).__name__][1][0]
                
                if Kdeep_index[-1][1] < self.brackets[type(datas).__name__][1][1]:
                    Kdeep_index[-1][1] = self.brackets[type(datas).__name__][1][1]
                
                len_Kdeep_index -= 2


            for linenum, (key, line) in enumerate(datas.items()):

                self.keep_index[-1] = linenum
                self.now_index[-1] = linenum

                self.y_flat_index.append(self.keep_index[:])

                linenum += 1

                if len_Kdeep_index < linenum:
                    Kdeep_index.insert(-1,[0,1])
               
                if isinstance(line, self.collection_type):
                    
                    # <t:collection_type,In_range>

                    if type(Kdeep_index[linenum][0]) != list:
                        key_len = max(Kdeep_index[linenum][0], len(str(key)))
                        value_len = max(Kdeep_index[linenum][1], self.collections[type(line).__name__][1])
                        Kdeep_index[linenum] = [[key_len,value_len],[]]
                    
                    else:
                        if Kdeep_index[linenum][0][0] < len(str(key)):
                            Kdeep_index[linenum][0][0] = len(str(key))

                        if Kdeep_index[linenum][0][1] < self.collections[type(line).__name__][1]:
                            Kdeep_index[linenum][0][1] = self.collections[type(line).__name__][1]
                                    
                    if type(line) == dict:
                        Kdeep_index[linenum][1] = self.search_mapping(line,Kdeep_index[linenum][1])
                    else:
                        Kdeep_index[linenum][1] = self.search_sequence(line,Kdeep_index[linenum][1])

                        # <t:配列の調査結果の受け取り,In_range>
                                        
                else:
                    
                    if type(Kdeep_index[linenum][0]) != list:
                        if Kdeep_index[linenum][0] < len(str(key)):
                            Kdeep_index[linenum][0] = len(str(key))

                        if Kdeep_index[linenum][1] < len(str(line)):
                            Kdeep_index[linenum][1] = len(str(line))
                    else:
                        if Kdeep_index[linenum][0][0] < len(str(key)):
                            Kdeep_index[linenum][0][0] =  len(str(key))

                        if Kdeep_index[linenum][0][1] < len(str(line)):
                            Kdeep_index[linenum][0][1] =  len(str(line))
                    
                    # <t:int/str_type,In_range>
            
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

            self.now_index.append('')

            parent_index = self.now_index.copy()
            parent_index[-1] = 'n'

            keep_x = self.keep_settings[self.now_deep-1] in ('x','f')
            direction_index = 0
            
            if not keep_x:
                if len(Kdeep_index) == 0:
                    Kdeep_index = [[0,1]]
                    #Kdeep_index = ['y']
                    
            len_Kdeep_index = len(Kdeep_index)-1

            for linenum, (key, line) in enumerate(datas.items()):
                self.now_index[-1] = linenum
                
                if keep_x:    
                    if len_Kdeep_index < linenum:
                        Kdeep_index.append([0,1])
                    direction_index = linenum                

                # インデックスのキープ化
                y_keep_index = self.transform_keep_index(self.now_index.copy())

                if y_keep_index not in self.Y_keep_index:
                    self.Y_keep_index[y_keep_index] = []

                self.Y_keep_index[y_keep_index].append([self.now_index[:-1],[[linenum]]])
                
                if isinstance(line, self.collection_type):
                    
                    # <t:collection_type,Out_of_range>

                    if len(line) != 0:                        
                        if type(Kdeep_index[direction_index][0]) != list:
                            key_len = max(Kdeep_index[direction_index][0], len(str(key)))
                            value_len = max(Kdeep_index[direction_index][1], self.collections[type(line).__name__][1])
                            Kdeep_index[direction_index] = [[key_len,value_len],[]]

                        else:
                            if Kdeep_index[direction_index][0][0] < len(str(key)):
                                Kdeep_index[direction_index][0][0] = len(str(key))
                        
                            if Kdeep_index[direction_index][0][1] < self.collections[type(line).__name__][1]:
                                Kdeep_index[direction_index][0][1] = self.collections[type(line).__name__][1]
                        
                        if type(line) == dict:
                            Kdeep_index[direction_index][1] = self.search_mapping(line,Kdeep_index[direction_index][1])
                        else:
                            Kdeep_index[direction_index][1] = self.search_sequence(line,Kdeep_index[direction_index][1])

                        # <t:配列の調査結果の受け取り,Out_of_range>
                    
                    else:
                        if type(Kdeep_index[direction_index][0]) != list:
                            if Kdeep_index[direction_index][0] < len(str(key)):
                                Kdeep_index[direction_index][0] = len(str(key))

                            if Kdeep_index[direction_index][1] < self.collections[type(line).__name__][1]:
                                Kdeep_index[direction_index][1] = self.collections[type(line).__name__][1]
                        else:
                            if Kdeep_index[direction_index][0][0] < len(str(key)):
                                Kdeep_index[direction_index][0][0] = len(str(key))

                            if Kdeep_index[direction_index][0][1] < self.collections[type(line).__name__][1]:
                                Kdeep_index[direction_index][0][1] = self.collections[type(line).__name__][1]

                else:
                    if type(Kdeep_index[direction_index][0]) != list:
                        if Kdeep_index[direction_index][0] < len(str(key)):
                            Kdeep_index[direction_index][0] = len(str(key))

                        if Kdeep_index[direction_index][1] < len(str(line)):
                            Kdeep_index[direction_index][1] = len(str(line))
                    else:
                        if Kdeep_index[direction_index][0][0] < len(str(key)):
                            Kdeep_index[direction_index][0][0] = len(str(key))

                        if Kdeep_index[direction_index][0][1] < len(str(line)):
                            Kdeep_index[direction_index][0][1] = len(str(line))
                
                    
                    # <t:int/str_type,Out_of_range>
            
            # <t:配列の調査完了,Out_of_range>


        del self.now_index[-1] #インデックスの調査が終わったら戻す
        self.now_deep -= 1

        return Kdeep_index

    # [↺:2] シーケンス型を調べる
    def search_sequence(self, datas, Kdeep_index):

        self.now_deep += 1 #deepはインデックスの次元測定
    
        # (P:2)
        # キープ範囲内にある次元の配列から情報を取得する。
        
        set_keep_type = self.keep_settings[self.now_deep-1]
        if set_keep_type == 'f':
            
            self.keep_index.append(-1)
            self.now_index.append('')

            # <t:start,In_range>
            
            len_Kdeep_index = len(Kdeep_index)

            if len_Kdeep_index == 0:
                Kdeep_index.append([0,self.brackets[type(datas).__name__][1][0],'a'])
                Kdeep_index.append([0,self.brackets[type(datas).__name__][1][1],'b'])
                len_Kdeep_index = 0
            else:
                if Kdeep_index[0][1] < self.brackets[type(datas).__name__][1][0]:
                    Kdeep_index[0][1] = self.brackets[type(datas).__name__][1][0]
                
                if Kdeep_index[-1][1] < self.brackets[type(datas).__name__][1][1]:
                    Kdeep_index[-1][1] = self.brackets[type(datas).__name__][1][1]
                
                len_Kdeep_index -= 2

            for linenum in range(len(datas)):

                line = datas[linenum]

                self.keep_index[-1] = linenum
                self.now_index[-1] = linenum

                self.y_flat_index.append(self.keep_index[:])

                linenum += 1

                if len_Kdeep_index < linenum:
                    Kdeep_index.insert(-1,[0,1])
               
                if isinstance(line, self.collection_type):
                    
                    # <t:collection_type,In_range>

                    if type(Kdeep_index[linenum][0]) != list:
                        Kdeep_index[linenum] = [[Kdeep_index[linenum][0],max(Kdeep_index[linenum][1], self.collections[type(line).__name__][1])],[]]
                    
                    else:
                        if Kdeep_index[linenum][0][1] < self.collections[type(line).__name__][1]:
                            Kdeep_index[linenum][0][1] = self.collections[type(line).__name__][1]
                                    
                    if type(line) == dict:
                        Kdeep_index[linenum][1] = self.search_mapping(line,Kdeep_index[linenum][1])
                    else:
                        Kdeep_index[linenum][1] = self.search_sequence(line,Kdeep_index[linenum][1])

                        # <t:配列の調査結果の受け取り,In_range>
                                        
                else:
                    
                    if type(Kdeep_index[linenum][0]) != list:
                        if Kdeep_index[linenum][1] < len(str(line)):
                            Kdeep_index[linenum][1] = len(str(line))
                    else:
                        if Kdeep_index[linenum][0][1] < len(str(line)):
                            Kdeep_index[linenum][0][1] =  len(str(line))
                    
                    # <t:int/str_type,In_range>
            
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

            self.now_index.append('')

            parent_index = self.now_index.copy()
            parent_index[-1] = 'n'

            keep_x = self.keep_settings[self.now_deep-1] in ('x','f')
            direction_index = 0
            
            if not keep_x:
                if len(Kdeep_index) == 0:
                    Kdeep_index = [[0,1]]
                    #Kdeep_index = ['y']

            len_Kdeep_index = len(Kdeep_index)-1

            for linenum in range(len(datas)):
                line = datas[linenum]

                self.now_index[-1] = linenum
                
                if keep_x:    
                    if len_Kdeep_index < linenum:
                        Kdeep_index.append([0,1])
                    direction_index = linenum
                
                # インデックスのキープ化
                y_keep_index = self.transform_keep_index(self.now_index.copy())

                if y_keep_index not in self.Y_keep_index:
                    self.Y_keep_index[y_keep_index] = []

                self.Y_keep_index[y_keep_index].append([self.now_index[:-1],[[linenum]]])
                
                if isinstance(line, self.collection_type):
                    
                    # <t:collection_type,Out_of_range>

                    if len(line) != 0:                        
                        if type(Kdeep_index[direction_index][0]) != list:
                            Kdeep_index[direction_index] = [[Kdeep_index[direction_index][0],max(Kdeep_index[direction_index][1], self.collections[type(line).__name__][1])],[]]

                        else:
                            if Kdeep_index[direction_index][0][1] < self.collections[type(line).__name__][1]:
                                Kdeep_index[direction_index][0][1] = self.collections[type(line).__name__][1]
                        
                        if type(line) == dict:
                            Kdeep_index[direction_index][1] = self.search_mapping(line,Kdeep_index[direction_index][1])
                        else:
                            Kdeep_index[direction_index][1] = self.search_sequence(line,Kdeep_index[direction_index][1])

                        # <t:配列の調査結果の受け取り,Out_of_range>
                    
                    else:
                        if type(Kdeep_index[direction_index][0]) != list:
                            if Kdeep_index[direction_index][1] < self.collections[type(line).__name__][1]:
                                Kdeep_index[direction_index][1] = self.collections[type(line).__name__][1]
                        else:
                            if Kdeep_index[direction_index][0][1] < self.collections[type(line).__name__][1]:
                                Kdeep_index[direction_index][0][1] = self.collections[type(line).__name__][1]

                else:
                    if type(Kdeep_index[direction_index][0]) != list:
                        if Kdeep_index[direction_index][1] < len(str(line)):
                            Kdeep_index[direction_index][1] = len(str(line))
                    else:
                        if Kdeep_index[direction_index][0][1] < len(str(line)):
                            Kdeep_index[direction_index][0][1] = len(str(line))
                    
                    # <t:int/str_type,Out_of_range>
            
            # <t:配列の調査完了,Out_of_range>


        del self.now_index[-1] #インデックスの調査が終わったら戻す
        self.now_deep -= 1

        return Kdeep_index


    # [→:3] キープデータの初期化/作成後の後処理
    def yf_setup(self,datas,parent_index,Kdeep_index):
        
        # 格納情報、次元情報、文字数を取得する為の処理

        # 格納情報の保存
        parent__keep_index = self.keep_index
        parent__y_flat_index = self.y_flat_index
        parent__X_keep_index = self.X_keep_index

        # 親キープインデックス
        parent_y_keep_index = self.transform_keep_index(parent_index)

        if parent_y_keep_index not in self.Y_keep_index:
            self.Y_keep_index[parent_y_keep_index] = []

        # <t:キープ初期化>

        self.keep_index = []

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
            Kdeep_index = [[0,1]]

        if type(datas) == dict:
            
            for linenum, (key, line) in enumerate(datas.items()):
                self.keep_line = [linenum]
                self.keep_index = []
                
                self.now_index[-1] = linenum

                # インデックスのキープ化
                y_keep_index = self.transform_keep_index(self.now_index)
                
                if y_keep_index not in self.Y_keep_index:
                    self.Y_keep_index[y_keep_index] = []
                
                self.y_flat_index = [[]]
                
                if isinstance(line, self.collection_type):
                    
                    # <t:collection_type,In_range>

                    if len(line) != 0:
                        if type(Kdeep_index[0][0]) != list:
                            key_len = max(Kdeep_index[0][0], len(str(key)))
                            value_len = max(Kdeep_index[0][1], self.collections[type(line).__name__][1])
                            Kdeep_index[0] = [[key_len,value_len],[]]

                        else:
                            if Kdeep_index[0][0][0] < len(str(key)):
                                Kdeep_index[0][0][0] = len(str(key))

                            if Kdeep_index[0][0][1] < self.collections[type(line).__name__][1]:
                                Kdeep_index[0][0][1] = self.collections[type(line).__name__][1]

                        # 以降の格納要素についてのキープデータ作成は search_ mapping,sequence 関数を使用する。
                        if type(line) == dict:
                            Kdeep_index[0][1] = self.search_mapping(line,Kdeep_index[0][1])
                        else:
                            Kdeep_index[0][1] = self.search_sequence(line,Kdeep_index[0][1])

                        # <t:配列の調査結果の受け取り,In_range>
                    
                    else:
                        if type(Kdeep_index[0][0]) != list:
                            if Kdeep_index[0][0] < len(str(key)):
                                Kdeep_index[0][0] = len(str(key))

                            if Kdeep_index[0][1] < self.collections[type(line).__name__][1]:
                                Kdeep_index[0][1] = self.collections[type(line).__name__][1]
                        else:
                            if Kdeep_index[0][0][0] < len(str(key)):
                                Kdeep_index[0][0][0] = len(str(key))

                            if Kdeep_index[0][0][1] < self.collections[type(line).__name__][1]:
                                Kdeep_index[0][0][1] = self.collections[type(line).__name__][1]

                else:
                    
                    # <t:int/str_type,In_range>

                    if type(Kdeep_index[0][0]) != list:
                        if Kdeep_index[0][0] < len(str(key)):
                            Kdeep_index[0][0] = len(str(key))

                        if Kdeep_index[0][1] < len(str(line)):
                            Kdeep_index[0][1] = len(str(line))
                    else:
                        if Kdeep_index[0][0][0] < len(str(key)):
                            Kdeep_index[0][0][0] = len(str(key))

                        if Kdeep_index[0][0][1] < len(str(line)):
                            Kdeep_index[0][0][1] = len(str(line))

                self.Y_keep_index[y_keep_index].append([self.now_index[:],self.y_flat_index[:]])

        else:
            for linenum in range(len(datas)):
                self.keep_line = [linenum]
                self.keep_index = []
                line = datas[linenum]
                
                self.now_index[-1] = linenum

                # インデックスのキープ化
                y_keep_index = self.transform_keep_index(self.now_index)
                
                if y_keep_index not in self.Y_keep_index:
                    self.Y_keep_index[y_keep_index] = []
                
                self.y_flat_index = [[]]
                
                if isinstance(line, self.collection_type):
                    
                    # <t:collection_type,In_range>

                    if len(line) != 0:
                        if type(Kdeep_index[0][0]) != list:
                            Kdeep_index[0] = [[Kdeep_index[0][0],max(Kdeep_index[0][1], self.collections[type(line).__name__][1])],[]]

                        else:
                            if Kdeep_index[0][0][1] < self.collections[type(line).__name__][1]:
                                Kdeep_index[0][0][1] = self.collections[type(line).__name__][1]

                        # 以降の格納要素についてのキープデータ作成は search_ mapping,sequence 関数を使用する。
                        if type(line) == dict:
                            Kdeep_index[0][1] = self.search_mapping(line,Kdeep_index[0][1])
                        else:
                            Kdeep_index[0][1] = self.search_sequence(line,Kdeep_index[0][1])

                        # <t:配列の調査結果の受け取り,In_range>
                    
                    else:
                        if type(Kdeep_index[0][0]) != list:
                            if Kdeep_index[0][1] < self.collections[type(line).__name__][1]:
                                Kdeep_index[0][1] = self.collections[type(line).__name__][1]
                        else:
                            if Kdeep_index[0][0][1] < self.collections[type(line).__name__][1]:
                                Kdeep_index[0][0][1] = self.collections[type(line).__name__][1]

                else:
                    
                    # <t:int/str_type,In_range>

                    if type(Kdeep_index[0][0]) != list:
                        if Kdeep_index[0][1] < len(str(line)):
                            Kdeep_index[0][1] = len(str(line))
                    else:
                        if Kdeep_index[0][0][1] < len(str(line)):
                            Kdeep_index[0][0][1] = len(str(line))

                self.Y_keep_index[y_keep_index].append([self.now_index[:],self.y_flat_index[:]])

        # print('return')
        # print(' > X.      ',self.range_idx)
        # print(' > Y.      ',self.Y_keep_index[parent_y_keep_index])
        # print(' > tracking',self.keep_tracking)
        # print()

        # <t:キープ範囲調査完了>
        
        # 情報復元
        self.keep_index = parent__keep_index
        self.y_flat_index = parent__y_flat_index
        self.X_keep_index = parent__X_keep_index

        return Kdeep_index


    def flat_x_keep_index(self,x_keep_index,index=[],keep_index=[],keep_len=[]):

        if self.keep_settings[len(index)] in ('x','y','yf'):
            for line,deep_data in enumerate(x_keep_index):
                
                if type(deep_data[0]) == list:
                    keep_index.append(index+[line])
                    keep_len.append(deep_data[0])
                    keep_index,keep_len = self.flat_x_keep_index(deep_data[1],index+[line],keep_index,keep_len)
                else:
                    keep_index.append(index+[line])
                    keep_len.append(deep_data)
                
            return keep_index,keep_len

        else:
            for line,deep_data in enumerate(x_keep_index):

                line -= 1
                
                if type(deep_data[0]) == list:
                    keep_index.append(index+[line])
                    keep_len.append(deep_data[0])
                    keep_index,keep_len = self.flat_x_keep_index(deep_data[1],index+[line],keep_index,keep_len)
                else:
                    keep_index.append(index+[line])
                    keep_len.append(deep_data)
                
            return keep_index,keep_len
    
    
    def map_sequence_indices(self,nested_list,indices):
        last_deep = len(indices)-1
        last_dict = None
        for now_deep,index in enumerate(indices):
            if isinstance(nested_list, self.mapping_type):
                last_dict = now_deep
                dict_key = list(nested_list.keys())[index]
                nested_list = list(nested_list.values())
                
            nested_list = nested_list[index]
        
        value = nested_list
        dict_key = dict_key if last_deep == last_dict else None
       
        return value,dict_key

    # [→:4] キープデータの整形
    def format_keep_data(self,route,X_keep_index,Y_keep_index):
        
        x_keep_index,keep_len = self.flat_x_keep_index(X_keep_index)
        x_keep_index.append(['end'])
        
        # キーを辞書順（インデックス順）でソート
        Y_keep_index = {k: Y_keep_index[k] for k in sorted(Y_keep_index)}
        format_texts = []

        for y_keep_index,y_line_data in Y_keep_index.items():
            # print(y_keep_index)
            now_line = 0
            line_txt = ''

            no_blanket_inmage = self.keep_settings[len(y_keep_index)-1] in ('y','x')

            
            if no_blanket_inmage:
        
                for parent,y_x_indexs in y_line_data:

                    keep_parent = parent[:]
                    parent_deep = len(parent)

                    for deep in range(parent_deep):
                        if self.keep_settings[deep] in ('y','yf'):
                            keep_parent[deep] = 0

                    # print(keep_parent)
                    
                    # print(parent,y_x_indexs,now_line)
                    
                    #print(search_index)
                    parent_list,no_use = self.map_sequence_indices(self.input_list,parent)
                    
                    for y_x_index in y_x_indexs:

                        keep_y_x_index = y_x_index[:]
                        for deep in range(len(y_x_index)):
                            if self.keep_settings[parent_deep+deep] in ('y','yf'):
                                keep_y_x_index[deep] = 0
                        
                        # print('search',keep_parent + keep_y_x_index)

                        while x_keep_index[now_line] != keep_parent + keep_y_x_index:
                            # print('False ',x_keep_index[now_line],keep_parent + y_x_index)
                            axis_len = keep_len[now_line]

                            if axis_len[0] == 0:
                                axis_len = axis_len[1]
                                a_2 = axis_len//2
                                if len(keep_len[now_line]) != 3:
                                    v_air = (a_2 - (1 - axis_len % 2)) * ' ' + self.y_axis_image + a_2*' '
                                else:
                                    v_air = (a_2 - (1 - axis_len % 2)) * ' ' + ' ' + a_2*' '

                            else:
                                axis_len = axis_len[0] + axis_len[1] + 1
                                a_2 = axis_len//2
                                if len(keep_len[now_line]) != 3:
                                    v_air = (a_2 - (1 - axis_len % 2)) * ' ' + self.y_axis_image + a_2*' '
                                else:
                                    v_air = (a_2 - (1 - axis_len % 2)) * ' ' + ' ' + a_2*' '
                            
                            line_txt += v_air + ' '
                            now_line += 1

                        # print('True  ',x_keep_index[now_line],keep_parent + keep_y_x_index)
                        # print()
                        
                        value,dict_key = self.map_sequence_indices(parent_list,y_x_index)
                        if isinstance(value, self.collection_type):
                            axis_len = keep_len[now_line]

                            value,image_len = self.collections[type(value).__name__]

                            dif = (axis_len[1] - image_len)
                            v_dif_2 = (dif // 2)
                        
                        else:
                            axis_len = keep_len[now_line]
                            
                            dif = (axis_len[1] - len(str(value)))
                            v_dif_2 = (dif // 2)
                        
                        if axis_len[0] == 0:
                            line_txt += v_dif_2*' ' + str(value) + (v_dif_2 + dif%2)*' ' + ' '
                        else:
                            if dict_key == None:
                                line_txt += axis_len[0]*'-' + '.' + v_dif_2*' ' + str(value) + (v_dif_2 + dif%2)*' ' + ' '
                            else:
                                k_dif = (axis_len[0] - len(str(dict_key)))
                                k_dif_2 = (k_dif // 2)
                                line_txt += k_dif_2*' ' + str(dict_key) + (k_dif_2 + k_dif%2)*' ' + ':' + v_dif_2*' ' + str(value) + (v_dif_2 + dif%2)*' ' + ' '
                                    
                        now_line += 1

            else:

                last_deep = None
                for now_deep,keep_setting in enumerate(self.keep_settings[len(y_keep_index):]):
                    if keep_setting != 'f':
                        last_deep = now_deep
                        break
                
                for parent,y_x_indexs in y_line_data:

                    keep_parent = parent[:]
                    parent_deep = len(parent)

                    for deep in range(parent_deep):
                        if self.keep_settings[deep] in ('y','yf'):
                            keep_parent[deep] = 0

                    # print(keep_parent)
                    
                    # print(parent,y_x_indexs,now_line)
                    
                    #print(search_index)
                    parent_list,dict_key = self.map_sequence_indices(self.input_list,parent)
                    value = parent_list
                    
                    before_nest = parent_deep
                    deep_types = []

                    while x_keep_index[now_line] != keep_parent:

                        axis_len = keep_len[now_line]

                        if axis_len[0] == 0:
                            axis_len = axis_len[1]
                            a_2 = axis_len//2
                            if len(keep_len[now_line]) != 3:
                                v_air = (a_2 - (1 - axis_len % 2)) * ' ' + self.y_axis_image + a_2*' '
                            else:
                                v_air = (a_2 - (1 - axis_len % 2)) * ' ' + ' ' + a_2*' '

                        else:
                            axis_len = axis_len[0] + axis_len[1] + 1
                            a_2 = axis_len//2
                            if len(keep_len[now_line]) != 3:
                                v_air = (a_2 - (1 - axis_len % 2)) * ' ' + self.y_axis_image + a_2*' '
                            else:
                                v_air = (a_2 - (1 - axis_len % 2)) * ' ' + ' ' + a_2*' '
                        
                        line_txt += v_air + ' '
                        now_line += 1
                        
                    if isinstance(value, self.collection_type):
                        
                        axis_len = keep_len[now_line]

                        data_type = type(value)
                        value,image_len = self.collections[type(value).__name__]

                        dif = (axis_len[1] - image_len)
                        v_dif_2 = (dif // 2)

                        if axis_len[0] == 0:
                            line_txt += v_dif_2*' ' + str(value) + (v_dif_2 + dif%2)*' ' + ' '
                        else:
                            if dict_key == None:
                                line_txt += axis_len[0]*'-' + '.' + v_dif_2*' ' + str(value) + (v_dif_2 + dif%2)*' ' + ' '
                            else:
                                k_dif = (axis_len[0] - len(str(dict_key)))
                                k_dif_2 = (k_dif // 2)
                                line_txt += k_dif_2*' ' + str(dict_key) + (k_dif_2 + k_dif%2)*' ' + ':' + v_dif_2*' ' + str(value) + (v_dif_2 + dif%2)*' ' + ' '
                                
                        
                        if last_deep != 0:
                            before_nest += 1
                            now_line += 1

                            deep_types.append(data_type)
                            bracket = self.brackets[data_type.__name__]
                            line_txt += (keep_len[now_line][1] - bracket[1][0])*' ' + bracket[0][0] + ' '
                        
                    else:

                        axis_len = keep_len[now_line]
                        
                        dif = (axis_len[1] - len(str(value)))
                        v_dif_2 = (dif // 2)
                        
                        if axis_len[0] == 0:
                            line_txt += v_dif_2*' ' + str(value) + (v_dif_2 + dif%2)*' ' + ' '
                        else:
                            if dict_key == None:
                                line_txt += axis_len[0]*'-' + '.' + v_dif_2*' ' + str(value) + (v_dif_2 + dif%2)*' ' + ' '
                            else:
                                k_dif = (axis_len[0] - len(str(dict_key)))
                                k_dif_2 = (k_dif // 2)
                                line_txt += k_dif_2*' ' + str(dict_key) + (k_dif_2 + k_dif%2)*' ' + ':' + v_dif_2*' ' + str(value) + (v_dif_2 + dif%2)*' ' + ' '
                                
                    now_line += 1

                    for y_x_index in y_x_indexs[1:]:

                        value,in_dect = self.map_sequence_indices(parent_list,y_x_index)

                        keep_y_x_index = y_x_index[:]
                        for deep in range(len(y_x_index)):
                            if self.keep_settings[parent_deep+deep] in ('y','yf'):
                                keep_y_x_index[deep] = 0
                        
                        now_deep = parent_deep + len(y_x_index)
                    
                        if 0 < before_nest - now_deep:

                            # line_txt += (keep_len[now_line] - len(']'))*' ' + ']' + ' '
                            
                            # del deep_types[-1]
                            # before_nest = len(y_x_index)
                            # now_line += 1
                            for i in range(before_nest - now_deep):
                                
                                while len(x_keep_index[now_line+1]) != before_nest -1:
                                   
                                    axis_len = keep_len[now_line]

                                    if axis_len[0] == 0:
                                        axis_len = axis_len[1]
                                        a_2 = axis_len//2
                                        if len(keep_len[now_line]) != 3:
                                            v_air = (a_2 - (1 - axis_len % 2)) * ' ' + self.y_axis_image + a_2*' '
                                        else:
                                            v_air = (a_2 - (1 - axis_len % 2)) * ' ' + ' ' + a_2*' '

                                    else:
                                        axis_len = axis_len[0] + axis_len[1] + 1
                                        a_2 = axis_len//2
                                        if len(keep_len[now_line]) != 3:
                                            v_air = (a_2 - (1 - axis_len % 2)) * ' ' + self.y_axis_image + a_2*' '
                                        else:
                                            v_air = (a_2 - (1 - axis_len % 2)) * ' ' + ' ' + a_2*' '
                                    
                                    line_txt += v_air + ' '
                                    now_line += 1

                                bracket = self.brackets[deep_types[-1].__name__]
                                line_txt += (keep_len[now_line][1] - bracket[1][1])*' ' + bracket[0][1] + ' '
                                
                                del deep_types[-1]
                                before_nest -= 1
                                now_line += 1
                           
                        while x_keep_index[now_line] != keep_parent + keep_y_x_index:

                            axis_len = keep_len[now_line]

                            if axis_len[0] == 0:
                                axis_len = axis_len[1]
                                a_2 = axis_len//2
                                if len(keep_len[now_line]) != 3:
                                    v_air = (a_2 - (1 - axis_len % 2)) * ' ' + self.y_axis_image + a_2*' '
                                else:
                                    v_air = (a_2 - (1 - axis_len % 2)) * ' ' + ' ' + a_2*' '

                            else:
                                axis_len = axis_len[0] + axis_len[1] + 1
                                a_2 = axis_len//2
                                if len(keep_len[now_line]) != 3:
                                    v_air = (a_2 - (1 - axis_len % 2)) * ' ' + self.y_axis_image + a_2*' '
                                else:
                                    v_air = (a_2 - (1 - axis_len % 2)) * ' ' + ' ' + a_2*' '
                            
                            line_txt += v_air + ' '
                            now_line += 1
                        
                        value,dict_key = self.map_sequence_indices(parent_list,y_x_index)

                        if isinstance(value, self.collection_type):
                            
                            axis_len = keep_len[now_line]

                            data_type = type(value)
                            value,image_len = self.collections[type(value).__name__]

                            dif = (axis_len[1] - image_len)
                            v_dif_2 = (dif // 2)

                            if axis_len[0] == 0:
                                line_txt += v_dif_2*' ' + str(value) + (v_dif_2 + dif%2)*' ' + ' '
                            else:
                                if dict_key == None:
                                    line_txt += axis_len[0]*'-' + '.' + v_dif_2*' ' + str(value) + (v_dif_2 + dif%2)*' ' + ' '
                                else:
                                    k_dif = (axis_len[0] - len(str(dict_key)))
                                    k_dif_2 = (k_dif // 2)
                                    line_txt += k_dif_2*' ' + str(dict_key) + (k_dif_2 + k_dif%2)*' ' + ':' + v_dif_2*' ' + str(value) + (v_dif_2 + dif%2)*' ' + ' '
                                    
                            
                            if last_deep != len(y_x_index):
                                before_nest += 1
                                now_line += 1

                                deep_types.append(data_type)
                                bracket = self.brackets[data_type.__name__]
                                line_txt += (keep_len[now_line][1] - bracket[1][0])*' ' + bracket[0][0] + ' '
                           
                        else:

                            axis_len = keep_len[now_line]
                            
                            dif = (axis_len[1] - len(str(value)))
                            v_dif_2 = (dif // 2)
                            
                            if axis_len[0] == 0:
                                line_txt += v_dif_2*' ' + str(value) + (v_dif_2 + dif%2)*' ' + ' '
                            else:
                                if dict_key == None:
                                    line_txt += axis_len[0]*'-' + '.' + v_dif_2*' ' + str(value) + (v_dif_2 + dif%2)*' ' + ' '
                                else:
                                    k_dif = (axis_len[0] - len(str(dict_key)))
                                    k_dif_2 = (k_dif // 2)
                                    line_txt += k_dif_2*' ' + str(dict_key) + (k_dif_2 + k_dif%2)*' ' + ':' + v_dif_2*' ' + str(value) + (v_dif_2 + dif%2)*' ' + ' '
                                    
                        now_line += 1
                        

                    if 0 < len(deep_types):

                        for i in range(len(deep_types)-1):

                            while len(x_keep_index[now_line+1]) != before_nest -1:

                                axis_len = keep_len[now_line]

                                if axis_len[0] == 0:
                                    axis_len = axis_len[1]
                                    a_2 = axis_len//2
                                    if len(keep_len[now_line]) != 3:
                                        v_air = (a_2 - (1 - axis_len % 2)) * ' ' + self.y_axis_image + a_2*' '
                                    else:
                                        v_air = (a_2 - (1 - axis_len % 2)) * ' ' + ' ' + a_2*' '

                                else:
                                    axis_len = axis_len[0] + axis_len[1] + 1
                                    a_2 = axis_len//2
                                    if len(keep_len[now_line]) != 3:
                                        v_air = (a_2 - (1 - axis_len % 2)) * ' ' + self.y_axis_image + a_2*' '
                                    else:
                                        v_air = (a_2 - (1 - axis_len % 2)) * ' ' + ' ' + a_2*' '
                                
                                line_txt += v_air + ' '
                                now_line += 1

                            bracket = self.brackets[deep_types[-1].__name__]
                            line_txt += (keep_len[now_line][1] - bracket[1][1])*' ' + bracket[0][1] + ' '
                            
                            del deep_types[-1]
                            before_nest -= 1
                            now_line += 1

                        # print(x_keep_index)

                        while len(x_keep_index[now_line]) > len(y_keep_index):
                            
                            axis_len = keep_len[now_line]

                            if axis_len[0] == 0:
                                axis_len = axis_len[1]
                                a_2 = axis_len//2
                                if len(keep_len[now_line]) != 3:
                                    v_air = (a_2 - (1 - axis_len % 2)) * ' ' + self.y_axis_image + a_2*' '
                                else:
                                    v_air = (a_2 - (1 - axis_len % 2)) * ' ' + ' ' + a_2*' '

                            else:
                                axis_len = axis_len[0] + axis_len[1] + 1
                                a_2 = axis_len//2
                                if len(keep_len[now_line]) != 3:
                                    v_air = (a_2 - (1 - axis_len % 2)) * ' ' + self.y_axis_image + a_2*' '
                                else:
                                    v_air = (a_2 - (1 - axis_len % 2)) * ' ' + ' ' + a_2*' '
                            
                            line_txt += v_air + ' '
                            now_line += 1

                        bracket = self.brackets[deep_types[-1].__name__]
                        line_txt = line_txt[:-(keep_len[now_line-1][1]+1)] + (keep_len[now_line-1][1] - bracket[1][1])*' ' + bracket[0][1] + ' '

            format_texts.append(line_txt)


        self.format_texts=format_texts[:]
        collection_image,image_len = self.collections[type(self.input_list).__name__]
        total_x_keep_data,map_width = self.total_x_keep_deata(X_keep_index,image_len+1)

        for line_num,line in enumerate(self.format_texts):
            self.format_texts[line_num] = image_len*' '+' ' + line
        
        self.format_texts.insert(0,collection_image+' ')
        self.y_keep_line = [list(t) for t in Y_keep_index.keys()]
        self.y_keep_line.insert(0,'')

        format_texts = self.format_texts[:]

        if route != 'maintenance':

            if self.y_axis_image != ' ':
                
                now_line = 0
                x_axis_txt = ''
                for nouse in range(len(x_keep_index) -1):
                    axis_len = keep_len[now_line]
                    axis_len = axis_len[1] if axis_len[0] == 0 else axis_len[0] + axis_len[1] +1
                    now_deep = len(x_keep_index[now_line])-1
                
                    a_2 = axis_len//2    

                    if len(keep_len[now_line]) != 3:
                        v_air = (a_2 - (1 - axis_len % 2)) * ' ' + self.y_axis_image + a_2*' '
                    else:
                        v_air = (a_2 - (1 - axis_len % 2)) * ' ' + ' ' + a_2*' '
                            
                    x_axis_txt += v_air + ' '
                    
                    now_line += 1

                for line_num,line in enumerate(format_texts):
                    format_texts[line_num] += x_axis_txt[len(line)-(image_len+1):]
                
                self.format_texts = format_texts[:]
                
            if route:
                self.format_route(self.input_list, total_x_keep_data, [0,image_len])
                format_texts_with_route = self.format_texts[:]

                # print()
                # print('with_route')
                # print('-'*map_width)
                # print()

                # for line in format_texts_with_route:
                #     print(line)
                
                # print()
                # print('-'*map_width)
                # print()

                format_texts_with_route = ['keep_settings',str(self.keep_settings),'-'*map_width+'\n'] + format_texts_with_route + ['\n'+'-'*map_width]

                return format_texts_with_route
            
            else:
                # print()
                # print('out_put')
                # print('-'*map_width)
                # print()

                # for line in format_texts:
                #     print(line)

                # print()
                # print('-'*map_width)
                # print()

                format_texts = ['keep_settings',str(self.keep_settings),'-'*map_width+'\n'] + format_texts + ['\n'+'-'*map_width]

                return format_texts

        else:
            self.format_route(self.input_list, total_x_keep_data, [0,image_len])
            format_texts_with_route = self.format_texts[:]

            format_texts_maintenance = []
            
            # print()
            
            format_texts_maintenance += ['with_route'+(map_width-10)*' '+'  / '+'out_put']
            format_texts_maintenance += ['='+'='*map_width+' ~ '+'-'+'-'*map_width + '\n']

            # print('with_route'+(map_width-10)*' '+'  / '+'out_put')
            # print('='+'='*map_width+' ~ '+'-'+'-'*map_width)
            # print()

            for line_with_route,line in zip(format_texts_with_route,format_texts):
                diff_air = (map_width - len(line_with_route))*' '
                # print(' '+line_with_route+diff_air+' :  '+line)
                format_texts_maintenance += [' '+line_with_route+diff_air+' :  '+line]
            
            # print()
            # print('='+'='*map_width+' ~ '+'-'+'-'*map_width)
            format_texts_maintenance += ['\n\n' + '='+'='*map_width+' ~ '+'-'+'-'*map_width]

            # print()
            
            # print()
            # print('with_route'+(map_width-10)*' '+' / '+'out_put')
            # print('┏━'+'━'*map_width+'━┱─'+'─'*map_width + '┐')
            # print('┃ '+' '*map_width+' ┃ '+' '*map_width + '│')
            
            # for line_with_route,line in zip(format_texts_with_route,format_texts):
            #     diff_air = (map_width - len(line_with_route))*' '
            #     print('┃ '+ line_with_route+diff_air +' ┃ '+ line+diff_air +'│')

            # print('┃ '+' '*map_width+' ┃ '+' '*map_width + '│')
            # print('┗━'+'━'*map_width+'━┹─'+'─'*map_width + '┘')
            # print()

            return format_texts_maintenance



    def total_x_keep_deata(self,x_keep_data,total_len=0):

        x_keep_total_len = []
            
        for line,deep_data in enumerate(x_keep_data):

            if type(deep_data[0]) == list:

                p_total_len = total_len
                if deep_data[0][0] == 0:
                    x_range_total_len,total_len = self.total_x_keep_deata(deep_data[1],total_len + deep_data[0][1] + 1)
                    x_keep_total_len.append([[p_total_len,deep_data[0][1]],x_range_total_len])
                else:
                    # p_total_len += deep_data[0][0] + 1
                    x_range_total_len,total_len = self.total_x_keep_deata(deep_data[1],total_len + deep_data[0][0] + deep_data[0][1] + 2)
                    x_keep_total_len.append([[p_total_len,deep_data[0][0]+deep_data[0][1]+1],x_range_total_len])
            else:
                if deep_data[0] == 0:
                    x_keep_total_len.append([total_len,deep_data[1]])
                    total_len += deep_data[1] +1
                else:
                    # total_len += deep_data[0] + 1
                    x_keep_total_len.append([total_len, deep_data[0] + deep_data[1] + 1])
                    total_len += deep_data[1] + deep_data[0] + 2
        
        return x_keep_total_len,total_len

    def format_route(self,datas,total_x_keep_data,parent_x=[0,0],now_deep=0,now_y_keep_index=[]):

        if isinstance(datas, self.mapping_type):
            datas = list(datas.values())

        set_keep_type = self.keep_settings[now_deep]
        
        if set_keep_type == 'f':
            for index,line in enumerate(datas):

                index += 1
                    
                if isinstance(line, (list, tuple, np.ndarray, dict)):
                    if len(line) != 0:
                        self.format_route(line,total_x_keep_data[index][1],total_x_keep_data[index][0],now_deep+1,now_y_keep_index+[0])

        elif set_keep_type == 'yf':
            
            parent_x_diff = parent_x[1]//2
            parent_x = parent_x[0] + parent_x_diff - (1 - parent_x[1]%2) # 偶数の場合は、中心より左側を中心とする。: - (1 - parent_x[1]%2)
            previous = self.y_keep_line.index(now_y_keep_index+[0])

            for index,line in enumerate(datas):

                # y_line ,parent_x
                y_line = self.y_keep_line.index(now_y_keep_index+[index])

                for line_plus in range (y_line - previous):
                    line_text = self.format_texts[previous+line_plus+1]  
                    if len(line_text) > parent_x:
                        self.format_texts[previous+line_plus+1] = line_text[:parent_x] + '┃' + line_text[parent_x+1:]
                    else:
                        self.format_texts[previous+line_plus+1] = line_text[:] + (parent_x - len(line_text))*' ' + '┃' + line_text[parent_x+1:]

                line_text = self.format_texts[y_line]
                self.format_texts[y_line] = line_text[:parent_x] + '┣' + '━'*parent_x_diff + line_text[parent_x+parent_x_diff+1:]

                if isinstance(line, (list, tuple, np.ndarray, dict)):
                    if len(line) != 0:
                        self.format_route(line,total_x_keep_data[0][1],total_x_keep_data[0][0],now_deep+1,now_y_keep_index+[index])

                previous = y_line

            line_text = self.format_texts[y_line]
            self.format_texts[y_line] = line_text[:parent_x] + '┗' + '━'*parent_x_diff + line_text[parent_x+parent_x_diff+1:]

        else:

            keep_x = set_keep_type == 'x'

            x_keep = 0
            y_keep = 0

            parent_x_diff = parent_x[1]//2
            parent_x = parent_x[0] + parent_x_diff - (1 - parent_x[1]%2) # 偶数の場合は、中心より左側を中心とする。: - (1 - parent_x[1]%2)
            
            parent_y = self.y_keep_line.index(now_y_keep_index+[0]) -1

            line_x_0 = total_x_keep_data[0] if type(total_x_keep_data[0][0]) != list else total_x_keep_data[0][0]
            previous = line_x_0[0] if keep_x else self.y_keep_line.index(now_y_keep_index+[0])

            for index,line in enumerate(datas):
            
                if keep_x:

                    # parent_y ,x_line
                    x_keep = index
                    x_line = total_x_keep_data[index] if type(total_x_keep_data[index][0]) != list else total_x_keep_data[index][0]

                    diff_2 = x_line[1]//2
                    x_line = x_line[0] + diff_2 - (1 - x_line[1]%2) # 偶数の場合は、中心より左側を中心とする。: - (1 - x_line[1]%2)

                    line_text = self.format_texts[parent_y]
                    self.format_texts[parent_y] = line_text[:previous] + (x_line - previous) * '━' + '┳' + line_text[x_line+1:]

                    previous = x_line +1
        
                else:

                    # y_line ,parent_x
                    y_keep = index
                    y_line = self.y_keep_line.index(now_y_keep_index+[index])

                    for line_plus in range (y_line - previous):
                        line_text = self.format_texts[previous+line_plus+1]  
                        if len(line_text) > parent_x:
                            self.format_texts[previous+line_plus+1] = line_text[:parent_x] + '┃' + line_text[parent_x+1:]
                        else:
                            self.format_texts[previous+line_plus+1] = line_text[:] + (parent_x - len(line_text))*' ' + '┃' + line_text[parent_x+1:]

                    line_text = self.format_texts[y_line]
                    self.format_texts[y_line] = line_text[:parent_x] + '┣' + '━'*parent_x_diff + line_text[parent_x+parent_x_diff+1:]

                    previous = y_line
            

                if isinstance(line, (list, tuple, np.ndarray, dict)):
                    if len(line) != 0:
                        self.format_route(line,total_x_keep_data[x_keep][1],total_x_keep_data[x_keep][0],now_deep+1,now_y_keep_index+[y_keep])

            if keep_x:
                
                line_text = self.format_texts[parent_y]
                self.format_texts[parent_y] = line_text[:x_line] + '┓' + line_text[x_line+1:]

                    
            else:
                for line_plus in range (y_line - previous):
                    line_text = self.format_texts[previous+line_plus+1]  
                    if len(line_text) > parent_x:
                        self.format_texts[previous+line_plus+1] = line_text[:parent_x] + '┃' + line_text[parent_x+1:]
                    else:
                        self.format_texts[previous+line_plus+1] = line_text[:] + (parent_x - len(line_text))*' ' + '┃' + line_text[parent_x+1:]

                line_text = self.format_texts[y_line]
                self.format_texts[y_line] = line_text[:parent_x] + '┗' + '━'*parent_x_diff + line_text[parent_x+parent_x_diff+1:]