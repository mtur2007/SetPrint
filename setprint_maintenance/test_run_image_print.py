from pynput import keyboard
import os

# サンプルデータ
data = [
    [0, 0],[[1, 0],[1,1],[[2, 4]],[1,3]]
]

# 現在の位置情報を保持するインデックスリスト
current_indices = [-1]  # 必要な次元のみ保持
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

# 現在の要素とその詳細を表示する関数
def display_current_element():
    os.system('cls' if os.name == 'nt' else 'clear')  # 画面をクリア
    element = get_current_element(data, current_indices)
    print("\n現在の要素を解析します:")
    print(f"現在のインデックス: {current_indices}")

    if isinstance(element, list):
        print(f"次元 {len(current_indices)} → リストを検出しました。")
        for i, item in enumerate(element):
            if isinstance(item, list):
                print(f"  [{i}] リスト: 次元を移動できます。")
            else:
                print(f"  [{i}] 値: {item}")
    else:
        print(f"値: {element}")

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

                print('->_pri ; ', element)
                print()
        else:
            
            print(indices)
            before_element = get_current_element(data, indices)
            print('<-_parent',element)
            print('<-_index ',indices)

            # print('<-_pri ; ', before_element)

            # print(0 <= indices[-1] <= len(pparent_element)-1)
            
            if len(indices) >= 2:
                print('True deep_2')
                indices = list_deep_search(element,indices)

            print('back_index',indices)
            before_element = get_current_element(data, indices)
            print('<-_pri ; ', before_element)
            

    else:
        # インデックスの範囲外

        if len(indices) >= 2:

            if indices[-1] > len(parent_element)-1:
                # ( over )
                print('out_range_(over > before)',indices)
                del indices[-1]
                indices[-1] = indices[-1] + 1

                print('out_range_(over ▷ after)',indices)
            else:
                # ( Under )
                del indices[-1]
                indices[-1] = indices[-1] - 1
                
                if 0 <= indices[-1] <= len(parent_element)-1:
                    indices = list_deep_search(parent_element,indices)
                    print('back_index',indices)
                    
        else:
            if indices[-1] > len(parent_element)-1:
                indices = [-1]
            else:
                indices = list_deep_search(data,[])

            print('in_range_y0',indices)

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

# 初期状態を表示
# display_current_element()

# メインループ
print("\n操作: 'd'で次の要素、'a'で前の要素、'q'で終了")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
