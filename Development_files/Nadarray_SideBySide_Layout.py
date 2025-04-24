def combine_blocks_with_block_titles(*blocks, separator="  :  "):
    split_blocks = []

    for block in blocks:
        if isinstance(block, list):
            split_blocks.append([str(line) for line in block])
        elif isinstance(block, str):
            split_blocks.append(block.splitlines())
        else:
            raise ValueError("Each block must be a string or a list of strings.")

    block_widths = [max((len(line) for line in block), default=0) for block in split_blocks]
    max_lines = max(len(block) for block in split_blocks)

    padded_blocks = []
    for block, width in zip(split_blocks, block_widths):
        padded = [line.ljust(width) for line in block]
        padded += [" " * width] * (max_lines - len(padded))
        padded_blocks.append(padded)

    # タイトル行（|で囲む）
    title_row = separator.join(f"[Block {i+1}]".center(block_widths[i]) for i in range(len(blocks)))
    title_row = f"| {title_row} |"

    # 本文行も | で囲む
    combined_lines = [title_row]
    for i in range(max_lines):
        line = separator.join(block[i] for block in padded_blocks)
        combined_lines.append(f"| {line} |")

    return "\n".join(combined_lines)

yx_noguide_output = [
    ">ndarray",
    "   ├──── >ndarray ───┬────────────────────┬────────────────────┐",
    "   │              >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐",
    "   │                       255  0   4           255 85   0           255 170  0",
    "   ├──── >ndarray ───┬────────────────────┬────────────────────┐",
    "   │              >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐",
    "   │                       170 255  0           85  255  0            0  255  4",
    "   └──── >ndarray ───┬────────────────────┬────────────────────┐",
    "                  >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐",
    "                            0  170 255           0  85  255           4   0  255"
]

yx_output = [
    ">ndarray    ┊        ┊      ┊   ┊   ┊     ┊      ┊   ┊   ┊     ┊      ┊   ┊   ┊  ",
    "   ├──── >ndarray ───┬────────────────────┬────────────────────┐      ┊   ┊   ┊  ",
    "   │        ┊     >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐  ",
    "   │        ┊        ┊     255  0   4     ┊     255 85   0     ┊     255 170  0  ",
    "   ├──── >ndarray ───┬────────────────────┬────────────────────┐      ┊   ┊   ┊  ",
    "   │        ┊     >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐  ",
    "   │        ┊        ┊     170 255  0     ┊     85  255  0     ┊      0  255  4  ",
    "   └──── >ndarray ───┬────────────────────┬────────────────────┐      ┊   ┊   ┊  ",
    "            ┊     >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐  ",
    "            ┊        ┊      0  170 255    ┊      0  85  255    ┊      4   0  255 "
]

yf_output = [
    ">ndarray    ┊          ┊        ┊   ┊   ┊       ┊        ┊   ┊   ┊       ┊        ┊   ┊   ┊      ",
    "   ├──── >ndarray [ >ndarray [ 255  0   4  ] >ndarray [ 255 85   0  ] >ndarray [ 255 170  0  ] ] ",
    "   ├──── >ndarray [ >ndarray [ 170 255  0  ] >ndarray [ 85  255  0  ] >ndarray [  0  255  4  ] ] ",
    "   └──── >ndarray [ >ndarray [  0  170 255 ] >ndarray [  0  85  255 ] >ndarray [  4   0  255 ] ] ",
]

print(combine_blocks_with_block_titles(yx_noguide_output,yx_output,yf_output, separator="  :  "))