
# クラス: SetPrint
 
対象のリストを格納場所(インデックス)と格納情報(文字列の長さ)で整え、<br>
格納情報を見やすく表示し、アクセスを容易にするための関数が複数定義されているクラスになります。<br>
リスト配列のデバックなどで、格納場所や格納情報の点検、リストの構造を把握する場合に、一目で理解できるように整列させている為、便利です。<br>
結果出力先のフォントが、等幅フォント・半角文字の場合にて有効です。
### クラス呼び出し
`• python`
```python
from setprint import SetPrint
list_data = SetPrint( ' list' )
set_data = list_data. method
```
## **メソッド**

- ## SetPrint.set_list(guide,keep_start,keeplen)

    `set_list` は、あらゆる次元のリストに対応した関数です。

    ### 注意点 
    配列が横に長い（X方向）場合、実行時間が非常に長くなります。また、その結果として意図しない自動改行が入ることもあるため、<br>X方向に長いリストを扱う際には注意が必要です。

    ### 引数

    `set_list` 関数には以下の引数を指定できます：

    - `guide`     : **(必須)** ボックスにインデックスを追加するかどうかを指定します。`True` または `False` を指定します。
    - `keep_start`: **(必須)** どの次元から維持を開始するかを指定します。
    - `keep_len`  : **(必須)** 維持する次元の範囲を指定します。終了する次元は `keep_start + keep_len` で決まります。

    ### 戻り値

    `set_list` は以下の情報を含む辞書型データを返します：

    - `input_list`       : 整列元のリスト。
    - `grid_slice`       : 整列後のテキスト情報が格納されたリスト。各行毎に格納されており、そのままテキストファイルなどに書き込むことで結果を確認できます。
    - `grid_block`       : ブロック状の形状を維持したまま整列情報が格納されているリスト。
    - `block_Xlines_data`: `GuidePrint` 関数で詳細なインデックスを表示する際に使用するデータ。


    ## 表示方法
    - ## 通常表示
        通常、整列対象のリストに格納されているデータに基づいて、リスト配列分のボックスが生成され、格納されている値が縦に積み重なった形で表示されます。
        ### 実行例
        
        `• python`
        ```python

        # from setprint import SetPrint
        
        '''
        # 1次元は、Y方向(ブロック:段)
        # 2次元以降は、リスト配列毎にX方向へ追加される。順番はインデックスの昇降順
        '''
        test_list =  [
                        ['[0][0]','[0][1]','[0][2]','[0][3]'],
                        ['[1][0]','[1][1]',['[1][2][1]','[1][2][2]'],'[1][3]'],
                        ['[2][0]','[2][1]','[2][2]',['[2][3][1]',['[2][3][2][1]','[2][3][2][2]']],'[2][4]','[2][5]'],
                        ['[3][0]','[3][1]','[3][2]','[3][3]','[3][4]'],
                        '[4]'
                    ]

        list_data = SetPrint(test_list)
        set_datas = list_data.set_list(guide=True,keep_start=False,keeplen=False)

        with open('output_path.txt','w') as f:
            for line in set_datas['grid_slice']:
                f.write(line)

        ```
        ### 実行結果
        `• output_path.txt`
        ```
        ===================================
            |  {n}                        |
            |-----------------------------|
            :                             :
            |  data_type: <class 'list'>  |
            |  data_type: <class 'list'>  |
            |  data_type: <class 'list'>  |
            |  data_type: <class 'list'>  |
            |  [4]                        |

        ===================================
         {0}|  [0]{n}                     |
            |-----------------------------|
            :                             :
            |  [0][0]                     |
            |  [0][1]                     |
            |  [0][2]                     |
            |  [0][3]                     |

        =================================================================
         {1}|  [1]{n}                     |  [1][2]{n}                  |
            |-----------------------------|-----------------------------|
            :                             :                             :
            |  [1][0]                     |  [1][2][0]                  |
            |  [1][1]                     |  [1][2][1]                  |
            |  data_type: <class 'list'>  |                             |
            |  [1][3]                     |                             |

        ==================================================================================
         {2}|  [2]{n}                     |  [2][3]{n}                  |  [2][3][1]{n}  |
            |-----------------------------|-----------------------------|----------------|
            :                             :                             :                :
            |  [2][0]                     |  [2][3][0]                  |  [2][3][1][0]  |
            |  [2][1]                     |  data_type: <class 'list'>  |  [2][3][1][1]  |
            |  [2][2]                     |                             |                |
            |  data_type: <class 'list'>  |                             |                |
            |  [2][4]                     |                             |                |
            |  [2][5]                     |                             |                |

        ==================================================================================
         {3}|  [3]{n}                     |
            |-----------------------------|
            :                             :
            |  [3][0]                     |
            |  [3][1]                     |
            |  [3][2]                     |
            |  [3][3]                     |
            |  [3][4]                     |

        ===================================
        ```


    - ## キープ表示

        `set_list` には、n次元に格納されている配列を1つのボックスで表示する機能があります。<br>
        n次元に格納されている配列ごとに、f次元までの中身が1列で表示され、他の行のインデックスに合わせる形で      整列されます。<br>
        - 簡単に説明すると、n次元の配列部分を for構文(多次元の場合は再帰関数) を使って取得できる順に整列されます。<br>
        for構文や再帰関数を使った格納情報の取得が上手くいかなかったり、<br>
        格納情報同士の関係性が不透明だった場合に、よりはっきりさせる事ができます。
        

        ### 実行例
        `• python`
        ```python

        # from setprint import SetPrint

        test_list =  [
                        ['[0][0]','[0][1]','[0][2]','[0][3]'],
                        ['[1][0]','[1][1]',['[1][2][1]','[1][2][2]'],'[1][3]'],
                        ['[2][0]','[2][1]','[2][2]',['[2][3][1]',['[2][3][2][1]','[2][3][2][2]']],'[2][4]','[2][5]'],
                        ['[3][0]','[3][1]','[3][2]','[3][3]','[3][4]'],
                        '[4]'
                    ]

        list_data = SetPrint(test_list)
        set_datas = list_data.set_list(guide=True,keep_start=1,keeplen=10) 
        '''
        現在はkeep_lenに、keep_startの次元に格納されている配列をすべて1列にする機能はないので、すべて一列にする場合はkeep_lenに大きな数を入れてください。
        '''

        with open('output_path.txt','w') as f:
            for line in set_datas['grid_slice']:
                f.write(line)

        ```
        ### 実行結果
        `• output_path.txt`
        ```
        ========================================================================================================================================
            |  {n}                                                                                                                             |
            |----------------------------------------------------------------------------------------------------------------------------------|
            :                                                                                                                                  :
            |  ►list { [0][0] [0][1] [0][2]   --------- ---------   [0][3]   --------- -----   ------------ ------------     ------ ------ )   |
            |  ►list { [1][0] [1][1]  ►list { [1][2][0] [1][2][1] ) [1][3]   --------- -----   ------------ ------------     ------ ------ )   |
            |  ►list { [2][0] [2][1] [2][2]   --------- ---------    ►list { [2][3][0] ►list { [2][3][1][0] [2][3][1][1] ) ) [2][4] [2][5] )   |
            |  ►list { [3][0] [3][1] [3][2]   --------- ---------   [3][3]   --------- -----   ------------ ------------     [3][4] ------ )   |
            |    [4]   ------ ------ ------   --------- ---------   ------   --------- -----   ------------ ------------     ------ ------     |

        =======================================================================================================================================
        ```



