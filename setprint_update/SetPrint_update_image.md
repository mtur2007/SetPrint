# SetPrint 実装項目メモ

| バージョン | シーケンス型 | マッピング型 | 表示スタイル<br>カスタマイズ | 処理の効率化<br>[ × < △ < ⚪︎] |
|:--------:|:----------:|:----------:|:------------------------:|:----------:|
|   デモ    |     ⚪     |     ×     　|    　  ×                 |      ×     |
|   0.1.0  |     ⚪     |     ×     　|    　  ×                 |      △     |
|   0.2.0  |     ⚪     |     ×     　|    　 ⚪                 |      △     |
|   0.3.0  |     ⚪     |     ⚪      |    　 ⚪                 |      △ 　　|

---
## (ver, 0.3.0) 実装項目メモ

ver, 0,2,0 シーケンス型の実装が容易な状態
ver, 0.3.0 シーケンス型とマッピング型の実装が容易な状態 

- `set_list`

   <新規>
   - [未完成] 数値を値で整える機能の追加
   - [未完成] 辞書型への対応
   
   <修正>
   - [未完成] 表示スタイルのカスタマイズ性の拡張(辞書型項目の追加)<br>
---

# 詳細な変更要素

- ### 表示スタイルの詳細と変更
    #### set_listで表現される特殊な要素をまとめた表<br>
    (記号の部分はデフォルトです)
    
    | スタイル名      | 用途      | タイプ     　| 記号/数値<br>(変更可能) | 説明　            | 指定制限             |
    |:-------------:|:----------|:-----------|:-------------|--------------------------|---------------------|
    | "Collections" | image     | list       | '►list'      | 配列の格納を表す            | type: str           |
    |    ``         | ``        | tuple      | '▷tuple'     | ``                       | type: str,          |
    |    ``         | ``        | ndarray    | '>ndarray'   | ``                       | type: str,          |
    |    ``         | ``        | dictionary | '◆dict'      | ``                       | type: str,          |
    | ------------- | --------  | ---------  | ----------   | ------------------------ | ------------------- |
    | "bracket"     | partially | list       | '{' ・ ")"   | 他の配列と違う次元要素       | type: str, len: 0<l |
    |    ``         | ``        | tuple      | '<' ・ ">'   | ``                       | type: str, len: 0<l |
    |    ``         | ``        | ndarray    | '(' ・ "}'   | ``                       | type: str, len: 0<l |
    |    ``         | ``        | dictionary | '/' ・ "/'   | ``                       | type: str, len: 0<l |
    |    ``         | ``        | None       | '`' ・ "``"  | 存在しない次元要素　　       | type: str, len: l=1 |
    | ------------- | --------  | ---------  | ----------   | ------------------------ | ------------------- |
    | "padding"     | style     |            | ' '          | 字数の穴埋め               | type: str, len: l=1 |
    | ------------- | --------  | ---------  | ----------   | ------------------------ | ------------------- |
    | "empty"       | style     | sequence   | '-'          | 存在しない要素　　          | type: str, len: l=1 |
    |    ``         | ``        | mapping    | '*'          | 存在しない辞書要素(key)　   | type: str, len: l=1 |
    | ------------- | --------  | ---------  | ----------   | ------------------------ | ------------------- |
    | "settings"    | print     |            | True         | スタイル設定値の表示,非表示　 | type: bool          |
    | "progress"    | print     |            | True         | プログレスバーの表示,非表示　 | type: bool          |
    | ``            | len       |            | int: 20      | プログレスバーの長さ　     　| type: int, num: 0<n |
    
    **`set_text_style`**

    スタイル変更として'記号'の部分を変更することができます。
    - **実行例**
        ```python
        #list_data = SetPrint(list)
        
        arguments = (
        
            (("Collections" , 
                { 'image'   : {'list'       :'►list',
                                'tuple'     :'▷tuple',
                                'ndarray'   :'>numpy',
                          New > 'dictionary':'◆dict'}}),
            ("bracket"     , 
                { 'partially': {'list'      :('{',')'),                 
                                'tuple'     :('<','>'),
                                'ndarray'   :('(','}'),
                          New > 'dictionary':('/','/'),
                                'None'      :('`','`')}}),
                                                
            ("empty"       , { 'style' : ' '}),
            ("padding"     , 
                {'sequence': { 'style' : '-'}
           New > 'mapping' : { 'style' : '*'}}),


            ("settings"    , { 'print' : True }),

            ("progress"    , { 'print' : True ,
                               'len'   : 20 }))
        )
        
        list_data.set_text_style(arguments) # set_listの前

        # インデックスで引数のチェックを行う為、この配列の通りに指定してください。
        # 制限の範囲内ではなかった値は表示され、デフォルトの値が代入されます。
        
        # set_datas = list_data.set_list(guide=True, keep_start=1, keep_range='all')
        ```

- ### 辞書型_整形イメージ
    格納例_python
    ```python
    # データの作成
    test_data = (
        [0.0, 0.1, 0.2],
        {zero: 0, one: 1, two: 2},
        {zero: 0, frst: {zero: 0, one: 1}, second:2}
    )

    # インスタンスを生成
    list_data = SetPrint(test_data)

    # データの整形
    set_datas = list_data.set_list(guide=True,keep_start=1,keep_range='all')

    # 表示
    for line in set_datas:
        print(line[-1])
    ```
    整形結果_txtfile
    ```
    =========================================================================
     {} | {n}                                                               |
        |-------------------------------------------------------------------|
        :                                                                   :
        |  ►list [ ****  0.0 ****  0.2   ` -------  ------ ` ******  0.2 ]  |
        |  ◆dict { zero: 0    one: 1     ` -------  ------ `    two: 2   }  |
        |  ◆dict { zero: 0   frst: ◆dict / zero: 0, one: 1 / second: 2   }  |

    =========================================================================
    ```

---