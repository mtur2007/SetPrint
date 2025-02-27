# ネタ系お遊び/没プログラム : 線を辿るコード

import os
import time

def parse_ascii_art(ascii_art):
    grid = [list(line) for line in ascii_art.split("\n")]
    rows = len(grid)
    return grid, rows

def find_special_blocks(grid, symbols):
    special_blocks = {}
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char in symbols:
                special_blocks[(r, c)] = char
    return special_blocks

def map_special_blocks_to_labels(grid, special_blocks):
    map_mapping = grid.copy()
    label = "A"
    for (r, c) in special_blocks:
        map_mapping[r][c] = label
        label = chr(ord(label) + 1)  # Increment label to next letter

    for line in map_mapping:
        text = ''
        for txt in line:
            text += txt
        print(text)

# 線をたどるロジック

def trace_lines(grid, rows, show_logs=False, special_blocks=None, branch_directions=None, branch_states=None):
    if special_blocks is None:
        special_blocks = {}

    if branch_directions is None:
        branch_directions = {}

    if branch_states is None:
        branch_states = {key: True for key in branch_directions.keys()}  # デフォルトで全てTrue

    directions = {
        "ˇ": (1, 0),  # 下方向
        "ˆ": (-1, 0),  # 上方向
        "‹": (0, -1),  # 左方向
        "›": (0, 1),   # 右方向
    }
    direction_symbols = {
        "ˇ": "ᐁ",  # 下方向
        "ˆ": "ᐃ",  # 上方向
        "‹": "ᐊ",  # 左方向
        "›": "ᐅ",  # 右方向
    }
    corners = {
        "┐": {"ˆ": "‹", "›": "ˇ"},  # 上から右へ、右から下へ
        "└": {"ˇ": "›", "‹": "ˆ"},  # 下から左へ、左から上へ
        "┘": {"›": "ˆ", "ˇ": "‹"},  # 右から上へ、下から左へ
        "┌": {"ˆ": "›", "‹": "ˇ"},  # 上から右へ、左から下へ
        "├": {"ˇ": "branch", "‹": "branch", "ˆ": "branch"},  # 分岐（branch_directionsを参照）
        "┤": {"ˇ": "branch", "›": "branch", "ˆ": "branch"},  # 分岐（branch_directionsを参照）
        "┬": {"‹": "branch", "›": "branch", "ˆ": "branch"},  # 分岐（branch_directionsを参照）
        "┴": {"‹": "branch", "›": "branch", "ˇ": "branch"},  # 分岐（branch_directionsを参照）
        # "┼": {"‹": "‹", "›": "›", "ˆ": "ˆ", "ˇ": "ˇ"},  # 分岐（branch_directionsを参照）
    }
    lines = ("│",'┆',"─",'┄',"┼")

    position = None
    direction = "ˇ"  # 初期方向
    logs = []  # ログリスト

    for r, row in enumerate(grid):
        if "start" in "".join(row):
            if r + 1 < rows and "ˇ" in grid[r + 1]:
                position = (r + 1, grid[r + 1].index("ˇ"))
            break

    if not position:
        raise ValueError("Start position or `ˇ` not found in the grid.")
    
    while position:
        os.system('cls' if os.name == 'nt' else 'clear')
        grid_to_display = [row[:] for row in grid]
        r, c = position

        if r < 0 or r >= rows or c < 0 or c >= len(grid[r]):
            logs.append(f"Stopped: Out of bounds at Position: {position}, Direction: '{direction_symbols[direction]}'")
            break

        current = grid[r][c]
        grid_to_display[r][c] = "#"  # 現在位置を表示

        for line in grid_to_display:
            print("".join(line))

        if current in directions or current in lines:
            dr, dc = directions[direction]
            next_position = (r + dr, c + dc)
            logs.append(f"{direction_symbols[direction]} {current} at Position: {position}")
            position = next_position

        elif current in corners:
            if direction in corners[current]:
                if corners[current][direction] == "branch":
                    # 分岐処理
                    if (r, c) not in branch_directions:
                        logs.append(f"Stopped: Branch directions not defined for block at {position} ({current})")
                        break

                    true_direction, false_direction = branch_directions[(r, c)]
                    state = branch_states[(r, c)] # 分岐後の方向の取得

                    new_direction = true_direction if state else false_direction
                    dr, dc = directions[new_direction]
                    next_position = (r + dr, c + dc)

                    # 状態を切り替え
                    # branch_states[(r, c)] = not state

                    logs.append(f"Branch Block at {position}, Current State: {'True' if state else 'False'}, Next State: {'True' if branch_states[(r, c)] else 'False'}")
                    logs.append(f"Direction: {direction_symbols[direction]} -> {direction_symbols[new_direction]}")

                    direction = new_direction
                    position = next_position

                else:
                    new_direction = corners[current][direction]
                    dr, dc = directions[new_direction]
                    next_position = (r + dr, c + dc)
                    logs.append(f"{direction_symbols[direction]} {current}, Change Direction: {direction_symbols[direction]} -> {direction_symbols[new_direction]} at Position: {position}")
                    direction = new_direction
                    position = next_position
            else:
                logs.append(f"Stopped: Invalid corner handling at Character: {current}, Position: {position}, Direction: '{direction_symbols[direction]}'")
                break

        else:
            logs.append(f"Stopped: Unexpected character at Character: {current}, Position: {position}, Direction: '{direction_symbols[direction]}'")
            break

        time.sleep(0.5)  # 0.5秒待機して次のステップを表示

    print("\nFinal Logs:")
    for log in logs:
        print(log)

