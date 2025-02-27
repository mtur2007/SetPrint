def insert_text_after_match_with_indent(input_file, output_file, keep_index=True, tracking_image=True, tracking_rog=True):
    
    """
    テキストファイルを読み込み、指定したキーワードに一致する行の「次の行」から対応する複数行の文字列を
    検出した行の空白を維持した状態で挿入する。
  
    Parameters:
        input_file (str): 読み込むテキストファイルのパス
        output_file (str): 編集後のテキストファイルを保存するパス
        replacements (dict): { "検索するキーワード": ["挿入する文章1", "挿入する文章2", ...] } の辞書
    """

    replacements = merge_dicts_with_list(keep_index, tracking_image, tracking_rog)


    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        
        outfile.write('# / maintenance / maintenance / maintenance / maintenance / maintenance / maintenance / maintenance / maintenance / maintenance / maintenance /')
        outfile.write("\n# print('\\n'+'/ \\033[38;2;255;165;0m\\033[1mmaintenance\\033[0m / \\033[38;5;27mmaintenance\\033[0m '*5+'/\\n')\n")

        insert_lines = []  # 挿入する行のバッファ

        # 1行目と2行目をスキップ
        next(infile)  # 1行目スキップ
        next(infile)  # 2行目スキップ

        for line in infile:
            outfile.write(line)  # まず元の行を書き出す
            
            # 先頭の空白部分を取得（行頭のスペース or タブ）
            leading_whitespace = line[:len(line) - len(line.lstrip())]

            # キーワードをチェック
            for keyword, insert_texts in replacements.items():
                if keyword in line:  # キーワードを含む行を発見
                    # 挿入するテキストに空白を付加してバッファに追加
                    insert_lines.extend([leading_whitespace + text + "\n" for text in insert_texts])
                    insert_lines.append("\n")  # 追加した行の後に1行空白を挿入
                    break  # 最初にマッチしたもののみ適用

            # もし挿入する行があれば、それを次の行に書き込む
            if insert_lines:
                outfile.writelines(insert_lines)
                insert_lines = []  # バッファをリセット


def merge_dicts_with_list(*set_bools):

    merged_dict = {}

    for setting_num, set_bool in enumerate(set_bools):
        if set_bool:
            for key, value in maintenance_codes[setting_num].items():
                if key in merged_dict:  # 既存キーならリストに追加
                    merged_dict[key] += value
                else:
                    merged_dict[key] = value  # 新しいキーならリスト作成

    return merged_dict


maintenance_codes = [

    # keep_index
    {

        '# <a:keep_index>' : [

        '''
        print()
        print('X_keep_index')
        for key,value in self.MAX_index.items():
            print(key,value)

        print()
        print('flat_X_keep_index')
        print(x_keep_index)

        print()
        print('Y_keep_index')
        for key,value in self.Y_keep_index.items():
            print(key,value)
        '''

        ]

    },

    #tracking_image
    { 
    
        '# <t:maintenance_run>' : [

    '''
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
            
            del self.run_tracking[-1]

            parent__keep_tracking = run_datas[2]
            
            self.keep_tracking = parent__keep_tracking + [ self.keep_tracking ]

    '''

        ],

        '# <t:初期化>' : ["self.maintenance_run('初期化')"],
        
        '# <t:start,In_range>' : ["self.maintenance_run('start','In_range')"],
        '# <t:collection_type,In_range>' : ["self.maintenance_run('collection_type','In_range')"],
        '# <t:配列の調査結果の受け取り,In_range>' : ["self.maintenance_run('配列の調査結果の受け取り','In_range')"],
        '# <t:int/str_type,In_range>' : ["self.maintenance_run('int/str_type','In_range')"],
        '# <t:配列の調査完了,In_range>' : ["self.maintenance_run('配列の調査完了','In_range')"],
        
        '# <t:start,Out_of_range>' : ["parent__keep_tracking = self.maintenance_run('start','Out_of_range')"],
        '# <t:collection_type,Out_of_range>' : ["self.maintenance_run('collection_type','Out_of_range')"],
        '# <t:配列の調査結果の受け取り,Out_of_range>' : ["self.maintenance_run('配列の調査結果の受け取り','Out_of_range')"],
        '# <t:int/str_type,Out_of_range>' : ["self.maintenance_run('int/str_type','Out_of_range')"],
        '# <t:配列の調査完了,Out_of_range>' : ["self.maintenance_run('配列の調査完了','Out_of_range',parent__keep_tracking)"],
        
        '# <t:キープ初期化>' : ["parent__parent_len,parent__keep_tracking = self.maintenance_run('キープ初期化')"],
        '# <t:キープ範囲調査完了>' : ["self.maintenance_run('キープ範囲調査完了', parent__parent_len,parent__keep_tracking)"],

        '# <t:print>' : ["print()","print('run_tracking')","print(self.keep_tracking[0])"],

        '# <t:return>': ["return [ format_texts, self.keep_tracking[0] ]"]
    
    },

    # tracking_rog
    {

        '# <t:start,In_range>' : ["print(' < f',Kdeep_index)"],
        '# <t:配列の調査完了,In_range>' : ["print(' > f',Kdeep_index)"],

        '# <t:キープ初期化>' : ["print(' < yf',Kdeep_index)","print()","print('deep',self.now_deep)","print('parent',parent__range_idx)","print('X_range_idx',self.range_idx)","print('Y_range_idx',self.Y_keep_index[parent_y_keep_index])"],
        '# <t:キープ範囲調査完了>' : ["print(' > yf',Kdeep_index)"],

        '# <t:start,Out_of_range>' : ["print(' < y.x',Kdeep_index)"],
        '# <t:配列の調査完了,Out_of_range>' : ["print(' > y.x',Kdeep_index)"]
            
    }
]

"""
run_tracking
[[5], [6], [[5], [6], [[0], [2], [2, 0], [2, 1], [2, 2], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [2, 4], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [8]], [9], [6], [[5], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 2], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [2, 4], [2, 1], [2, 3], [4]], [9], [8]], [9], [8]]

run_tracking
[[5], [6], [[5], [6], [[0], [2], [2, 0], [2, 1], [2, 2], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [2, 4], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [8]], [9], [6], [[5], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [9], [6], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 2], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [2, 4], [2, 1], [2, 3], [4]], [9], [8]], [9], [8]]

"""