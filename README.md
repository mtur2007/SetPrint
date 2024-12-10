# SetPrint(ver, 0.2.0) - Simplify Formatting and Display of High-Dimensional Data!
SetPrint is a Python library designed to easily format and display multi-dimensional data in lists.<br>
Even for data structures with mixed dimensions, you no longer need to manually adjust spaces or formatting. It automatically achieves beautiful formatting!

## Documentation  
- [日本語のドキュメント](https://github.com/mtur2007/SetPrint/blob/main/README_ja.md)

## Features
  - **Support for Flexible Data Structures**: Automatically formats multi-dimensional lists and mixed data structures.
  - **Great for Debugging**: Organizes and displays the structure and contents of data during execution in an easy-to-understand way.
  - **Flexible Formatting**: Visually organizes data hierarchy and content with guided formatting.

### Examples of Literacy Programs
- https://github.com/mtur2007/SetPrint/blob/main/ocr_data.txt
---
### New Features/Fixes in ver 0.2.0
- `set_list`

   <New Features>
   - Simplified progress bar to represent processing status<br>
   - Added keep functionality with argument extensions for automatic list formatting<br>
   - Enhanced customizability of display styles<br>
   - Support for tuple types

- `pick_guideprint`

   <Fixes>
   - Resolved display bugs
---

## Methods
- ## set_list Method

   - The `set_list` method of the SetPrint class provides a feature to easily format and output multi-dimensional lists and complex data structures in a visually comprehensible format.<br>
    Using this method enables optimal formatting tailored to the dimensions of the data.

   - #### Parameters
        - **`guide`** (bool): Enables or disables the guide display.
            - If `True`, outputs a guide containing dimension and index information.

        - **`keep_start`** (int): The dimension where flattening begins.
            - Example: `keep_start=1` expands the first dimension in the Y direction.

        - **`keep_range`** (int): The range of dimensions to flatten.
            - Dimensions outside the specified range are boxed in the X direction.

   - #### Return Values

        - `input_list`       : The original list before formatting.
        - `grid_slice`       : A list containing the formatted text information, with each line stored individually. It can be written directly to a text file to check the results.
        - `grid_block`       : A list maintaining the block-shaped format of the structured data.
        - `block_Xlines_data`: Data used for displaying detailed indices with the `GuidePrint` function.

     ### Relationship Between `keep_start` and Data Formatting
 
     The `keep_start` parameter specifies the dimension where formatting begins and organizes data in the most suitable format based on its structure and use case. Below are examples of how `keep_start` values affect formatting and their corresponding data types.

     #### **Recommended Settings**

    1. **`keep_start=1`**
        - **Use Case**: Data expanding in the Y direction (e.g., logs or image data).
        - **Description**: Formats data along the first dimension in the Y direction while maintaining the X direction as-is.
        - **Example** (Debug Log):
            ```python
            logs = [
                ["Value", 30, "is", "less than", 50],
                [["Action", "Process"], ["Details", "Valid range"]],
                [["Value", 90], ["Condition", ["greater than", 50]], ["Action", "Alert"]],
            ]
            ```
        - **Formatted Result**:
            ```plaintext
            Formatted Log:
            =================================================================================================================================

            |  ►list [ Value   ------ -------      30   --------- -----------   ------------ --        is   ------ -----   less than 50 ]   |
            |  ►list [ ►list { Action Process ) ►list {   Details Valid range   ------------ --   ) -----   ------ -----   --------- -- ]   |
            |  ►list [ ►list {  Value      90 ) ►list { Condition       ►list { greater than 50 ) ) ►list { Action Alert ) --------- -- ]   |

            =================================================================================================================================
            ```
        - **Execution Example**:
            ```python
            from setprint import SetPrint

            # Format and display the data
            list_data = SetPrint(logs)
            set_datas = list_data.set_list(guide=False, keep_start=1, keep_range='all')

            print("\nFormatted Log:")
            for line in set_datas['grid_slice']:
                print(line[:-1])  # Output formatted log
            ```

    2. **`keep_start=2`**
        - **Use Case**: Information divided in the X direction (e.g., tabular data).
        - **Description**: Formats data along the second dimension in the X direction, emphasizing separation in the Y direction.
        - **Example** (Tabular Data):
            ```python
            data = [
                ["Name", "Age", "Country"],
                ["Alice", 30, "USA"],
                ["Bob", 25, "UK"]
            ]
            ```
        - **Formatted Result**:
            ```plaintext
            Formatted Table:
            ====================================
              {} |  {n}                        |
                 |-----------------------------|
                 :                             :
                 |  data_type: <class 'list'>  |
                 |  data_type: <class 'list'>  |
                 |  data_type: <class 'list'>  |

            ====================================
             {0} |  [0]{n}                     |
                 |-----------------------------|
                 :                             :
                 |     Name                    |
                 |      Age                    |
                 |  Country                    |

            ====================================
             {1} |  [1]{n}                     |
                 |-----------------------------|
                 :                             :
                 |  Alice                      |
                 |     30                      |
                 |    USA                      |

            ====================================
             {2} |  [2]{n}                     |
                 |-----------------------------|
                 :                             :
                 |  Bob                        |
                 |   25                        |
                 |   UK                        |

            ====================================
            ```
        - **Execution Example**:
            ```python
            list_data = SetPrint(data)
            set_datas = list_data.set_list(guide=True, keep_start=2, keep_range='all')

            for line in set_datas['grid_slice']:
                print(line[:-1])
            ```

    3. **`keep_start=3`**
        - **Use Case**: Data separated in both Y and X directions (e.g., matrices or 3D arrays).
        - **Description**: Organizes data based on the third dimension, retaining overall structure while arranging information in both Y and X directions.
        - **Example Input Data**:
            ```python
            data = [
                [[1, 2], [3, 4]],
                [[5, 6], [7, 8]]
            ]
            ```
        - **Formatted Result**:
            ```plaintext
            Formatted Matrix:
            ====================================
              {} |  {n}                        |
                 |-----------------------------|
                 :                             :
                 |  data_type: <class 'list'>  |
                 |  data_type: <class 'list'>  |

            ================================================================
             {0} |  [0]{n}                     |  [0][0]{n}  |  [0][1]{n}  |
                 |-----------------------------|-------------|-------------|
                 :                             :             :             :
                 |  data_type: <class 'list'>  |  1          |  3          |
                 |  data_type: <class 'list'>  |  2          |  4          |
   
            ================================================================
             {1} |  [1]{n}                     |  [1][0]{n}  |  [1][1]{n}  |
                 |-----------------------------|-------------|-------------|
                 :                             :             :             :
                 |  data_type: <class 'list'>  |  5          |  7          |
                 |  data_type: <class 'list'>  |  6          |  8          |

            ================================================================
            ```
       
        - **Execution Example**:
            ```python
            list_data = SetPrint(data)
            set_datas = list_data.set_list(guide=False, keep_start=3, keep_range='all')

            print("\nFormatted Log:")
            for line in set_datas['grid_slice']:
                print(line[:-1])  # Output formatted log
            ```

    - ### Detailed Description and Style Modification
        #### Table Summarizing Special Elements Represented in `set_list`<br>
        (Symbols shown are default)

        | Style Name      | Use Case   | Type      | Symbol/Value<br>(Customizable) | Description                                      | Specification Limits     |
        |:---------------:|:-----------|:----------|:-------------------------------|:-------------------------------------------------|:-------------------------|
        | "Collections"   | image      | list      | '►list'                        | Represents stored arrays                         | type: str                |
        |    ``           | ``         | tuple     | '▷tuple'                       | Same as above                                    | type: str                |
        |    ``           | ``         | ndarray   | '>ndarray'                     | Same as above                                    | type: str                |
        | -------------   | --------   | --------  | ----------                     | ------------------------------------------------ | ------------------------ |
        | "bracket"       | partially  | list      | '{' ・ ')'                     | Dimension elements different from other arrays   | type: str, len: 0<l      |
        |    ``           | ``         | tuple     | '<' ・ '>'                     | Same as above                                    | type: str, len: 0<l      |
        |    ``           | ``         | ndarray   | '(' ・ '}'                     | Same as above                                    | type: str, len: 0<l      |
        |    ``           | ``         | None      | '`' ・ "``"                    | Non-existent dimension elements                  | type: str, len: l=1      |
        | -------------   | --------   | --------  | ----------                     | ------------------------------------------------ | ------------------------ |
        | "padding"       | style      |           | ' '                            | Fills gaps in character count                    | type: str, len: l=1      |
        | "empty"         | style      |           | '-'                            | Represents non-existent elements                 | type: str, len: l=1      |
        | -------------   | --------   | --------  | ----------                     | ------------------------------------------------ | ------------------------ |
        | "progress"      | len        |           | int: 20                        | Sets progress bar length                         | type: int, num: 0<n      |

        **`set_text_style`**

        You can customize the 'symbol' part of the styles.
        - **Example Execution**
            ```python
            #list_data = SetPrint(list)

            arguments = (
            
                (("Collections" , 
                  { 'image'    : {'list'   :'►list',
                                  'tuple'  :'▷tuple',
                                  'ndarray':'>numpy'}}),
                ("bracket"     , 
                 { 'partially' : {'list'   :('{',')'),                 
                                  'tuple'  :('<','>'),
                                  'ndarray':('(','}'),
                                  'None'   :('`','`')}}),
                                                    
                ("empty"       , { 'style' : ' '}),
                ("padding"     , { 'style' : '-'}),

                ("progress"    , { 'len'   : 20}))
            )

            list_data.set_text_style(arguments) # Before `set_list`

            # To check arguments by index, specify them in the same order as this array.
            # Values outside the acceptable range will be displayed, and default values will be assigned.

            # set_datas = list_data.set_list(guide=True, keep_start=1, keep_range='all')
            ```


- ## pick_guideprint Method
      
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

- ## bloks_border_print Method

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
                        [ ['block_title','1line','2line'], ['1_2','1_txt','2_txt'] ],                                      # 1step
                        [ ['2_1','1_data','2_data'],       ['2_2','1_line','2_line','3_line'], ['2_3','1_txt','2_txt']],   # 2step
                        [ ['3_1','1_txt','2_txt']]                                                                         # 3step

                    ]

        line_title = ['1step','2step','3step']
    ```
    ```

                A visual representation of the relationship    　　　　  |
                between the output result and `All_blocks`       　　　　|                     Output Result  
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
