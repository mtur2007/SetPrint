import os
from pynput import keyboard

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

# 0 範囲内
# 1 範囲内 int/str型
# 2 範囲内 配列型
# 3 配列の調査完了
# 4 範囲外
# 5 アンワインド

def clear_screen():
    """画面をクリアする関数"""
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("\033c", end="")  # ANSIエスケープシーケンスで画面クリア

def print_cards_in_blocks(blocks, outer_index, inner_index):
    """
    1段目に2次元目、2段目に3次元目を表示する関数。

    :param blocks: ブロックリスト
    :param outer_index: 1次元目のインデックス
    :param inner_index: 3次元目のインデックス
    """
    clear_screen()
    block = blocks[outer_index]

    # 1段目（2次元目）
    first_layer = block[0]
    card_lines = [cards[index].splitlines() for index in first_layer]
    max_lines = max(len(lines) for lines in card_lines)
    max_widths = [max(len(line) for line in lines) for lines in card_lines]
    padded_cards = []

    for lines, width in zip(card_lines, max_widths):
        padded_card = [line.ljust(width) for line in lines]
        padded_card += [" " * width] * (max_lines - len(lines))
        padded_cards.append(padded_card)

    outer_air = len(str(len(blocks)-1))
    outer_count = (outer_air-len(str(outer_index))) * ' ' + str(outer_index)+' / '+str(len(blocks)-1)

    inner_air = len(str(len(block[1])-1))
    inner_count = (inner_air-len(str(inner_index))) * ' ' + str(inner_index)+' / '+str(len(block[1])-1)
    
    print('action_key normal : a - d')
    print('action_key keep   : w - s')
    print()
    if (outer_index == len(blocks)-1) and (inner_index == len(block[1])-1):
        print('[ normal : ' + outer_count + ' - keep : ' + inner_count + ' ] ----- ▶ Finish')
    elif inner_index == len(block[1])-1:
        print('[ normal : ' + outer_count + ' - keep : ' + inner_count + ' ] ----- ▶ Next ▷')
    else:
        print('[ normal : ' + outer_count + ' - keep : ' + inner_count + ' ] Start ▽')
    for i in range(max_lines):
        print("   ".join(padded_cards[j][i] for j in range(len(padded_cards))))
    print("\n")  # 段間の空行

    # 2段目（3次元目）
    second_layer = block[1][inner_index]
    card_lines = [cards[index].splitlines() for index in second_layer]
    max_lines = max(len(lines) for lines in card_lines)
    max_widths = [max(len(line) for line in lines) for lines in card_lines]
    padded_cards = []

    for lines, width in zip(card_lines, max_widths):
        padded_card = [line.ljust(width) for line in lines]
        padded_card += [" " * width] * (max_lines - len(lines))
        padded_cards.append(padded_card)
    
    print('[ keep : ' + inner_count + ' ] Start ▷' if inner_index != len(block[1])-1 else '[ keep : ' + inner_count + ' ] ----- ▶ Finish ▲')
    for i in range(max_lines):
        print("   ".join(padded_cards[j][i] for j in range(len(padded_cards))))
    print("\n")

def image_print(blocks):
    outer_index = 0  # 初期の1次元目のインデックス
    inner_index = 0  # 初期の3次元目のインデックス

    print_cards_in_blocks(blocks, outer_index, inner_index)

    def on_press(key):
        nonlocal outer_index, inner_index
        try:
            if key.char == 'a':  # 1次元目を左移動
                outer_index = (outer_index - 1) % len(blocks)
                inner_index = 0
                print_cards_in_blocks(blocks, outer_index, inner_index)
            elif key.char == 'd':  # 1次元目を右移動
                outer_index = (outer_index + 1) % len(blocks)
                inner_index = 0
                print_cards_in_blocks(blocks, outer_index, inner_index)
            elif key.char == 'w':  # 3次元目を前移動
                inner_index = (inner_index - 1) % len(blocks[outer_index][1])
                print_cards_in_blocks(blocks, outer_index, inner_index)
            elif key.char == 's':  # 3次元目を後移動
                inner_index = (inner_index + 1) % len(blocks[outer_index][1])
                print_cards_in_blocks(blocks, outer_index, inner_index)
            elif key.char == 'q':  # 終了
                print("終了します。")
                return False  # リスナーを停止
        except AttributeError:
            pass

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


