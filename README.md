# setprint

A module that organizes the contents of a list and visualizes its hierarchical structure.  
リストの中身を整理し、階層構造を可視化するモジュールです。  

## Documentation  
- [日本語のドキュメント](https://github.com/mtur2007/SetPrint/blob/main/README_ja.md)


# Class: SetPrint
 
The class organizes the target list based on its storage location (index) and storage information (string length).<br>
It includes multiple functions that allow you to easily visualize storage information and facilitate access.<br>
<br>
This is particularly useful for debugging list arrays, inspecting storage locations or storage information,<br>
and understanding the structure of the list at a glance by aligning the data for clarity.<br>
<br>
The result is effective when the output font is monospaced and uses half-width characters.

### Class Invocation

`• python`
```python
from setprint import SetPrint
list_data = setprint( ' list' )
set_data = list_data. method
```
## **Methods**

- ## SetPrint.set_list(guide,keep_start,keeplen)

    `set_list` is a function that supports lists of any dimension.

    ### Notes
    When handling horizontally long arrays (X-direction), the execution time may become significantly longer.  
    Additionally, unintended line breaks may occur as a result, so caution is needed when working with horizontally long lists.


    ### Parameters

    The `set_list` function accepts the following parameters:

    - `guide`     : **(Required)** Specifies whether to add indexes to the boxes. Accepts `True` or `False`.
    - `keep_start`: **(Required)** Specifies the dimension from which preservation should start.
    - `keep_len`  : **(Required)** Specifies the range of dimensions to preserve. The end dimension is determined by `keep_start + keep_len`.

    ### Return Value

    `set_list` returns a dictionary containing the following information:

    - `input_list`       : The original unorganized list.
    - `grid_slice`       : A list containing the formatted text information. Each line is stored separately,  
                        allowing it to be directly written to a text file for review.
    - `grid_block`       : A list that maintains the block-like structure of the formatted information.
    - `block_Xlines_data`: Data used by the `GuidePrint` function to display detailed indexes.

    ## Display Method
    - ## Normal Display
        Normally, boxes are generated based on the data stored in the organized list,  
        and the stored values are displayed in a vertically stacked format.
        ### Execution Example
        
        `• python`
        ```python

        # from setprint import SetPrint
        
        '''
        # 1D corresponds to the Y-direction (blocks: rows)
        # 2D and beyond are added in the X-direction for each list array. The order follows the ascending index.
        '''
        test_list =  [
                        ['[0][0]', '[0][1]', '[0][2]', '[0][3]'],
                        ['[1][0]', '[1][1]', ['[1][2][1]', '[1][2][2]'], '[1][3]'],
                        ['[2][0]', '[2][1]', '[2][2]', ['[2][3][1]', ['[2][3][2][1]', '[2][3][2][2]']], '[2][4]', '[2][5]'],
                        ['[3][0]', '[3][1]', '[3][2]', '[3][3]', '[3][4]'],
                        '[4]'
                    ]

        list_data = setprint(test_list)
        answer = list_data.set_list(guide=True, keep_start=False, keeplen=False)

        with open('output_path.txt', 'w') as f:
            for line in set_datas['grid_slice']:
                f.write(line)

        ```

        ### Execution Result
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


    - ## Keep Display

        The `set_list` function has the ability to display arrays stored in n-dimensions within a single box.<br>

        For each array stored in n-dimensions, its contents up to f-dimensions are displayed in a single column, aligned with the indexes of other rows.  

        - Simply put, the n-dimensional array parts are aligned in the order they are retrieved using a for loop (or a recursive function for multi-dimensional cases).  

        If retrieving stored information using for loops or recursive functions is not successful, or if the relationships between the stored information are unclear, this function helps to clarify the structure.


        ### Execution Example  

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

        list_data = setprint(test_list)
        answer = list_data.set_list(guide=True,keep_start=1,keeplen=10) 

        '''
        Currently, there is no functionality in `keep_len` to merge all arrays in the dimension specified by `keep_start` into a single column.  
        To merge everything into a single column, set a large value for `keep_len`.
        '''

        with open('output_path.txt','w') as f:
            for line in set_datas['grid_slice']:
                f.write(line)

        ```
        ### Execution Result  
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
      
    `pick_guideprint` operates as follows:  
    - **Move between blocks**: Use the `f`, `h`, `g`, and `t` keys to navigate between different blocks.  
    - **Move within a block**: Use the `a`, `d`, `s`, and `w` keys to navigate within the current block.  
    - **Directions**:  ← → ↓ ↑  

    **Displayed Information**:  
    - `index`: The index of the currently selected data (e.g., `{y}[x0][x1][x2]`).  
    - `value`: The value stored in the currently selected index. The value is displayed in green, and the data type is displayed in blue.  

    ### Parameters  

    The `pick_guideprint` function accepts the following parameter:  
    - `output_path`: **(Required)** The path to the linked text file.  

    ### Execution Example  
    `• python`
    ```python

    # from setprint import SetPrint
    # list_data = setprint( `list` )
    # list_data.SET_list(guide=True,keep_start=1,keeplen=10)

    list_data.pick_guideprint( 'output_path' )

    ```

    ### Execution Result  
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
    value \ [1][2][0] : str
    ```

- ## SetPrint.bloks_border_print()

    A function that allows you to create boxes, like the output result of `setlist`, and input strings into them.  

    ### Parameters  

    - `All_blocks`: **(Required)** A list array containing the content to be displayed.  
    - `line_title`: **(Required)** The titles of the blocks in the Y-direction.  
    - `guide`    : **(Required)** Specifies whether to include titles. Accepts `True` or `False`.  

    ### Example of `All_blocks` Storage  
    ```python
        '''
        # 1D corresponds to the Y-direction (blocks: rows)
        # 2D corresponds to the X-direction
        # 3D corresponds to the Y-direction (content: rows)
        ! All storage locations must be in the third dimension.
        '''
        
                                            Column 1                        Column 2                        Column 3
        All_blocks = [  
                        1step[ ['block_title','1line','2line'], ['1_2','1_txt','2_txt'] ]
                        2step[ ['2_1','1_data','2_data'],       ['2_2','1_line','2_line','3_line'], ['2_3','1_txt','2_txt']]
                        3step[ ['3_1','1_txt','2_txt']]

                    ]

        line_title = ['1step','2step','3step']
    ```
    ```

                A visual representation of the relationship    　　　　  |
                between the output result and `All_blocks`       　　　　|                       Output Result  
                                                                     　 |
        [                                                            　 |
                                                                     　 |
                         Column 1       Column 2  　   Column 3         |            
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
    ### Return Value  

    - `grid_slice`: A list containing the formatted text information. Each line is stored individually, allowing it to be directly written to a text file for review.  

    ### Execution Example  
    `• python`
    ```python

    # from setprint import SetPrint

    list_data = setprint( `All_blocks` )
    grid_slice = blocks_border_print(line_title = line_title,　guide=True):

    with open('output_path','w') as f:
        for line in grid_slice:
            f.write(line)

    ```
