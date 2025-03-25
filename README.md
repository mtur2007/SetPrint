## [ demo ]

---

# SetPrint(ver, 0.3.0) - Easily Format and Display High-Dimensional Data!

## <> A Data Visualization Tool That Properly Formats 2D/NumPy Arrays and Image Data <>

---

*Read this in [English](https://github.com/mtur2007/SetPrint/blob/main/README.md) or [日本語](https://github.com/mtur2007/SetPrint/blob/main/README_ja.md)*

> #### TestPyPI : Testing environment<br>https://test.pypi.org/project/setprint/

---
setprint is a powerful data‑formatting tool that extends Python’s standard pprint, allowing you to properly format not only lists and dictionaries but also NumPy arrays and 2D data (including image data).  
It features enhanced visibility for data with missing elements or mismatched dimensions, making debugging easier.  

> #### Update Information<br>https://github.com/mtur2007/SetPrint/blob/main/Development_files/update_0_3_d/SetPrint_update_image.md

<br>

---

## ✅ Features of `setprint`<br>

 - #### Automatically Adjusts for Missing Elements and Dimension Mismatches

    Formats data to make “storage bugs” and the mixing of different-dimensional data—easily missed by pprint—immediately apparent.<br>
    Automatically fills missing sections with blank spaces so that inconsistencies in your data are instantly recognizable.<br>

<br>

 - #### Maintains and Properly Formats the Intended Structure of `2D Arrays` (e.g., Image or Binary Data)

    Unlike pprint, which struggles with formatting multi‑dimensional data, setprint correctly formats `2D arrays` by leveraging both their vertical and horizontal dimensions for an intuitive, clean display.<br>

    > #### OCR Program Example<br>https://github.com/mtur2007/SetPrint/blob/main/Development_files/format_data/y_x_yf_f.txt  


<br>

 - #### Compact Representation of Array Hierarchies

    Instead of using brackets ([]/()/{}),<br> 
    setprint uses lines (┣ :┃:┗) and (┳ : ━ : ┓) to clearly show parent-child relationships and connections.

    ```txt
    Parent 
      ┣━━━ Sibling
      ┃       ┣━━━ Child
      ┃       ┗━━━ Child
      ┗━━━ Sibling
              ┣━━━ Child
              ┗━━━ Child
    ```

    ```txt
    Parent ━━━┳━━━━━━━━━━━━━┓
           Sibling       Sibling
              ┣━━━ Child    ┣━━ Child
              ┗━━━ Child    ┗━━ Child
    ```
<br>

- [Upcoming Updates]

  > #### Index Display Feature (Planned)<br>Will make it even easier to understand data structure relationships.

  > #### Storage Information Transformation Feature (Value Mapping)<br>Will simplify data transformation processes by allowing mapping of specific values.
<br>

---

## 🛠 Use Cases for `setprint`

🔹 Detecting Storage Bugs in Color Image Data

📌 When Different-Dimensional Data Are Mixed (e.g., RGB Images Mixed with Grayscale Images)

```python
import numpy as np
from setprint import setprint

data = [
    np.random.randint(0, 256, (3, 3, 3)),  # RGB image (3x3x3)
    np.random.randint(0, 256, (3, 3)),     # Grayscale image (3x3) → Different dimension here
    np.random.randint(0, 256, (3, 3, 3)),  # RGB image (3x3x3)
    None                                   # Missing data
]

setprint(data)
```

<br>

🔹 Output of setprint

```txt
keep_settings
['y', 'y', 'x', 'x']
--------------------------------------------------------------------------------------------

►list 
  ┣━━ >nadarray 
  ┃       ┣━━━━ >nadarray ━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
  ┃       ┃               >nadarray ━┳━━━┳━━━┓  >nadarray ━┳━━━┳━━━┓  >nadarray ━┳━━━┳━━━┓
  ┃       ┃                         57  233 198           122 193 78            87  68  15  
  ┃       ┣━━━━ >nadarray ━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
  ┃       ┃               >nadarray ━┳━━━┳━━━┓  >nadarray ━┳━━━┳━━━┓  >nadarray ━┳━━━┳━━━┓
  ┃       ┃                         21  45  99            154 214 132           243 128 56  
  ┃       ┗━━━━ >nadarray ━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
  ┃                       >nadarray ━┳━━━┳━━━┓  >nadarray ━┳━━━┳━━━┓  >nadarray ━┳━━━┳━━━┓
  ┃                                 72  94  45            187 29  67            124 232 190 
  ┣━━ >nadarray 
  ┃       ┣━━━━ >nadarray ━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
  ┃       ┃                  58                    167                   205    
  ┃       ┣━━━━ >nadarray ━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
  ┃       ┃                  134                   77                    49     
  ┃       ┗━━━━ >nadarray ━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
  ┃                          72                    98                    36     
  ┣━━ >nadarray 
  ┃       ┣━━━━ >nadarray ━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
  ┃       ┃               >nadarray ━┳━━━┳━━━┓  >nadarray ━┳━━━┳━━━┓  >nadarray ━┳━━━┳━━━┓
  ┃       ┃                         201 86  52            27  123 111           78  239 194 
  ┃       ┣━━━━ >nadarray ━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
  ┃       ┃               >nadarray ━┳━━━┳━━━┓  >nadarray ━┳━━━┳━━━┓  >nadarray ━┳━━━┳━━━┓
  ┃       ┃                         94  208 193           234 98  72            43  57  65  
  ┃       ┗━━━━ >nadarray ━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
  ┃                       >nadarray ━┳━━━┳━━━┓  >nadarray ━┳━━━┳━━━┓  >nadarray ━┳━━━┳━━━┓
  ┃                                  9  14  186            8  129 244           168 55  210 
  ┗━━   None    

--------------------------------------------------------------------------------------------
```
```
keep_settings
['y', 'yf', 'f', 'f']
------------------------------------------------------------------------------------------------------------

►list 
  ┣━━ >nadarray 
  ┃       ┣━━━━ >nadarray [ >nadarray [ 57  233 198 ] >nadarray [ 122 193 78  ] >nadarray [ 87  68  15  ] ] 
  ┃       ┣━━━━ >nadarray [ >nadarray [ 21  45  99  ] >nadarray [ 154 214 132 ] >nadarray [ 243 128 56  ] ] 
  ┃       ┗━━━━ >nadarray [ >nadarray [ 72  94  45  ] >nadarray [ 187 29  67  ] >nadarray [ 124 232 190 ] ] 
  ┣━━ >nadarray 
  ┃       ┣━━━━ >nadarray [    58                        167                       205                    ] 
  ┃       ┣━━━━ >nadarray [    134                       77                        49                     ] 
  ┃       ┗━━━━ >nadarray [    72                        98                        36                     ] 
  ┣━━ >nadarray 
  ┃       ┣━━━━ >nadarray [ >nadarray [ 201 86  52  ] >nadarray [ 27  123 111 ] >nadarray [ 78  239 194 ] ] 
  ┃       ┣━━━━ >nadarray [ >nadarray [ 94  208 193 ] >nadarray [ 234 98  72  ] >nadarray [ 43  57  65  ] ] 
  ┃       ┗━━━━ >nadarray [ >nadarray [  9  14  186 ] >nadarray [  8  129 244 ] >nadarray [ 168 55  210 ] ] 
  ┗━━   None    

------------------------------------------------------------------------------------------------------------
```

✅ Dimension differences (3D vs 2D) and missing data are visually clear<br>
✅ Easily identify anomalies at a glance, making debugging effortless

<br>

🔹 Output of pprint

```python
[array([[[ 57, 233, 198],
         [122, 193,  78],
         [ 87,  68,  15]],

        [[ 21,  45,  99],
         [154, 214, 132],
         [243, 128,  56]],

        [[ 72,  94,  45],
         [187,  29,  67],
         [124, 232, 190]]]),

 array([[ 58, 167, 205],
        [134,  77,  49],
        [ 72,  98,  36]]),

 array([[[201,  86,  52],
         [ 27, 123, 111],
         [ 78, 239, 194]],

        [[ 94, 208, 193],
         [234,  98,  72],
         [ 43,  57,  65]],

        [[  9,  14, 186],
         [  8, 129, 244],
         [168,  55, 210]]]),

 None]
```
<br>

## Methods

- ## `set_collection` Method

    The SetPrint class’s `set_collection` method provides functionality to neatly align multi-dimensional lists and complex data structures, outputting them in a visually intuitive format.<br>
    By using this method, you can automatically format data optimally according to its dimensions.<br>

   - #### Arguments

        - **`route`** (bool or str): Enable root display.
            - If `True`, lines representing hierarchical relationships are also output.<br>
            - If `maintenance` (str), outputs both enabled and disabled root display for maintenance purposes.

        - **`keep_setting`** { `dict`_type } ( deep/`int` : direction/`str` ): Specify the direction to expand for each dimension.
            - { 1:'y', 3:'x', 4:'yf' } Dimensions should be specified in ascending order; unspecified dimensions inherit their parent dimension’s setting.

              ※ Default setting is `x`

   - #### Returns
        
        - `format_texts`: A list where each element is a line of the formatted text output.

    <br>

   - ### **Example Usage**

        ```python
        from demo_setprint_0_3_0 import SetPrint

        # Specify the array you want to format
        list_data = SetPrint(datas)

        # Specify the directions to expand (explained below)
        keep_settings = {1: 'x', 3: 'yf', 4: 'f'}

        # Execute formatting
        format_texts = list_data.set_collection(route=True, keep_settings=keep_settings)

        # Output results to a text file
        with open('output.txt', 'w') as f:
            for line in format_texts:
                f.write(line + '\n')
        ```
    
    <br><br>

    ---
    ## [] Relationship Between `keep_setting` and Data Alignment

    <br>
    keep_setting allows you to specify the display direction for each dimension, enabling flexible visualization tailored to your data’s structure and purpose.<br>
    Below, we explain how different keep_setting values affect formatting and which data formats they are best suited for.

    <br>

    <br>

    - ## **Recommended Settings Examples**
        
        # 1. **`x`**
        ### **Behavior**: Expands the specified dimension in the `X` direction.

        **Use Cases**:
        - When you want to check dimensional alignment of arrays per dimension element
        - When you want to verify order alignment of parallel elements in the X direction
        - When you want to verify dimensional alignment of parallel elements in the Y direction<br>
        ※ Dimension mismatches are automatically expanded in the Y direction.

        **Effect**: Expanding in the X direction creates parallel arrays along the Y axis.



        <br>
        
        - **Example Arrays**

            ```python 
            test_data = [
                'a','b','c'
            ]
            ```

        - **Formatted Result**

            ```plaintext
            with_route    / out_put
            ============= ~ -------------

             ►list ┳━┳━┓  :  ►list 
                   a b c  :        a b c 

            ============= ~ -------------
            ```

        - **Example Settings**

            ```python
            keep_settings = {1:'x'}
            ```
        <br>
        
        ---
        <br>
        # 2. **`y`**

        ### **Behavior**: Expands the specified dimension in the `Y` direction.

        **Use Cases**: 
        - When you want to verify order alignment of arrays per dimension element

            ---

            > [Not Recommended] Although the following specifications can theoretically be reversed,<br>they are not recommended because they break axis consistency.
            >> - Dimensional elements where you want to verify order alignment of parallel elements in the Y direction.
            >> - Dimensional elements where you want to verify dimensional alignment of parallel elements in the X direction.<br>
                ※ Dimension mismatches are automatically expanded in the X direction.
            ---

        **Effect**: Expanding in the Y direction creates parallel arrays along the X axis.
        
        <br>
        
        - **Example Arrays**
            ```python 
            test_data = [
                'a','b','c'
            ]
            ```

        - **Formatted Result**
            ```plaintext
            with_route  / out_put
            =========== ~ -----------

             ►list      :  ►list 
               ┣━━ a    :        a 
               ┣━━ b    :        b 
               ┗━━ c    :        c 

            =========== ~ -----------
            ```

        - **Example Settings**
            ```python
            keep_settings = {1:'y'}
            ```
        <br>
        
        ---
        <br>

        # 3. **`yf`** ( y_flat )

        ### **Behavior**: Expands the specified dimension in the Y direction, and any subsequent dimensions within its range are added on the same row as expansions in the X direction.

        > #### Optimal setting for compactly aligning array information with dense storage, such as image data.

        <br>

        **Use Cases**: When you want to expand the specified dimension in the Y direction and display it as parallel arrays in the X direction, succinctly summarizing both `order alignment` (missing elements) and `dimension alignment` (dimension mismatches) in a single row.

        <br>
        
        - **Example Arrays**
            ```python
            test_data = [
                [[1,2,3], [4,5,6]],
                [[7,8,9], [10,11,12]]
            ]
            ```

        - **Formatted Result**
            ```plaintext
            with_route                                           / out_put
            ==================================================== ~ ----------------------------------------------------

             ►list                                               :  ►list 
               ┣━━ ►list [ ►list [ 1 2 3 ] ►list [ 4  5  6  ] ]  :        ►list [ ►list [ 1 2 3 ] ►list [ 4  5  6  ] ] 
               ┗━━ ►list [ ►list [ 7 8 9 ] ►list [ 10 11 12 ] ]  :        ►list [ ►list [ 7 8 9 ] ►list [ 10 11 12 ] ] 

            ==================================================== ~ ----------------------------------------------------
            ```

        - **Example Settings**
            ```python
            keep_settings = {1:'yf',2:'f',3:'f'}
            ```

        <br>

    ---

    ## [] Parallel Arrays: Matching Array `Order`/`Dimensions`

    SetPrint includes a feature that, as part of its formatting, automatically fills missing data with blank spaces by comparing parallel elements along each axis, allowing you to instantly spot “storage bugs” and “mixed data with different dimensions” for each structure/object.<br>
    Specifically, this is represented by overlaps along the `X` and `Y` axes.

    - ### Test Array
        ```
        keep_settings
        ['x', 'y', 'x', 'x']
        -----------------------------------------------------------------

           ►list ━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                 ►list                       ►list 
                   ┣━━ ►list ┳━━━┳━━━━━━━┓     ┣━━ ►list ┳━━━┳━━━━━━━┓
                   ┃         0 ►list ┳━┓ 0     ┃         1 ►list ┳━┓ 1 
                   ┃                 0 0       ┃                 1 1 
                   ┗━━ ►list ┳━━━┳━━━━━━━┳━┓   ┗━━ ►list ┳━━━┳━━━━━━━┳━┓
                             0   0       0 0             1   1       1 1 

        -----------------------------------------------------------------
        ```


    - ## X Axis - Matching Array `Order` / Parallel Elements Along the X Axis
        ```
                   .     .   .   .   ⌄ ⌄ . .   .     .   .   .   ⌄ ⌄ . .
                                     ┋ ┋                         ┋ ┋
           ►list ──┬─────────────────┋─┋───────┐                 ┋ ┋
                 ►list               ┋ ┋     ►list               ┋ ┋
                   ├── ►list ┬───┬───┋─┋─┐     ├── ►list ┬───┬───┋─┋─┐
                   │         0 ►list ┬─┐ 0     │         1 ►list ┬─┐ 1 
                   │                 0 0       │                 1 1 
                   └── ►list ┬───┬───┋─┋─┬─┐   └── ►list ┬───┬───┋─┋─┬─┐
                             0   0   ┋ ┋ 0 0             1   1   ┋ ┋ 1 1 
                                     X X                         X X
                                     ^ ^                         ^ ^
        ```
        
        Values stored in the array are displayed horizontally,<br>
        but to maintain consistency with the `order` of parallel arrays expanded in the `Y` direction,<br>
        any unexpected anomalous arrays or partial gaps become easy to spot.

         ※ When using `f`, even if dimensions differ, dimensions within the same range are displayed on a single row, allowing you to detect dimension mismatches.


    - ## Y Axis - Matching Array `Dimensions` / Parallel Elements Along the Y Axis
        ```
           ►list ──┬───────────────────────────┐
        .        ►list                       ►list 
        =          ├── ►list ┬───┬───────┐     ├── ►list ┬───┬───────┐
        .          │         0 ►list ┬─┐ 0     │         1 ►list ┬─┐ 1 
        > ┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉ X ┉┉┉┉┉ 0 0 X ┉┉┉┉┉┉┉┉┉┉┉┉┉ X ┉┉┉┉┉ 1 1 X ┉┉┉ <
        =          └── ►list ┬───┬───────┬─┐   └── ►list ┬───┬───────┬─┐
        .                    0   0       0 0             1   1       1 1 
        ```
        
        Values are displayed vertically according to array dimensions,<br>
        but to maintain consistency with the `dimensions` of parallel arrays expanded in the `X` direction,<br>
        any unexpected anomalous arrays or partial gaps become easy to identify.

        #### ※ When the setting is `y`, the Y axis is interpreted in a parallel sense rather than as a dimension.
        - Note / The Y axis has two meanings:<br>
            - `Dimension mismatch` ( . ): Line breaks in this context occur automatically per dimension.<br>
            - `Parallel elements` ( = ): Line breaks triggered by the settings `'y'` or `'yx'` indicate parallel elements.

    ### ※ When comparing parallel elements, consistency is maintained according to the expansion direction of the nearest parallel element,<br>    so vertical alignment consistency applies only at the level of each parallel element.


    <br><br>

    ---
    ## [] Changing Display Style

    > Currently, only modifications to the array‑style text representation are supported.

    - ###  **Example Usage**

        ```python
        '''
        from demo_setprint_0_3_0 import SetPrint
        
        # Specify the array you want to format
        list_data = SetPrint(datas)
        '''

        #----------------------------------------------------

        style_settings = (

          ("Collections" ,
            {  'image'   : { 'list'    : '►list' ,
                             'tuple'   : '▷tuple' ,
                             'ndarray' : '>nadarray' ,
                             'dict'    : '◆dict' }}),

        )

        list_data.update_data_with_arguments(style_settings)

        #----------------------------------------------------

        """        
        # Specify the directions to expand (explained below)
        keep_settings = {1: 'x', 3: 'yf', 4: 'f'}    
        
        # Execute formatting
        format_texts = list_data.set_collection(route=True, keep_settings=keep_settings)

        # Output results to a text file
        with open('output.txt', 'w') as f:
            for line in format_texts:
                f.write(line + '\n')
        """
        ```