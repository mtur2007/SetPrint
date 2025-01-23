from pynput import keyboard
import os

# 現在の位置情報を保持するインデックスリスト
current_indices = [-1]  # 必要な次元のみ保持q
current_depth = 0

# 現在のインデックスに基づいてデータを取得する関数
def get_current_element(data, indices):
    element = data
    for idx in indices:
        if isinstance(element, list) and idx < len(element):
            element = element[idx]
        else:
            break
    return element

def list_deep_search(data,idx):
    if type(data) == list :
        idx.append(len(data)-1)
        list_deep_search(data[len(data)-1],idx)

    return idx[:-1]

def display_cards_horizontally(indices):
    """
    指定されたインデックスのカードを横に並べて表示する関数。

    Parameters:
        card_list (list): カードデザインが格納されたリスト。
        indices (list): 表示するカードのインデックスを指定するリスト。
    """
    
    # 2段目（3次元目）
    card_lines = [cards[index].splitlines() for index in indices]
    max_lines = max(len(lines) for lines in card_lines)
    max_widths = [max(len(line) for line in lines) for lines in card_lines]
    padded_cards = []

    for lines, width in zip(card_lines, max_widths):
        padded_card = [line.ljust(width) for line in lines]
        padded_card += [" " * width] * (max_lines - len(lines))
        padded_cards.append(padded_card)
    
    for i in range(max_lines):
        print("   ".join(padded_cards[j][i] for j in range(len(padded_cards))))

# 現在の要素とその詳細を表示する関数
def display_current_element(data,indices):

    os.system('cls' if os.name == 'nt' else 'clear')  # 画面をクリア

    print("\n現在の要素を解析します:")
    print(f"現在のインデックス: {indices}")
    #route_index = route_index[-1]q
    #route_index[-1] -= 1
    for line in range(len(indices)-1):
        idx = indices[:line+1]
        idx[-1] -= 1
        element = get_current_element(data, idx)
        
        parent_element = get_current_element(data, idx[:-1])
        parent_len = 0
        line_index = idx[-1]
        for linenum,p_line in enumerate(parent_element):
            if type(p_line[0]) != list:
                parent_len += 1
            else:
                if linenum <= idx[-1]:
                    line_index -= 1

        
        print(str(line_index+1)+'/'+str(parent_len))
        
        display_cards_horizontally(element)
        # print()

        # print(line*' ' + str(idx))
        # print(line*' ' + str(element))
    

    element = get_current_element(data, indices)

    parent_element = get_current_element(data, indices[:-1])
    parent_len = 0
    line_index = indices[-1]
    for linenum,p_line in enumerate(parent_element):
        if type(p_line[0]) != list:
            parent_len += 1
        else:
            if linenum <= indices[-1]:
                line_index -= 1
    
    print(str(line_index+1)+'/'+str(parent_len))

    display_cards_horizontally(element)
        
    # print()
    # print((len(indices)-1) * ' ' + str(indices))
    # print((len(indices)-1) * ' ' + str(element))


# インデックスを更新する関数
def update_indices(direction, indices):

    global data

    element = get_current_element(data, indices)
    global current_indices

    parent_element = get_current_element(data, indices[:-1])

    indices[-1] += direction
    
    if 0 <= indices[-1] <= len(parent_element)-1:

        element = get_current_element(data, indices)
        
        if direction >= 0:
            if isinstance(element[0], list):
                indices.append(-1)  # 次の次元に進む
                update_indices(direction, indices)
            
            else:
                
                display_current_element(data,indices)
                print()
                print('->_pri ; ', element)
                
                # print()
        else:
            
            # print(indices)
            before_element = get_current_element(data, indices)
            # print()
            # print('<-_index  ',indices)
            # print('   element',element)

            indices = list_deep_search(before_element,indices)
            
            # print('back_index',indices)
            before_element = get_current_element(data, indices)

            display_current_element(data,indices)
            print()
            print('<-_pri ; ', before_element)
        

    else:
        # インデックスの範囲外

        if len(indices) >= 2:

            if indices[-1] > len(parent_element)-1:
                # ( over )
                print('over')
                # print('out_range_(over > before)',indices)
                del indices[-1]
                indices[-1] += 1

                # print('out_range_(over ▷ after)',indices)
            else:
                # ( Under )
                print('Under')
                del indices[-1]

                indices[-1] -= 1

                print(indices)
                
                if 0 <= indices[-1] <= len(parent_element)-1:
                    indices = list_deep_search(parent_element[indices[-1]],indices)
                    # print('back_index',indices)
                    
        else:
            if indices[-1] > len(parent_element)-1:
                print('0_over')
                indices = [-1]
            else:
                print('0_Under')
                indices = list_deep_search(data[-1],[len(parent_element)-1])

            # print('in_range_y0',indices)

        direction = 0
        update_indices(direction, indices)
        
    current_indices[:] = indices
    # display_current_element()


