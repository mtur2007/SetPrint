def restore_backticks(text, placeholder):
    """
    プレースホルダーを元の ``` に戻します。
    """
    return text.replace(placeholder, "```")

def process_file(input_file):
    # input_file を読み込む
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 置換結果を元に戻す
    restored_content = restore_backticks(content,"XYZBACKTICKSXYZ")
    print("\n----- Restored Content -----")
    print(restored_content)

if __name__ == "__main__":
    # input.txt というファイルを処理
    process_file("/Users/matsuurakenshin/WorkSpace/development/setprint_package/GPT_honnyaku.txt")
