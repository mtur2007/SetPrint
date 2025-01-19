from pynput import keyboard
import os

# サンプルデータ
data = [
    [0],[[1, 0],[1,1,1],[[2, 0, 0],[2, 1, 0],[[3,0],[3,1]]],[1,3]],[0,2]
]

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

def display_cards_horizontally(card_list, indices):
    """
    指定されたインデックスのカードを横に並べて表示する関数。

    Parameters:
        card_list (list): カードデザインが格納されたリスト。
        indices (list): 表示するカードのインデックスを指定するリスト。
    """
    # 指定されたインデックスのカードを抽出し、行単位に分割
    selected_cards = [card_list[i].splitlines() for i in indices]

    # 各カードの最大行数を取得
    max_lines = max(len(card) for card in selected_cards)

    # 全てのカードの行を揃える
    for card in selected_cards:
        while len(card) < max_lines:
            card.append(" " * len(card[0]))

    # 横に並べて表示
    for line_group in zip(*selected_cards):
        print("   ".join(line_group))

# 現在の要素とその詳細を表示する関数
def display_current_element(data,indices):
    #os.system('cls' if os.name == 'nt' else 'clear')  # 画面をクリア
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
        for p_line in parent_element:
            if type(p_line[0]) != list:
                parent_len += 1
        
        print(str(idx[-1]+1)+'/'+str(parent_len))
        
        display_cards_horizontally(card_designs_half_width,element)
        # print()

        # print(line*' ' + str(idx))
        # print(line*' ' + str(element))
    

    element = get_current_element(data, indices)

    parent_element = get_current_element(data, indices[:-1])
    parent_len = 0
    for p_line in parent_element:
        if type(p_line[0]) != list:
            parent_len += 1
    print(str(indices[-1]+1)+'/'+str(parent_len))

    display_cards_horizontally(card_designs_half_width,element)
        
    # print()
    # print((len(indices)-1) * ' ' + str(indices))
    # print((len(indices)-1) * ' ' + str(element))


# インデックスを更新する関数
def update_indices(direction, indices):

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
                # print('out_range_(over > before)',indices)
                del indices[-1]
                indices[-1] = indices[-1] + 1

                # print('out_range_(over ▷ after)',indices)
            else:
                # ( Under )
                del indices[-1]
                indices[-1] = indices[-1] - 1
                
                if 0 <= indices[-1] <= len(parent_element)-1:
                    indices = list_deep_search(parent_element,indices[:-1])
                    # print('back_index',indices)
                    
        else:
            if indices[-1] > len(parent_element)-1:
                indices = [-1]
            else:
                indices = list_deep_search(data,[])

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

card_designs_half_width = [
    """
    +---+
    | 0 |
    +---+
    """,
    """
    +---+
    | 1 |
    +---+
    """,
    """
    +---+
    | 2 |
    +---+
    """,
    """
    +---+
    | 3 |
    +---+
    """
]

# 初期状態を表示
# display_current_element()

# メインループ
print("\n操作: 'd'で次の要素、'a'で前の要素、'q'で終了")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
