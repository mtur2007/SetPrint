# SetPrint 実装項目メモ
---
## ver 0.2.1の新規機能/修正
- `set_list`

   <新規>
   - [完成] プログレスバーや、表示スタイル設定の格納状況の表示のon.offの指定<br>
   
   <修正>
   - [完成]　 表示スタイル設定の格納情報の可読性向上

   [アップデートに向け、デバック中...<br>
   　github内のSetPrintパッケージで ver 0.2.1 の機能を使用する事ができます。 ]
---

## 詳細な変更要素

- ### 表示スタイルの詳細と変更
    #### set_listで表現される特殊な要素をまとめた表<br>
    (記号の部分はデフォルトです)
    
    | スタイル名      | 用途      | タイプ     　| 記号/数値<br>(変更可能) | 説明　            | 指定制限             |
    |:-------------:|:----------|:-----------|:-------------|--------------------------|---------------------|
    | "Collections" | image     | list       | '►list'      | 配列の格納を表す            | type: str           |
    |    ``         | ``        | tuple      | '▷tuple'     | ``                       | type: str,          |
    |    ``         | ``        | ndarray    | '>ndarray'   | ``                       | type: str,          |
    | ------------- | --------  | ---------  | ----------   | ------------------------ | ------------------- |
    | "bracket"     | partially | list       | '{' ・ ")"   | 他の配列と違う次元要素       | type: str, len: 0<l |
    |    ``         | ``        | tuple      | '<' ・ ">'   | ``                       | type: str, len: 0<l |
    |    ``         | ``        | ndarray    | '(' ・ "}'   | ``                       | type: str, len: 0<l |
    |    ``         | ``        | None       | '`' ・ "``"  | 存在しない次元要素　　       | type: str, len: l=1 |
    | ------------- | --------  | ---------  | ----------   | ------------------------ | ------------------- |
    | "padding"     | style     |            | ' '          | 字数の穴埋め               | type: str, len: l=1 |
    | ------------- | --------  | ---------  | ----------   | ------------------------ | ------------------- |
    | "empty"       | style     |            | '-'          | 存在しない要素　　          | type: str, len: l=1 |
    | ------------- | --------  | ---------  | ----------   | ------------------------ | ------------------- |
    | "progress"    | print     |            | True         | プログレスバーの表示　     　| type: bool          |
    | ``            | len       |            | int: 20      | プログレスバーの長さ　     　| type: int, num: 0<n |
    

    **`set_text_style`**

    スタイル変更として'記号'の部分を変更することができます。
    - **実行例**
        ```python
        #list_data = SetPrint(list)
        
        arguments = (
                
            (("Collections" , 
                 { 'image'   : {'list'   :'►list',
                                'tuple'  :'▷tuple',
                                'ndarray':'>numpy'}}),
            ("bracket"     , 
                { 'partially': {'list'   :('{',')'),                 
                                'tuple'  :('<','>'),
                                'ndarray':('(','}'),
                                'None'   :('`','`')}}),
                                                
            ("empty"       , { 'style' : ' '}),
            ("padding"     , { 'style' : '-'}),

            ("progress"    , { 'print' : False ,  # <- New  True(表示)/False(非表示)
                               'len'   : 20}))
            
        )
            
        list_data.set_text_style(arguments) # set_listの前

        # インデックスで引数のチェックを行う為、この配列の通りに指定してください。
        # 制限の範囲内ではなかった値は表示され、デフォルトの値が代入されます。
        
        # set_datas = list_data.set_list(guide=True, keep_start=1, keep_range='all')
        ```
        表示スタイルの表示方法
        ```python
        print(list_data.set_text_style(arguments))
        ^^^^^*-----------------------------------*

        表示内容_terminal

        # style_settings = (

        #    (("Collections" ,
        #      {  'image'   : { 'list'    : '►list' ,
        #                       'tuple'   : '▷tuple' ,
        #                       'ndarray' : '>numpy' ,

        #     ("bracket"     ,
        #      { 'partially': { 'list'    : ( '{' ・ ')' ),
        #                       'tuple'   : ( '<' ・ '>' ),
        #                       'ndarray' : ( '(' ・ '}' ),
        #                       'None'    : ( '`' ・ '`' ),

        #     ("empty"       , { 'style'  : ' ' ),
        #     ("padding"     , { 'style'  : '-' ),

        #     ("progress"    , { 'print'  :  False  ,
        #                        'len'    :  20  }))
        # )

        ```
---
## (ver, 0.3.0) 実装項目メモ

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
    | "progress"    | len       |            | int: 20      | プログレスバーの長さ　     　| type: int, num: 0<n |
    
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

            ("progress"    , {'print':True, 'len'   : 20}))
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
