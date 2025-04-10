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