# キー操作の処理
def on_press(key):
    try:
        if key.char == 'd':  # 次の要素に進む
            update_indices(1, current_indices)
        elif key.char == 'a':  # 前の要素に戻る
            update_indices(-1, current_indices)
        elif key.char == 'q':  # 終了
            print("終了キー 'q' が押されました。プログラムを終了します。")
            return False
    except AttributeError:
        pass

cards = [
    """
    0_ In_range
        ┌┄┄┄┄┄┄ ‹ › ┄┄┄┄┄┄┄┄ [↺:(1,2)]
        ┆                     ˅   ˆ
        ┆                     ┃   ┆
        ┆           ┌┄┄ ‹ ┄(if:0) ┆
        ˆ           ┆   ┌ › ┄ ┃ ┄┄┤ 
        ˇ         ( ⤹   ↰  :  ⤹   ↰  / for:0 )
        ┆           ┆   ┆     ┆   ┆
        ┆        (if:1)┄┤  (if:1)┄┤
        ┆           ┆   ┆     ┆   ┆
        ├┄ ________ ‹ ┄┄┄┄┄┄┄┄┘   ┆
        └┄ › ________ ┄┄┴┄┄┄┄┄┄┄┄┄┘
    """,
#----------------------------------------
    """
    1_ In_range : int/str_type
        ┌┄┄┄┄┄┄ ‹ › ┄┄┄┄┄┄┄┄ [↺:(1,2)]
        ┆                     ˇ   ˆ
        ┆                     ┆   ┆
        ┆           ┌┄┄ ‹ ┄(if:0) ┆
        ˆ           ┆   ┌ › ┄ ┆ ┄┄┤ 
        ˇ         ( ⤹   ↰  :  ⤹   ↰  / for:0 )
        ┆           ┆   ┆     ┃   ┃
        ┆        (if:1)┄┤  (if:1)━┩
        ┆           ┆   ┆     ┆   ┆
        ├┄ ________ ‹ ┄┄┄┄┄┄┄┄┘   ┆
        └┄ › ________ ┄┄┴┄┄┄┄┄┄┄┄┄┘
    """,
#----------------------------------------
    """
    2_ In_range : collection_type
        ┏━━━━━━━━━ > ━━━━━━━ [↺:(1,2)]
        ┃                     ˇ   ˆ
        ┃                     ┆   ┆
        ┃           ┌┄┄ ‹ ┄(if:0) ┆
        ^           ┆   ┌ › ┄ ┆ ┄┄┤ 
                  ( ⤹   ↰  :  ⤹   ↰  / for:0 )
        ┃           ┆   ┆     ┃   ┆
        ┃        (if:1)┄┤  (if:1)┄┤
        ┃           ┆   ┆     ┃   ┆
        ┡━ ________ < ━━━━━━━━┛   ┆
        └┄ › ________ ┄┄┴┄┄┄┄┄┄┄┄┄┘
    """,
#----------------------------------------
    """
    3_ In_range : 配列の調査完了
        ┌┄┄┄┄┄┄ ‹ › ┄┄┄┄┄┄┄┄ [↺:(1,2)]
        ┆                     ˇ   ^
        ┆                     ┆   ┃
        ┆           ┌┄┄ ‹ ┄(if:0) ┃
        ˆ           ┆   ┌ › ┄ ┆ ┄┄┨
        ˇ         ( ⤹   ↰  :  ⤹   ↰  / for:0 )
        ┆           ┆   ┆     ┆   ┆
        ┆        (if:1)┄┤  (if:1)┄┤
        ┆           ┆   ┆     ┆   ┆
        ├┄ ________ ‹ ┄┄┄┄┄┄┄┄┘   ┆
        └┄ › ________ ┄┄┴┄┄┄┄┄┄┄┄┄┘
    """,
#----------------------------------------
    """
    4_ In_range : 配列の調査結果の受け取り
        ┏━━━━━━━━ < ━━━━━━━━ [↺:(1,2)]
        ┃                     ˇ   ˆ
        ┃                     ┆   ┆
        ┃           ┌┄┄ ‹ ┄(if:0) ┆
                    ┆   ┌ › ┄ ┆ ┄┄┤ 
        ˅         ( ⤹   ↰  :  ⤹   ↰  / for:0 )
        ┃           ┆   ┆     ┆   ┃
        ┃        (if:1)┄┤  (if:1)┄┨
        ┃           ┆   ┆     ┆   ┃
        ┠┄ ________ ‹ ┄┄┄┄┄┄┄┄┘   ┃
        ┗━━ > _______ ━━┷━━━━━━━━━┛
        """,
#----------------------------------------
    """
    5_ Out_of_range
        ┌┄┄┄┄┄┄ ‹ › ┄┄┄┄┄┄┄┄ [↺:(1,2)]
        ┆                     ˅   ˆ
        ┆                     ┃   ┆
        ┆           ┏━━ < ━(if:0) ┆
        ˆ           ┃   ┌ › ┄ ┆ ┄┄┤ 
        ˇ         ( ⤹   ↰  :  ⤹   ↰  / for:0 )
        ┆           ┆   ┆     ┆   ┆
        ┆        (if:1)┄┤  (if:1)┄┤
        ┆           ┆   ┆     ┆   ┆
        ├┄ ________ ‹ ┄┄┄┄┄┄┄┄┘   ┆
        └┄ › ________ ┄┄┴┄┄┄┄┄┄┄┄┄┘
    """,

#----------------------------------------
    """
    6_ Out_of_range : collection_type
        ┏━━━━━━━━━ > ━━━━━━━ [↺:(1,2)]
        ┃                     ˇ   ˆ
        ┃                     ┆   ┆
        ┃           ┌┄┄ ‹ ┄(if:0) ┆
        ^           ┆   ┌ › ┄ ┆ ┄┄┤ 
                  ( ⤹   ↰  :  ⤹   ↰  / for:0 )
        ┃           ┃   ┆     ┆   ┆
        ┃        (if:1)┄┤  (if:1)┄┤
        ┃           ┃   ┆     ┆   ┆
        ┡━ ________ < ┄┄┄┄┄┄┄┄┘   ┆
        └┄ › ________ ┄┄┴┄┄┄┄┄┄┄┄┄┘
    """,


#----------------------------------------
    """
    7_ Out_of_range : int/str_type
        ┌┄┄┄┄┄┄ ‹ › ┄┄┄┄┄┄┄┄ [↺:(1,2)]
        ┆                     ˇ   ˆ
        ┆                     ┆   ┆
        ┆           ┌┄┄ ‹ ┄(if:0) ┆
        ˆ           ┆   ┌ › ┄ ┆ ┄┄┤ 
        ˇ         ( ⤹   ↰  :  ⤹   ↰  / for:0 )
        ┆           ┃   ┃     ┆   ┆
        ┆        (if:1)━┩  (if:1)┄┤
        ┆           ┆   ┆     ┆   ┆
        ├┄ ________ ‹ ┄┄┄┄┄┄┄┄┘   ┆
        └┄ › ________ ┄┄┴┄┄┄┄┄┄┄┄┄┘
    """,

#----------------------------------------
    """
    8_ Out_of_range : 配列の調査完了
        ┌┄┄┄┄┄┄ ‹ › ┄┄┄┄┄┄┄┄ [↺:(1,2)]
        ┆                     ˇ   ^
        ┆                     ┆   ┃
        ┆           ┌┄┄ ‹ ┄(if:0) ┃
        ˆ           ┆   ┏ > ━ ┆ ━━┩
        ˇ         ( ⤹   ↰  :  ⤹   ↰  / for:0 )
        ┆           ┆   ┆     ┆   ┆
        ┆        (if:1)┄┤  (if:1)┄┤
        ┆           ┆   ┆     ┆   ┆
        ├┄ ________ ‹ ┄┄┄┄┄┄┄┄┘   ┆
        └┄ › ________ ┄┄┴┄┄┄┄┄┄┄┄┄┘
    """,
#----------------------------------------
    """
    9_ Out_of_range : 配列の調査結果の受け取り
        ┏━━━━━━━━ < ━━━━━━━━ [↺:(1,2)]
        ┃                     ˇ   ˆ
        ┃                     ┆   ┆
        ┃           ┌┄┄ ‹ ┄(if:0) ┆
                    ┆   ┌ › ┄ ┆ ┄┄┤ 
        ˅         ( ⤹   ↰  :  ⤹   ↰  / for:0 )
        ┃           ┆   ┃     ┆   ┆
        ┃        (if:1)┄┨  (if:1)┄┤
        ┃           ┆   ┃     ┆   ┆
        ┠┄ ________ ‹ ┄┄┄┄┄┄┄┄┘   ┆
        ┗━ > ________ ━━┹┄┄┄┄┄┄┄┄┄┘
    """,
#----------------------------------------
    """
    # 10_ None
    """,

]

    # サンプルデータ

data = []

def image_print(run_tracking):

    global data

    data = run_tracking


    # data = [[5], [6], [[0], [2], [[0], [2], [2, 0], [2, 1], [2, 2], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [2, 4], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [4], [2], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [4]], [9], [6], [[0], [2], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [4], [2], [[0], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4]], [4]], [9], [8]]


    # 初期状態を表示
    # display_current_element()

    # メインループ
    print("\n操作: 'd'で次の要素、'a'で前の要素、'q'で終了")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
