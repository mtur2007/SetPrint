import os
from pynput import keyboard

cards = [
    """
# 0_ 範囲内
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
# 1_ 範囲内 int/str型
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
# 2_ 範囲内 配列型
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
# 3_ 範囲内 配列の調査完了
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
# 4_ 範囲内 再起の戻り
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
    ┗━━ > ________ ━━┷━━━━━━━━┛
    """,
#----------------------------------------
    """
# 5_ 範囲外
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
# 6_ 範囲外 配列型
    ┏━━━━━━━━━ > ━━━━━━━ [↺:(1,2)]
    ┃                     ˇ   ˆ
    ┃                     ┆   ┆
    ┃           ┌┄┄ ‹ ┄(if:0) ┆
    ˆ           ┆   ┌ › ┄ ┆ ┄┄┤ 
              ( ⤹   ↰  :  ⤹   ↰  / for:0 )
    ┃           ┃   ┆     ┆   ┆
    ┃        (if:1)┄┤  (if:1)┄┤
    ┃           ┃   ┆     ┆   ┆
    ┡━ ________ < ┄┄┄┄┄┄┄┄┘   ┆
    └┄ › ________ ┄┄┴┄┄┄┄┄┄┄┄┄┘
    """,


#----------------------------------------
    """
# 7_ 範囲外 int/str型
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
# 8_ 範囲外 配列の調査完了
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
# 9_ 範囲外 再起の戻り
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
# 10_ git 範囲外 再起の戻り
    ┌┄┄┄┄┄┄ ‹ › ┄┄┄┄┄┄┄┄ [↺:(1,2)]
    ┆                     ˇ   ˆ
    ┆                     ┆   ┆
    ┆           ┌┄┄ ‹ ┄(if:0) ┆
    ˆ           ┆   ┌ › ┄ ┆ ┄┄┤ 
    ˇ         ( ⤹   ↰  :  ⤹   ↰  / for:0 )
    ┆           ┆   ┆     ┆   ┆
    ┆        (if:1)┄┤  (if:1)┄┤
    ┆           ┆   ┆     ┆   ┆
    ├┄ ________ ‹ ┄┄┄┄┄┄┄┄┘   ┆
    └┄ › ________ ┄┄┴┄┄┄┄┄┄┄┄┄┘
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

    for i in range(max_lines):
        print("   ".join(padded_cards[j][i] for j in range(len(padded_cards))))
    print("\n")

def main():
    blocks = [[[0], [[0], [2], [2, 0], [2, 2], [2, 2, 0], [2, 2, 3], [2, 4], [2, 2], [2, 2, 0], [2, 2, 3], [2, 4], [2, 3], [4], [2], [2, 0], [2, 3], [4], [2], [2, 0], [2, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2], [2, 2, 2, 0], [2, 2, 2, 1], [2, 2, 2, 2], [2, 2, 2, 2, 0], [2, 2, 2, 2, 1], [2, 2, 2, 2, 1], [2, 2, 2, 2, 3], [2, 2, 2, 4], [2, 2, 2, 3], [2, 2, 4], [2, 2, 1], [2, 2, 3], [2, 4], [2, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2], [2, 2, 2, 0], [2, 2, 2, 1], [2, 2, 2, 1], [2, 2, 2, 3], [2, 2, 4], [2, 2, 1], [2, 2, 3], [2, 4], [2, 3], [4], [2], [2, 0], [2, 1], [2, 1], [2, 3], [4], [2], [2, 0], [2, 2], [2, 2, 0], [2, 2, 3], [2, 4], [2, 3], [4]]]]
    outer_index = 0  # 初期の1次元目のインデックス
    inner_index = 0  # 初期の3次元目のインデックス

    print_cards_in_blocks(blocks, outer_index, inner_index)

    def on_press(key):
        nonlocal outer_index, inner_index
        try:
            if key.char == 'a':  # 1次元目を左移動
                outer_index = (outer_index - 1) % len(blocks)
                print_cards_in_blocks(blocks, outer_index, inner_index)
            elif key.char == 'd':  # 1次元目を右移動
                outer_index = (outer_index + 1) % len(blocks)
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

if __name__ == "__main__":
    main()


groups = [[0], [2], [2,0], [2,1], [2,3], [5], [4]]  # グループ