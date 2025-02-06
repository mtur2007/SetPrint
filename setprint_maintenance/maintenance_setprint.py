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
・初歩的な整列
'''

# リストに格納されている情報を文字とみて整列させる関数(main)
def set_txt(txtslist,mode,position):

    if mode == 0:
        Max = 0
        len_list = []

        for line in txtslist:
            len_list.append(len(line))
            if len(line) > Max:
                Max = len(line)

        New_list = []
        Line_list = []
        for nouse in range(Max):
            New_list.append("")

        for line in txtslist:
            Set_list = New_list[:]

            for number in range(len(line)):
                Set_list[number] = line[number]
            
            Line_list.append(Set_list)
        
        Line_list = np.array(Line_list)

        search_list = []
        for num in range(np.shape(Line_list)[1]):
            search_list.append(Line_list[:,num])

        search_list = np.array(set_txt(search_list,1,position))

        Line_list = []
        
        for num in range(np.shape(search_list)[1]):
            Line_list.append(search_list[:,num])
        
        returndata = []

        for line in range (np.shape(Line_list)[0]):
            cut = len_list[line]
            listline = Line_list[line].tolist()
            returndata.append(listline[:cut])

        return returndata

    
    elif mode == 1:

        for line in range(len(txtslist)):
            Maxtxtlen = 0

            for num in txtslist[line]:

                if len(str(num)) > Maxtxtlen:
                    Maxtxtlen = len(str(num))

            Maxlen = Maxtxtlen

            for nowread in range(len(txtslist[line])):
                txt = txtslist[line][nowread]
                Air = Maxlen - len(str(txt))

                if position == 0:

                    txtslist[line][nowread] = str(txt) + (Air * " ")
                elif position == 1:
                    txtslist[line][nowread] = (Air//2 * " ") + str(txt) + ((Air//2 + Air%2) * " ")
                elif position == 2:
                    txtslist[line][nowread] = (Air * " ") + str(txt)

        return txtslist#[:-1]

# リストに格納されている情報を文字とみて整列させる関数(引数処理)
def set_txts(txtslist,mode,position):

    if isinstance(txtslist[0], list) == False:
        txtslist = [txtslist]
        mode = 1

    if position == "left":
        position = 0
    if position == "center":
        position = 1
    if position == "right":
        position = 2

    txtslist = set_txt(txtslist,mode,position)

    return txtslist

'''
=============================================================================================================================================================
・配列のフラット化
'''

# 3次元配列を2次元にフラット化する関数
def slice_blocks(datas,mode):

    if isinstance(datas[0][0], list) == False:
        datas = [datas]
        mode = 1

    Allprint_txt = []
    Lineslist = []

    #リストの２次元配列ごとに, 3次元配列同士の要素を縦方向毎になる様に入れ変える
    for line in datas:
        # [[],[],[]]
        #  ^  ^  ^
        max= 0
        for data in line:
            # [ [ [],[] ], [ [],[] ] ,[ [],[] ] ]
            #      ^  ^       ^  ^       ^  ^

            if len(data) > max:
                max = len(data)

        printline = []
        for nouse in range(max):
            printline.append([])
        for data in line:
            if len(data) == 0:
                data.append("")
            for dataline in range(len(data)):
                printline[dataline].append(data[dataline])

            for num in range((max-1 - dataline)):
                printline[dataline + num+1].append('')

        for line in printline:
            Allprint_txt.append(line)
        
        Lineslist.append(len(Allprint_txt)-1)
    
    set_datas = set_txts(Allprint_txt,mode,0)

    set_shape = []
    start = 0
    finish = Lineslist[0] + 1
    set_shape.append(set_datas[start:finish])


    for linenum in range(len(Lineslist)-1):
        linenum += 1

        start = Lineslist[linenum-1] + 1
        finish = Lineslist[linenum] + 1
        set_shape.append(set_datas[start:finish])

    return set_shape

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
    ・ブロック状の配列にボーダーをつけ見やすくする関数。
    '''
    # ボーダーを追加する関数
    def blocks_border_print(self, **kwargs):

        #引数チェック
        key_list = ['All_blocks','line_title','guide']
        diff_key = list(kwargs.keys())
        for key in key_list:
            if key in kwargs:
                diff_key.remove(key)
        
        if len(diff_key) > 0:
            print(str(diff_key) + '存在しないキーです。')
            return KeyError
        
        if 'All_blocks' in kwargs:
            All_blocks = kwargs['All_blocks']
        else:
            All_blocks = self.input_list
        
        if 'line_title' in kwargs:
            line_title = kwargs['line_title']

        if 'guide' in kwargs:
            guide = kwargs['guide']
        else:
            guide = False

        # ボックス状の配列をスライスする。
        slice_data = slice_blocks(All_blocks,0)
        printlist = []
        linelen0 = 0

        if guide == True:
            maxlen_ytitle = 0
            for line in line_title:
                if maxlen_ytitle < len(str(line)):
                    maxlen_ytitle = len(str(line))
            maxlen_ytitle += 2
            sample_guide = f" {maxlen_ytitle * ' '} |  "
        else:
            sample_guide = "|  "

        list_index = []
        for linenum in range(len(slice_data)):
            dataline = slice_data[linenum]
            if len(dataline) != 0:
                writeline = []

                #それぞれのラインに横枠をつける
                list_index.append(dataline[0])
                printline = sample_guide + str(dataline[0][0]) + '   '
                
                for linenum in range(len(dataline)-1):
                    line = dataline[linenum+1]
                    printline = sample_guide
                    for txt in line:
                        printline +=  txt + "  |  "
                    printline = printline[:-2]

                    writeline.append(printline)

                linelen1 = len(sample_guide)+sum([len(str(line))+5 for line in dataline[0]])-2
                
                #横枠の作成...表示文字列列の以前の長さと現在の長さによって長さの基準を変える
                if linelen0 > linelen1:
                    printlist.append(f"{'='*linelen0}\n")
                    printlist.append('\n')
                else:
                    printlist.append(f"{'='*linelen1}\n")
                    printlist.append('\n')

                linelen0 = linelen1

                for line in writeline:
                    printlist.append(f"{line}\n")

                printlist.append('\n') # <※0>
            
            else:
                printlist.append(f"{'='*linelen0}\n")
                printlist.append('\n')
                if linenum != len(slice_data)-1:
                    printlist.append(f" >> Xx__No_data__xX\n")
                    printlist.append('\n')
                else:
                    printlist.append(f" >> Xx__No_data__xX\n")
                linelen0 = 0

        if len(slice_data[-1]) != 0:
            printlist.append(f"{'='*linelen1}\n")

        #ガイド(index)を追加する場合の処理
        if guide == True:

            sample_guide = f" {maxlen_ytitle * ' '} "
            set_index = 1
            for linenum in range(len(slice_data)):
                line = slice_data[linenum]
                indexline = list_index[linenum]

                if len(line) != 0:
                    if len(line_title)-1 >= linenum: 
                        txt = '{' + str(line_title[linenum]) + '}'
                    else:
                        txt = '{}'

                    air = (maxlen_ytitle - len(txt)) * ' '
                    guidex0 = ' ' + air + str(txt) + ' |  '
                    
                    guidex1 = sample_guide + '|--'
                    guidex2 = sample_guide + ':  '

                    for txtnum in range(len(line[0])):
                        txt_index = indexline[txtnum]

                        guidex0 += str(txt_index) + "  |  "
                        guidex1 += len(line[0][txtnum]) * "-" + "--|--"
                        guidex2 += len(line[0][txtnum]) * " " + "  :  "

                    printlist.insert(set_index,guidex0[:-2]+'\n')
                    printlist.insert(set_index+1,guidex1[:-2]+'\n')

                    printlist[set_index+2] = guidex2[:-2] + '\n' #更新場所プログラム内の印<※0>

                    set_index += len(line)+2 + 2

                else: #データがない時は1文で表示される為、例外処理
                    set_index += 1 +3

        return printlist

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
    
    def maintenance_run(self,*run_datas):
        
        run_title = run_datas[0]

        if run_title == '初期化':
            self.parent_len = 0
            self.run_tracking = []
            self.tracking_data = []
            self.keep_tracking = []
        
        elif run_title == 'キープ初期化':
            parent__parent_len = self.parent_len
            self.parent_len = self.now_deep-1
            print('parent_len',self.parent_len)
            
            parent__keep_tracking = self.keep_tracking[:]
            self.keep_tracking = []
            return parent__parent_len,parent__keep_tracking
        

        elif run_title in ('start','int/str_type','collection_type','配列の調査結果の受け取り','配列の調査完了'):

            range_type = run_datas[1]

            if run_title == 'start':
                self.run_tracking.append(0 if range_type == 'In_range' else 5)
                run_point = self.run_tracking

            elif run_title == 'int/str_type':
                self.run_tracking[-1] = 1 if range_type == 'In_range' else 7
                run_point = self.run_tracking

            elif run_title == 'collection_type':
                self.run_tracking[-1] = 2 if range_type == 'In_range' else 6
                run_point = self.run_tracking
            
            elif run_title == '配列の調査結果の受け取り':
                self.run_tracking[-1] = 4 if range_type == 'In_range' else 9
                run_point = self.run_tracking
                
            elif run_title == '配列の調査完了':
                del self.run_tracking[-1]
                run_point = self.run_tracking + [3] if range_type == 'In_range' else [8]

            if range_type == 'In_range':    
                self.keep_tracking.append(run_point[self.parent_len:])
            
            if range_type == 'Out_of_range':
                if run_title == 'start':
                    parent__keep_tracking = self.keep_tracking[:]
                    self.keep_tracking = []

                    self.keep_tracking.append([run_point[-1]])

                    return parent__keep_tracking

                self.keep_tracking.append([run_point[-1]])

                if run_title == '配列の調査完了':
                    parent__keep_tracking = run_datas[2]
                    self.keep_tracking = parent__keep_tracking + [ self.keep_tracking ]
        
        elif run_title == 'キープ範囲調査完了':

            if self.min_keep_deep != self.now_deep:
                self.parent_len = run_datas[1]
                print('back_parent_len',self.parent_len)
            
            del self.run_tracking[-1]

            parent__keep_tracking = run_datas[2]
            print('parent',parent__keep_tracking)
            
            self.keep_tracking = parent__keep_tracking + [ self.keep_tracking ]

        else:
            print(run_title)

    

    
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
        self.maintenance_run('初期化')


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

        print(keep_deeps)
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
        
        print('\n\nall_deep_settings\n',keep_settings)
        self.keep_settings = keep_settings
        
        if isinstance(datas, self.mapping_type):
            self.search_mapping(datas)
        else:
            x_keep_index = self.search_sequence(datas,[])

        # ber_print(3)
        if self.ber_print:
            print('\033[F\033[F\033[KThe search_collection process has been successfully completed.\n' + '{ '+'='*self.ber_len+' }')
        
        print()
        print('X_keep_index')
        for key,value in self.MAX_index.items():
            print(key,value)

        print()
        print('flat_X_keep_index')
        print(x_keep_index)
        
        # x_keep_index,keep_len = self.flat_x_keep_index(x_keep_index)
        # print(x_keep_index)
        # print(keep_len)

        print()
        print('Y_keep_index')
        for key,value in self.Y_keep_index.items():
            print(key,value)
        
        # <t:print>
        print()
        print('run_tracking')
        print(self.keep_tracking[0])


        print()

        self.format_keep_data(x_keep_index,self.Y_keep_index)

        # <t:return>
        return self.keep_tracking[0]


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
            print(' < f',Kdeep_index)
            
            self.keep_index.append(-1)
            self.now_index.append('')
       
            insert_index = self.keep_index[:]
           
            if (insert_index in self.range_idx) == False:
                self.range_idx.append(insert_index)
            
            len_Kdeep_index = len(Kdeep_index)-1

            # <t:start,In_range>
            self.maintenance_run('start','In_range')


            for linenum in range(len(datas)):

                line = datas[linenum]

                self.keep_index[-1] = linenum
                self.now_index[-1] = linenum

                insert_index = self.keep_index[:]

                self.y_flat_index.append(self.keep_index[:])

                if len_Kdeep_index < linenum:
                    Kdeep_index.append(linenum)
               
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
                    self.maintenance_run('collection_type','In_range')

                                 
                    if type(line) == dict:
                        self.search_mapping(line)
                    else:
                        Kdeep_index[linenum][1] = self.search_sequence(line,Kdeep_index[linenum][1])

                    # <t:配列の調査結果の受け取り,In_range>
                    self.maintenance_run('配列の調査結果の受け取り','In_range')

        
                else:
                    
                    if type(Kdeep_index[linenum]) != list:
                        if Kdeep_index[linenum] < len(str(line)):
                            Kdeep_index[linenum] = len(str(line))
                    else:
                        if Kdeep_index[linenum][0] < len(str(line)):
                            Kdeep_index[linenum][0] =  len(str(line))
                    
                    # <t:int/str_type,In_range>
                    self.maintenance_run('int/str_type','In_range')


                #存在するインデックスの情報の新規作成/更新
                if (insert_index in self.range_idx) == False:
                    self.range_idx.append(insert_index)
                
            insert_index = self.keep_index.copy()
            insert_index[-1] += 1

            if (insert_index in self.range_idx) == False:
                self.range_idx.append(insert_index)
            
            del self.keep_index[-1]

            # <t:配列の調査完了,In_range>
            self.maintenance_run('配列の調査完了','In_range')


            print(' > f',Kdeep_index)
        
        # (P:1)
        # キープする次元と現在の次元が同じなら、キープ用の処理に移る。
            
        elif set_keep_type == 'yf':

            print(' < yf',Kdeep_index)
            
            print()
            print('deep',self.now_deep)
            
            parent_index = self.now_index.copy() + [0]
            Kdeep_index = self.yf_setup(datas,parent_index,Kdeep_index)

            print(' > yf',Kdeep_index)

        # (P:0)
        else:

            print(' < y.x',Kdeep_index)

            # <t:start,Out_of_range>
            parent__keep_tracking = self.maintenance_run('start','Out_of_range')


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
                        Kdeep_index.append(linenum)
                    direction_index = linenum
                
                if self.min_keep_deep <= self.now_deep <= self.max_keep_deep:

                    # インデックスのキープ化
                    x_keep_index,y_keep_index = self.transform_keep_index(self.now_index.copy())

                    if x_keep_index not in self.MAX_index:
                        self.MAX_index[x_keep_index] = []
                    
                    if y_keep_index not in self.Y_keep_index:
                        self.Y_keep_index[y_keep_index] = []

                        print(self.now_index)
                        for key in self.Y_keep_index.keys():
                            print(key)
                    
                    print()
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
                    self.maintenance_run('collection_type','Out_of_range')


                    if type(line) == dict:
                        self.search_mapping(line)
                    else:
                        Kdeep_index[direction_index][1] = self.search_sequence(line,Kdeep_index[direction_index][1])

                    # <t:配列の調査結果の受け取り,Out_of_range>
                    self.maintenance_run('配列の調査結果の受け取り','Out_of_range')

                    
                    keep_liens_data.append(f'data_type: {type(line)}')
                else:
                    if type(Kdeep_index[direction_index]) != list:
                        if Kdeep_index[direction_index] < len(str(line)):
                            Kdeep_index[direction_index] = len(str(line))
                    else:
                        if Kdeep_index[direction_index][0] < len(str(line)):
                            Kdeep_index[direction_index][0] = len(str(line))
                    
                    # <t:int/str_type,Out_of_range>
                    self.maintenance_run('int/str_type','Out_of_range')


                    keep_liens_data.append(str(line))
            
            # <t:配列の調査完了,Out_of_range>
            self.maintenance_run('配列の調査完了','Out_of_range',parent__keep_tracking)


            print(' > y.x',Kdeep_index)

        del self.now_index[-1] #インデックスの調査が終わったら戻す
        self.now_deep -= 1

        return Kdeep_index

    # [→:3] キープデータの初期化/作成後の後処理
    def yf_setup(self,datas,parent_index,Kdeep_index):
        
        # 格納情報、次元情報、文字数を取得する為の処理

        # <t:キープ初期化>
        parent__parent_len,parent__keep_tracking = self.maintenance_run('キープ初期化')


        # 格納情報の保存
        parent__keep_index = self.keep_index
        parent__range_idx = self.range_idx
        parent__y_flat_index = self.y_flat_index
        parent__X_keep_index = self.X_keep_index
        now_keep_index = self.X_keep_index
        print('parent',parent__range_idx)

        # parent__MAX_index     = self.MAX_index # 存在する インデックス now_index[1:] の値を使用し、1列毎での整列を可能にする。
        # parent__MAX_indexlen  = self.MAX_indexlen # インデックスに格納されている配列の文字数を格納する。

        # parent__paretnt_key     = parent_key # 親インデックスのキー
        # parent__pivot_value     = self.pivot_value # 親インデックスのキー以降をmapping_keyに格納するための基準値設定。

        # parent__mapping_point   = self.mapping_point # 辞書型が存在している場所を格納する。
        # parent__mapping_key      = self.mapping_key # keep_keyに対応するマッピング型のキー
        
        # parent__keep_liens_data = keep_liens_data # 1列毎の配列情報を格納するリスト
        
        # parent__finish_index    = self.finish_index #リスト配列の最後尾のインデックスを格納

        # 格納情報の初期化

        # インデックスのキープ化
        parent_x_keep_index,parent_y_keep_index = self.transform_keep_index(parent_index)

        if parent_x_keep_index not in self.MAX_index:
            self.MAX_index[parent_x_keep_index] = []
        
        if parent_y_keep_index not in self.Y_keep_index:
            self.Y_keep_index[parent_y_keep_index] = []


        self.keep_index = []
        self.range_idx = self.MAX_index[parent_x_keep_index]
        print('X_range_idx',self.range_idx)
        print('Y_range_idx',self.Y_keep_index[parent_y_keep_index])
        
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
        # self.Xline_blocks.append('')
        # self.keep_txts_data.append('')
        # insert_index = len(self.Xline_blocks)-1
        

        # <t:start,In_range>
        self.maintenance_run('start','In_range')


        # print('start')
        # print(' < X.      ',self.range_idx)
        # print(' < Y.      ',self.Y_keep_index[parent_y_keep_index])
        # print(' < tracking',self.keep_tracking)

        if len(Kdeep_index) == 0:

            Kdeep_index = [[0,[]]]
            #Kdeep_index = [['yf',[]]]
        
        len_Kdeep_index = len(Kdeep_index)-1

        if type(datas) == dict:
            # self.now_key.append('')
            
            for linenum, (key, line) in enumerate(datas.items()):

                self.now_index[-1] = linenum
                # self.now_key[-1] = [self.now_deep-1,key]

                self.keep_line = [linenum]

                self.keep_index = []

                # self.mapping_point.append(self.keep_line + self.keep_index)
                # self.mapping_key.append(self.now_key[self.pivot_value:])

                if isinstance(line, (list, tuple, np.ndarray, dict)):
                    
                    # <t:collection_type,In_range>
                    self.maintenance_run('collection_type','In_range')

                    
                    # self.keep_1line_data = [] #1列の配列情報を格納するリスト
                    value_txt = self.collections[str(type(line).__name__)][0]
                    # self.keep_1line_data.append([self.keep_index,value_txt,key])

                    # 以降の格納要素についてのキープデータ作成は search_ mapping,sequence 関数を使用する。
                    if type(line) == dict:
                        self.search_mapping(line)
                    else:
                        self.search_sequence(line)
                    
                    # <t:配列の調査結果の受け取り,In_range>
                    self.maintenance_run('配列の調査結果の受け取り','In_range')

                
                    # keep_liens_data.append(self.keep_1line_data)
                
                else:

                    # <t:int/str_type,In_range>
                    self.maintenance_run('int/str_type','In_range')


                    value_line = str(line)
                    # keep_liens_data.append([[self.keep_index,value_line,key]])
                
                #存在するインデックスの情報の新規作成/更新
                if (self.keep_index in self.range_idx) == False:
                    self.range_idx.append(self.keep_index.copy())
                    # self.MAX_indexlen.append([len(str(key)),len(value_txt)])
                # else:
                #     if self.MAX_indexlen[self.MAX_index.index(self.keep_index)][0] < len(str(key)):
                #         self.MAX_indexlen[self.MAX_index.index(self.keep_index)][0] = len(str(key))

                #     if self.MAX_indexlen[self.MAX_index.index(self.keep_index)][1] < len(value_txt):
                #         self.MAX_indexlen[self.MAX_index.index(self.keep_index)][1] = len(value_txt)

                # ber_print(2)
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
                
                    print(':'*20,self.collections[type(line).__name__][1])
                    print(Kdeep_index[0][0])

                    # <t:collection_type,In_range>
                    self.maintenance_run('collection_type','In_range')


                    # self.keep_1line_data = [] #1列の配列情報を格納するリスト

                    value_txt = self.collections[str(type(line).__name__)][0]
                    # self.keep_1line_data.append([self.keep_index,value_txt])

                    # 以降の格納要素についてのキープデータ作成は search_ mapping,sequence 関数を使用する。

                    if type(line) == dict:
                        self.search_mapping(line)
                    else:
                        Kdeep_index[0][1] = self.search_sequence(line,Kdeep_index[0][1])

                    # <t:配列の調査結果の受け取り,In_range>
                    self.maintenance_run('配列の調査結果の受け取り','In_range')


                    # keep_liens_data.append(self.keep_1line_data)

                else:
                    
                    if type(Kdeep_index[0]) != list:
                        if Kdeep_index[0] < len(str(line)):
                            Kdeep_index[0] = len(str(line))
                    else:
                        if Kdeep_index[0][0] < len(str(line)):
                            Kdeep_index[0][0] = len(str(line))
                    
                    # <t:int/str_type,In_range>
                    self.maintenance_run('int/str_type','In_range')

                
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
        self.maintenance_run('キープ範囲調査完了', parent__parent_len,parent__keep_tracking)


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

        print('---------',self.input_list[0][0][1])

        print()
        self.a = X_keep_index
        x_keep_index,keep_len = self.flat_x_keep_index(X_keep_index)
        print(x_keep_index)
        print(keep_len)
        
        # キーを辞書順（インデックス順）でソート
        Y_keep_index = {k: Y_keep_index[k] for k in sorted(Y_keep_index)}

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
            

    # def range_deep_format(x_range_index,,line_txt=''):

    '''
    # [→:4] キープデータの整形
    def format_keep_data(self,keep_liens_data):
           
        1列毎に調査された内容毎をfor構文で回し、
        存在したインデックスが格納された配列と比べて整えていく。
        
        # その為には、両者の格納を昇降順にソートする必要があるのでsorted関数を使用する。
        sort_MAX_index = sorted(self.MAX_index)
        sort_MAX_indexlen = []
        for linenum,indexline in enumerate(sort_MAX_index):
            a = self.MAX_index.index(indexline)
            sort_MAX_indexlen.append(self.MAX_indexlen[a])

        self.MAX_index,self.MAX_indexlen = sort_MAX_index,sort_MAX_indexlen
        
        linenum = 0
        format_txtdata = []

        # 格納情報の中には リストである事を表す為に '[', "]" の情報が格納されており、pick_guideprint関数では扱われないようにする為、それらサブで調べる。

        # 他の列と格納状況が異なる箇所を格納する変数。存在だけを確認するのでset()。結果を用いて、見た目を変更する。
        mismatch_indices = set()
        
        for keep_linenum in range(len(keep_liens_data)):
            keep_line = keep_liens_data[keep_linenum]
            txt = ''
            
            linenum = 0
            for keep_txtnum in range(len(keep_line)):
                keep_txts = keep_line[keep_txtnum]
                index_line = self.MAX_index[linenum]
                noput_point = []

                # 両者のインデックスが同じだった場合。
                if keep_txts[0] == index_line:

                    index_len = self.MAX_indexlen[linenum]

                    if index_len[0] == 0:
                        value = (index_len[1] - len(keep_txts[1])) * self.padding_value + str(keep_txts[1])
                        txt += value + ' '

                    else:
                        if len(keep_txts) == 2:
                            key_empty = index_len[0] * self.empty_key
                            value = (index_len[1] - len(keep_txts[1])) * self.padding_value + str(keep_txts[1])
                            txt += key_empty + self.empty_colon + value + ' '
                        else:
                            key = (index_len[0] - len(str(keep_txts[2]))) * self.padding_key + str(keep_txts[2])
                            value = (index_len[1] - len(keep_txts[1])) * self.padding_value + str(keep_txts[1])
                            txt += key + self.padding_colon + value + ' '

                else:
                    #違かった場合、配列数が足りない 又は、違う次元があるのかを調べる
                    #         [ a, b, 'c', d ] 　   [ a, b, '[' a,b,c ], d  ]
                    #         [ a, b  "]"  -     　 [ a, b,  ^  ^ ^ ^ ^ 'd' ]

                    if keep_txts[0] == 'finish':
                        #配列が足りない場合は同じ次元の終わりのインデックスを検索項目にする。
                        search_finish = keep_txts[1][:-1]
                        search_finish.append(self.finish_index[str(search_finish)])
                        finish_value = keep_txts[2]
                    else:
                        #違う次元がある場合は現在のインデックスを検索項目にする。
                        search_finish = keep_txts[0]
                        finish_value = keep_txts[1]

                    while True:
                        #検索項目のインデックスが出てくるまで空白を挿入
                        index_len = self.MAX_indexlen[linenum]

                        if search_finish == self.MAX_index[linenum]:
                        
                            value_txt = str(finish_value)
                            value_txt = (index_len[1] - len(value_txt)) * self.padding_value + value_txt

                            if index_len[0] == 0:
                                txt += value_txt + ' '

                            else:
                                if len(keep_txts) == 2:
                                    key_empty = index_len[0] * self.empty_key
                                    txt += key_empty + self.empty_colon + value_txt + ' '
                                else:
                                    key = (index_len[0] - len(str(keep_txts[2]))) * self.padding_key + str(keep_txts[2])
                                    txt += key + self.padding_colon + value_txt + ' '
                            
                            break
                        else:
                            # 穴埋め時に他次元の情報が見つかったら、格納状況が異なる箇所として扱う
                            if self.MAX_index[linenum][-1] == -1:
                            
                                mismatch_indices.add(tuple(self.MAX_index[linenum][:-1]))
                        
                                key_index = self.MAX_index[linenum][:-1]
                                key_index.append(self.finish_index[str(key_index)])
                                noput_point.append(self.MAX_index.index(key_index))

                                txt += (index_len[1] * ' ') + ' '

                            else:
                                # 穴埋め時、格納状況が異なる箇所だった場合、空白ではなく '-' を挿入。
                                if (linenum in noput_point) != True:
                                    value_empty = index_len[1] * self.empty_value
                                    if index_len[0] == 0:
                                        txt += value_empty + ' '
                                    else:
                                        key_empty = index_len[0] * self.empty_key
                                        txt += key_empty + self.empty_colon + value_empty + ' '
                                else:
                                    del noput_point[noput_point.index(linenum)]
                                    txt += (index_len[1] * ' ') + ' '
                    
                        linenum += 1
                linenum += 1

            # 余った配列の穴埋め
            # [[~~~],[~~~], [========] ]
            # [[~~~],[~~~]] ^--------^
            for i in range(len(self.MAX_index) - linenum):
                i_index = self.MAX_index[linenum + i]

                if i_index[-1] == -1:

                    mismatch_indices.add(tuple(self.MAX_index[linenum][:-1]))    

                    key_index = i_index[:-1]
                    key_index.append(self.finish_index[str(key_index)])
                    noput_point.append(self.MAX_index.index(key_index))
                    txt += (self.MAX_indexlen[linenum + i][1] * ' ') + ' '
                else:
                    if ((linenum + i) in noput_point) != True:

                        index_len = self.MAX_indexlen[linenum + i]
                        value_empty = index_len[1] * self.empty_value

                        if index_len[0] == 0:
                            txt += value_empty + ' '
                        else:
                            key_empty = index_len[0] * self.empty_key
                            txt += key_empty + self.empty_colon + value_empty + ' '
                    else:

                        del noput_point[noput_point.index(linenum + i)]
                        txt += (self.MAX_indexlen[linenum + i][1] * ' ') + ' '

            format_txtdata.append(txt)

            # ber_print(3)
            if self.ber_print:
                if self.keep_start == 1:
                    now_len = int(self.line_ber_len*(keep_linenum+1))
                    print('\033[F\033[K{ '+'='*now_len+'-'*(self.ber_len-now_len)+' }')

        return format_txtdata,mismatch_indices
    '''
    '''
    =============================================================================================================================================================
    ・set_listで大まかなガイドが表示されるが、さらに詳しい格納情報を見ることが出来るようにする関数。
    '''

    # ブロック状の整形データにアクセスし、詳細を出力する関数
    def Block_GuidePrint(self, y,x,gx,gy):

        y = abs(self.y % len(self.block_keep_data))
        x = abs(self.x % len(self.block_keep_data[y]))
        if y == 0:
            self.y = 0
        if x == 0:
            self.x = 0
        
        k_data = self.block_keep_data[y][x]

        y_lens = len(self.block[y][x])-1

        if y_lens == 0:

            guide_index = ''
            no_color_ver = ''
            for line in k_data[0][:-1]:
                guide_index += f'[\033[38;2;127;82;0m{str(line)}\033[0m]'
                no_color_ver += '['+str(line)+']'
                
            # 行1を更新
            print("\033[F\033[F\033[Kindex \\ " + guide_index)
            # 行2を更新
            print(' value \\ \033[K'+'\033[1;32m_no_in_data_\033[30m'+'\033[0m')

            with open(self.output_path ,'w') as f:
                f.write('{guide}' + no_color_ver + '\n\n')

            return

        if len(k_data) == 6:
            class_index = k_data[0][:-1]
            indexs = k_data[1]
            x_lens = k_data[2]
            positions = k_data[3]
            mapping_point = k_data[4]
            mapping_key = k_data[5]

        elif len(k_data) >= 2:
            class_index = k_data[0][:-1]
            indexs = [[]]
            x_lens = [k_data[1]]
            positions = [0]
            if len(k_data) == 4:
                mapping_point = k_data[2]
                mapping_key = k_data[3]
            else:
                mapping_point = []
                mapping_key = []
        
        gy = abs(gy%y_lens)
        gx = abs(gx%len(positions))
        if gx == 0:
            self.gx = 0
        if gy == 0:
            self.gy = 0

        guide_index = ''
        no_color_ver = ''
        for line in class_index:
            guide_index += f'[\033[38;2;127;82;0m{str(line)}\033[0m]'
            no_color_ver += '['+str(line)+']'
        
        guide_index += f'{{\033[38;2;255;165;0m\033[1m{str(gy)}\033[0m}}'
        no_color_ver += '{'+str(gy)+'}'
        

        collection_index = [gy] + indexs[gx]
        this = class_index+collection_index
        matching_index = check_matching_elements(mapping_point, collection_index)
        if matching_index != -1:
            
            key_data = mapping_key[matching_index]
            
            for line in key_data:
                this[line[0]] = line[1]
            
            for line in this[len(class_index):]:
                guide_index += f'[\033[1;34m{str(line)}\033[0m]'
                no_color_ver += '['+str(line)+']'

        else:

            for line in indexs[gx]:
                guide_index += f'[\033[1;34m{str(line)}\033[0m]'
                no_color_ver += '['+str(line)+']'

        value = access_nested_collection(self.input_list,this)
        
        value_txt = str(value).replace(', ', ',').replace('\n', '')
        value_txt = value_txt if len(value_txt) < 140 else value_txt[:140] + ' ~'
        
        if isinstance(value,(list,tuple,np.ndarray)):
            in_data_txt = '\033[1;32m'+value_txt+'\033[30m : \033[1;34m'+ type(value).__name__ +'\033[0m'
        else:
            in_data_txt = '\033[1;32m'+value_txt+'\033[30m : \033[1;34m'+ type(value).__name__ +'\033[0m'
        
        # 行1を更新
        print("\033[F\033[F\033[Kindex \\ " + guide_index)
        # 行2を更新
        print(' value \\ \033[K'+in_data_txt+'\033[0m')
        
        guide = ' '
        for line in range(gx):
            guide += (positions[line]+1 - len(guide)) * ' '
            line = x_lens[line]
            guide += (line//2) * ' ' + '>'
        
        guide += (positions[gx]+1 - len(guide)) * ' '+ (x_lens[gx]//2)*' ' + ' ▼' + no_color_ver
        data = self.block[y][x]
        write_txt = []

        start = positions[gx]
        finish = start + x_lens[gx]
        for linenum in range(len(data)-1):
            line = data[linenum+1]
            write_txt.append(' ' + line[:start] +' '+ line[start:finish] +' '+ line[finish:])

        guide_line = '━' * len(write_txt[0])
        write_txt.insert(gy,guide_line)
        write_txt.insert(gy+2,guide_line)


        line = write_txt[gy]
        write_txt[gy] = line[:start] +' ┏'+ x_lens[gx]*' ' +'┓ '+ line[finish+4:]

        line = write_txt[gy+1]
        write_txt[gy+1] = line[:start] +'  '+ line[start+2:finish+2] + '  ' + line[finish+4:]

        line = write_txt[gy+2]
        write_txt[gy+2] = line[:start] +' ┗'+ x_lens[gx]*' ' +'┛ '+ line[finish+4:]


        with open(self.output_path ,'w') as f:
            
            f.write('{guide}' + guide + '\n\n')
            for line in write_txt:
                f.write('       ' + line + '\n')

            # f.write('\n')
            # keep_data = self.block_keep_data[y][x]
            # if len(keep_data) == 4:
            #     f.write((keep_data[3][gx]+8)*' '+str(keep_data[0])+'\n')
            #     for line in keep_data[1:]:
            #         f.write((keep_data[3][gx]+8)*' '+str(line[gx]) + '\n')
            # else:
            #     for line in keep_data:
            #         f.write(str(line)+'\n')

    # 入力キーに応じて ブロック間の場所(y,x)とブロック内の場所(gy,gx) の値を処理する関数
    def on_press(self, key):
        try:
            
            key = key.char

            if key in ('w','s','a','d'):
                if key == 'w':
                    self.gy -= 1
                elif key == 's':
                    self.gy += 1
                elif key == 'a':
                    self.gx -= 1
                elif key == 'd':
                    self.gx += 1
            else:
                if key == 't':
                    self.y -= 1
                elif key == 'g':
                    self.y += 1
                elif key == 'f':
                    self.x -= 1
                elif key == 'h':
                    self.x += 1
                
            self.Block_GuidePrint(self.y,self.x,self.gx,self.gy)


        except AttributeError:
            if key == keyboard.Key.esc:
                # ESC キーが押された場合に終了
                return False

    # 位置の初期化とキーボードのリスナーを開始する関数
    def pick_guideprint(self, output_path):

        # リスト内包表記を使って、キーに対応する値を取り出す
        try:
            set_data_dict = self.set_data_dict
        except:
            print('`pick_guidePrint`関数を実行するには "set_list"関数 を先に実行してください。')
            return
        
        self.input_list      = set_data_dict['input_list']
        self.block           = set_data_dict['grid_block']
        self.block_keep_data = set_data_dict['block_keep_data']

        self.output_path = output_path

        self.y,self.x = 0,0
        self.gy,self.gx = 0,0

        print()
        print('連動先のファイル : '+self.output_path)
        print()
        print()
        print()
        self.Block_GuidePrint(self.y,self.x,self.gx,self.gy)
        #キーボードのリスナーを開始
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()



'''
次元毎にリスト配列と整合性を取る形で文字の長さなのどを格納し、インデックスで指定できるようにする。
y,yf , x の部分はインデックスが0の箇所として格納する。
[10,20[5,3,2]]
'''