ascii_art = """
    start
        ˇ
        ├───┐
        │   ˇ
        │   ├────┐
        └───┘    ˆ
                 └──
"""

ascii_art = """
                                    
                           start end
                             ˇ    ˆ
                             ┆   ┌┘
    ┌┄┄┄┄┄┄┄┄┄┄┄┄‹┄┄┄┄┄┄┄┄┄┄┄┼┄┄┄┤
    ┆  ┌┄┄┄┄┄┄┄┄┄›┄┄┄┄┄┄┄┄┄┄┄┤:(1┆2)]
    ┆  ┆                     ˇ   ˆ
    ┆  ┆                     ┆   ┆
    ┆  ┆           ┌┄┄┄‹┄┄┄┄┄┤   ┆
    ˇ  ˆ           ┆   ┌┄›┄┄┄┼┄┄┄┤ 
    ┆  ┆         ( ├┄┄┄┤  :  ├┄┄┄┤  / for:0 )
    ┆  ┆           ┆   ┆     ┆   ┆
    ┆  ┆         ( ├┄┄┄┤  :  ├┄┄┄┤  / if:1)
    ┆  ┆           ┆   ┆     ┆   ┆
    ┆  └┄┄‹┄┄┄┄┄┄┄┄┴┄┄┄┼┄┄┄┄‹┘   ˆ
    └┄┄┄┄┄›┄┄┄┄┄┄┄┄┄┄┄┄┴┄┄┄┄┄┄┄┄┄┘
"""
# Find special blocks in the grid
special_symbols = ["├", "┤", "┬", "┴"]
grid, rows = parse_ascii_art(ascii_art)
special_blocks = find_special_blocks(grid, special_symbols)
# Map special blocks to labels
#map_special_blocks_to_labels(grid, special_blocks)

# Branch directions for if-like blocks

'''
侵入先の経路も可変的にする
'''
branch_directions = {

(5, 33): ( 'ˆ', ['ˇ', '›'] ),  # O : ┤
(6, 29): ( 'ˇ', ['›', 'ˆ'] ),  # P : ┤
(9, 29): ( 'ˇ', ['›', 'ˆ'] ),  # Q : ┤
(10, 33): ( 'ˆ', ['ˇ', '›'] ),  # R : ┤
(11, 19): ( 'ˇ', ['‹', 'ˆ'] ),  # S : ├
(11, 23): ( 'ˆ', ['ˇ', '›'] ),  # T : ┤
(11, 29): ( 'ˇ', ['‹', 'ˆ'] ),  # U : ├
(11, 33): ( 'ˆ', ['ˇ', '›'] ),  # V : ┤
(13, 19): ( 'ˇ', ['‹', 'ˆ'] ),  # W : ├
(13, 23): ( 'ˆ', ['ˇ', '›'] ),  # X : ┤
(13, 29): ( 'ˇ', ['‹', 'ˆ'] ),  # Y : ├
(13, 33): ( 'ˆ', ['ˇ', '›'] ),  # Z : ┤
(15, 19): ( 'ˇ', ['‹', '›'] ),  # [ : ┴
(16, 23): ( '›', ['‹', 'ˇ'] ),  # \ : ┴


}

# Initial states for each branch block
branch_states = {

    (5, 33): True,  # O : ┤
    (6, 29): True,  # P : ┤
    (9, 29): True,  # Q : ┤
    (10, 33): True,  # R : ┤
    (11, 19): True,  # S : ├
    (11, 23): True,  # T : ┤
    (11, 29): True,  # U : ├
    (11, 33): True,  # V : ┤
    (13, 19): True,  # W : ├
    (13, 23): True,  # X : ┤
    (13, 29): True,  # Y : ├
    (13, 33): True,  # Z : ┤
    (15, 19): True,  # < [ : ┴
    (16, 23): True,  # \ : ┴

}
    
corners = {
        "├": ("ˇ", "‹", "ˆ"),  # 分岐（branch_directionsを参照）
        "┤": ("ˇ", "›", "ˆ"),  # 分岐（branch_directionsを参照）
        "┬": ("‹", "›", "ˆ"),  # 分岐（branch_directionsを参照）
        "┴": ("‹", "›", "ˇ"),  # 分岐（branch_directionsを参照）
        "┼": ("‹", "›", "ˆ", "ˇ"),  # 分岐（branch_directionsを参照）
    }
a = {"‹": "›", "›": "‹", "ˆ": "ˇ", "ˇ": "ˆ"}
# # 実行
trace_lines(grid, rows, show_logs=True, special_blocks=special_blocks, branch_directions=branch_directions, branch_states=branch_states)

# Display the special_blocks dictionary
print("Special Blocks Dictionary:")
# label = "A"
# for position, block_type in special_blocks.items():
#     #print(f"Position: {position}, Block Type: {block_type}")
#     # print(f"{position}: ((), {corners[block_type]}),  # {block_type}")
#     print(f"{position}: {corners[block_type]},  # {label} : {block_type}")
#     label = chr(ord(label) + 1)  # Increment label to next letter
#     #print(position+':')
# print()
# for (position, block_type), (position, enter_direction) in zip(special_blocks.items(),branch_directions.items()):
#     #print(f"Position: {position}, Block Type: {block_type}")
#     # print(f"{position}: ((), {corners[block_type]}),  # {block_type}")
#     out_direction = [fit for fit in corners[block_type] if fit != enter_direction]
#     print(f"{position}: ( '{enter_direction}', {out_direction} ),  # {label} : {block_type}")
#     label = chr(ord(label) + 1)  # Increment label to next letter
#     #print(position+':')
# print()
for position, if_bool in branch_states.items():
    print(f"Position: {position} : {if_bool}")