- ## SetPrint.pick_guideprint(output_path)

    `pick_guideprint` は以下のように動作します：
    - **ブロック間の移動**: `f`, `h`, `g`, `t` キーを使用して、異なるブロック間を移動します。
    - **ブロック内の移動**: `a`, `d`, `s`, `w` キーを使用して、現在のブロック内を移動します。
    - **方向**:  ←    →    ↓    ↑  

    **表示される情報**:
    - `index`: 現在選択されているデータのインデックス（例: `{y}[x0][x1][x2]`）。
    - `value`: 現在選択されているインデックスに格納されているデータの値。データの値は緑色で表示され、データ型は青色で表示されます。
    ### 引数

    `pick_guideprint` には以下の引数を指定します：

    - `output_path`  : **(必須)** 連動先のテキストファイルのパス。

    ### 実行例
    `• python`
    ```python

    # from setprint import SetPrint
    # list_data = SetPrint(test_list)
    # list_data.set_list(guide=True,keep_start=1,keeplen=10)

    list_data.pick_guideprint(output_path)


    ```

    ### 実行結果 
    `• txt_file`
    ```
        ►list { [0][0] [0][1] [0][2]    ---------  ---------   [0][3]   --------- -----   ------------ ------------     ------ ------ ) 
       ------------------------------- ┏         ┓ -------------------------------------------------------------------------------------
        ►list { [1][0] [1][1]  ►list {  [1][2][0]  [1][2][1] ) [1][3]   --------- -----   ------------ ------------     ------ ------ ) 
       ------------------------------- ┗         ┛ -------------------------------------------------------------------------------------
        ►list { [2][0] [2][1] [2][2]    ---------  ---------    ►list { [2][3][0] ►list { [2][3][1][0] [2][3][1][1] ) ) [2][4] [2][5] ) 
        ►list { [3][0] [3][1] [3][2]    ---------  ---------   [3][3]   --------- -----   ------------ ------------     [3][4] ------ ) 
          [4]   ------ ------ ------    ---------  ---------   ------   --------- -----   ------------ ------------     ------ ------   
    ```
    `• terminal`
    ```
    index \ {1}[2][0]
    value \ [1][2][1] : str
    ```

