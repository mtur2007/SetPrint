from setprint import SetPrint

def generate_ranges_from_phrases(file_path, range_phrases):
    """
    複数のフレーズに基づいて範囲を生成する。

    :param file_path: テキストファイルのパス
    :param range_phrases: 範囲生成に使用するフレーズのリスト
    :return: 範囲リスト [[start, finish], ...]
    """
    line_numbers = []

    try:
        # ファイル内の行番号を収集
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if any(phrase in line for phrase in range_phrases):
                    line_numbers.append(line_number)
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
        return []
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return []

    # 範囲を生成（n番目~n+1番目）
    ranges = [[line_numbers[i], line_numbers[i + 1] - 1] for i in range(len(line_numbers) - 1)]
    return ranges


def find_lines_with_dynamic_ranges(file_path, phrases, range_phrases):
    """
    複数のフレーズで生成した範囲を基に、別のフレーズの行番号を範囲ごとに探す。

    :param file_path: テキストファイルのパス
    :param phrases: 検索対象のフレーズリスト
    :param range_phrases: 範囲生成に使用するフレーズのリスト
    :return: 結果リスト（範囲ごとの一致行番号）
    """
    # 範囲を生成
    ranges = generate_ranges_from_phrases(file_path, range_phrases)
    if not ranges:
        print(f"範囲が生成できませんでした。")
        return []

    # フレーズごとの行番号を収集
    phrase_lines = {phrase: [] for phrase in phrases}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                for phrase in phrases:
                    if phrase in line:
                        phrase_lines[phrase].append(line_number)
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
        return []
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return []

    # 範囲ごとに整理
    results = []
    for phrase in phrases:
        phrase_result = []
        for start, finish in ranges:
            in_range_lines = [ln for ln in phrase_lines[phrase] if start <= ln <= finish]
            phrase_result.append(in_range_lines)
        results.append(phrase_result)

    return results

# 使用例
file_path = '/Users/matsuurakenshin/WorkSpace/development/setprint_package/setprint_update/test_setprint_0_3_0.py'  # ファイルのパスを指定
range_phrases = ['def set_list', 'def search_mapping', 'def search_sequence', 'def keep_setup']  # 範囲生成に使用する複数のフレーズ
phrases = ["# (P:0)", "# (P:1)", "# (P:2)"]  # 検索対象のフレーズ
point_coment = ['キープ無しでブロック化','キープブロック化 (キープデータの初期化)','キープブロック化 (キープデータへ格納情報を格納)']
# 関数を呼び出して結果を取得
results = find_lines_with_dynamic_ranges(file_path, phrases, range_phrases)

results = [[['→:0'],['↺:1'],['↺:2']]] + results
list_data = SetPrint(results)

arguments = (
                    
   (("Collections" , 
        { 'image'    : {'list'   :'',
                        'tuple'  :'▷tuple',
                        'ndarray':'>numpy'}}),
    ("bracket"     , 
        { 'partially': {'list'   :('{',')'),                 
                        'tuple'  :('<','>'),
                        'ndarray':('(','}'),
                        'None'   :('`','`')}}),
                                        
    ("empty"       , { 'style' : ' '}),
    ("padding"     , { 'style' : '-'}),

    ("settings"    , { 'print' : False }), # <- New  True (display) / False (hide)

    ("progress"    , { 'print' : False ,   # <- New  True (display) / False (hide)
                        'len'   : 20 }))

    
)

list_data.set_text_style(arguments) # set_listの前
set_data = list_data.set_list(guide=False,keep_start=1,keep_range='all')['grid_block'][0][0][1:]

# 結果を表示
print("動的範囲ごとの一致行番号:")
print('        |'+set_data[0]+'|')
print('---------'+len(set_data[0])*'-'+'-')
for i, phrase_results in enumerate(set_data[1:]):
    print(f"{phrases[i]} :{phrase_results}: {point_coment[i]}")