- ## SetPrint.bloks_border_print()

    `setlist`の出力結果のような、ボックスを生成し、文字列を記入できる機能を、利用できる関数。

    ### 引数

    - `All_blocks`: **(必須)** 表示したい内容を格納したリスト配列。
    - `line_tilte`: **(必須)** y方向のブロックのタイトル
    - `guide`     : **(必須)** タイトル表記の有無。`True` または `False` を指定します。


    ### `All_blocks` 格納例
    ```python
        '''
        # 1次元は、Y方向(ブロック:段)
        # 2次元は、X方向
        # 3次元は、Y方向(内容:行)
        ! 格納場所はすべて ３次元目 である必要があります
        '''
        
                                            1列目                            2列目                            3列目
        All_blocks = [ 
                        [ ['block_title','1line','2line'], ['1_2','1_txt','2_txt'] ],                                      #1step
                        [ ['2_1','1_data','2_data'],       ['2_2','1_line','2_line','3_line'], ['2_3','1_txt','2_txt'] ],  #2step
                        [ ['3_1','1_txt','2_txt'] ]                                                                        #3step

                    ]

        line_title = ['1step','2step','3step']
    ```
    ```
        
            出力結果とAll_blocksの関係性を視覚的に表したもの                  |　　　　　　　　            出力結果
                                                                     　 |
        [                                                            　 |
                                                                     　 |
                           1列目          2列目                          |            
           ========================================                   　|      =====================================
            _____ [ ｜["block_title",｜["1_2",     ｜           　       |       {1step} |  block_title  |  1_2     |
                    ｜---------------｜------------｜           　       |               |---------------|----------|
                    ：               ：            ：           　       |               :               :          :
                    ｜ '1line',      ｜ '1_txt',   ｜           　       |               |  1line        |  1_txt   |
                    ｜ '2line' ],    ｜ '2_txt' ], ｜ ],         　      |               |  2line        |  2_txt   |
                                                                     　 |
           =====================================================      　|      ===============================================
            _____ [ ｜["2-1",        ｜["2-2",     ｜["2_3",    ｜       |       {2step} |  2_1          |  2_2     |  2_3    |
                    ｜---------------｜------------｜-----------｜       |               |---------------|----------|---------|
                    ：               ：            ：           ：       |               :               :          :         :
                    ｜ '1_data',     ｜ '1_line',  ｜ '1_txt',  ｜       |               |  1_data       |  1_line  |  1_txt  |
                    ｜ '2_data' ],   ｜ '2_line',  ｜ '2_txt' ],｜       |               |  2_data       |  2_line  |  2_txt  |
                    ｜               ｜ '3_line' ],｜           ｜ ],    |               |               |  3_line  |         |
                                                                     　 |
           =====================================================      　|      ===============================================
            _____ [ ｜["3-1",        ｜            　           　       |       {3step} |  3_1          |
                    ｜---------------｜            　           　       |               |---------------|
                    ：               ：            　           　       |               :               :
                    ｜ '1_txt',      ｜            　           　       |               |  1_txt        |
                    ｜ '2_txt' ],    ｜ ]          　           　       |               |  2_txt        |
                    　            　               　           　       |
           ===========================                                　|      ==========================
        ]  
    ```

    ### 戻り値

    - `grid_slice`: 整列後のテキスト情報が格納されたリスト。各行毎に格納されており、そのままテキストファイルなどに書き込むことで結果を確認できます。

    ### 実行例
    `• python`
    ```python

    #from setprint import SetPrint

    list_data = SetPrint( `All_blocks` )
    grid_slice = list_data.blocks_border_print(line_title =  `line_title` , guide=True):

    with open('output_path','w') as f:
        for line in grid_slice:
            f.write(line)

    ```