## [ demo ]

---

# SetPrint(ver, 0.3.1) - Easily Format and Display High-Dimensional Data!

## <> A Data Visualization Tool That Properly Formats Even 2D/NumPy Arrays and Image Data <>

---

*Read this in [English](https://github.com/mtur2007/SetPrint/blob/main/README.md) or [日本語](https://github.com/mtur2007/SetPrint/blob/main/README_ja.md)*

---

setprint is a powerful data formatting tool that extends Python’s built-in pprint—not only for lists and dictionaries but also for NumPy arrays and 2D data (including image data). It is designed to enhance the visibility of missing data and mismatched dimensions, thereby making debugging much easier.

- ### Installation
    ```python
    pip install setprint
    ```

- ### **Example Execution Template**

    ```python
    from setprint import SetPrint

    # Specify the array you want to format
    #                  　　    ∨
    list_data 　　= SetPrint(datas)
    
    # Specify the expansion direction (detailed explanation follows)
    #                          ∨
    keep_settings = {1:'x', 3:'yf', 4:'f'}

    # Execute the formatting
    format_texts = list_data.set_collection(route=True, keep_settings=keep_settings)

    # Display the result: writing to a text file
    # (The output method is flexible; just be sure to include a newline '\n' at the end!)
    with open('output.txt', 'w') as f:
        for line in format_texts:
            f.write(line + '\n')
    ```

<br>

---

## ✅ Features of `setprint`

 - ### Automatically Adjusts for Missing Data and Dimension Differences

    It formats “storage bugs” and “mixed-dimension data” that are easily overlooked by pprint so that they can be instantly identified.  
    Missing parts are automatically filled with blanks, enabling immediate detection of data inconsistencies.
    
    <br>
    By comparing the expected structure (for example, from a template or sample) with the actual array, you can highlight anomalies and quickly identify bugs or structural discrepancies.
    
<br>

 - ### Debug and Visualize by Structure/Object

    With setprint, debugging and visualization can be performed on a per-structure or per-object basis, resolving issues like uniform formatting or unwanted line breaks.  
    Consequently,  
    **arrays intended to maintain a 2D structure (such as image data or binary data) can be formatted and displayed while preserving their designed layout.**
    
    > #### Example from an OCR Program  
    > https://github.com/mtur2007/SetPrint/blob/main/Development_files/format_data/y_x_yf_f.txt

<br>

 - ### Compact Representation of Containment Relationships

    Instead of representing relationships between parent and child elements with brackets ([]/()/{})<br> the tool uses lines (┣ :┃:┗) and (┳ : ━ : ┓) to clearly depict connections.

    <img src="https://raw.githubusercontent.com/mtur2007/SetPrint/main/Development_files/md_images/root.png" width="310" alt="サンプル画像">

<br>

- [Upcoming Updates]

  > #### An index display feature is planned, which will help further clarify data structure relationships.
  
  > #### A conversion feature for stored data (mapping specific values) is planned to simplify data transformation processes.

<br>

---

## 🛠 Usage Example of `setprint`

🔹 Example of Visualizing Three Different Formats of Image Data

📌 For cases where data with different dimensions coexist (e.g. a mix of RGB and grayscale images)

```python
import numpy as np

data = [
    
    # RGB image (3x3x3) – Sample array 
    np.array([[[255,   0,   4],
               [255,  85,   0],
               [255, 170,   0]],

              [[170, 255,   0],
               [ 85, 255,   0],
               [  0, 255,   4]],

              [[  0, 170, 255],
               [  0,  85, 255],
               [  4,   0, 255]]]),
    
    # Sample array in a different format: BGR image
    np.array([[[  4,   0, 255],
               [  0,  85, 255],
               [  0, 170, 255]],

              [[  0, 255, 170],
               [  0, 255,  85],
               [  4, 255,   0]],

              [[255, 170,   0],
               [255,  85,   0],
               [255,   0,   4]]]),
    
    # Grayscale image (3x3) → This one has a different dimension
    np.array([[ 77, 126, 176],
              [200, 175, 150],
              [129,  79,  29]]),

    None

]

setprint(data)
```

<br>

🔹 Output from setprint

<img src="https://raw.githubusercontent.com/mtur2007/SetPrint/main/Development_files/md_images/y_x.png" width="1000" alt="サンプル画像">

#### Version with Root Omission Settings
<img src="https://raw.githubusercontent.com/mtur2007/SetPrint/main/Development_files/md_images/y_yf.png" width="1000" alt="サンプル画像">

<br>

✅ Differences in dimensions (3D vs 2D) and missing data are clearly visible  
✅ Abnormalities can be immediately identified, making debugging much easier

<br>

---

- ## [] Parallel Arrays: Alignment of Array `Order`/`Dimensions`
    
    In setprint, as part of its formatting process, “storage bugs” and “mixed-dimension data” are represented linearly by duplicating axes to visualize the alignment of array `order` and `dimensions`.

    - ### Test Array

        <img src="https://raw.githubusercontent.com/mtur2007/SetPrint/main/Development_files/md_images/Axis.png" width="600" alt="サンプル画像">

    - ## y-Axis – Alignment of Order with the Parallel Array in the x Direction

        <img src="https://raw.githubusercontent.com/mtur2007/SetPrint/main/Development_files/md_images/Y_Axis.png" width="600" alt="サンプル画像">

        This axis maintains the order alignment with the parallel array expanded in the x direction.

    - ## x-Axis – Alignment of Dimensions with the Parallel Array in the y Direction
        
        <img src="https://raw.githubusercontent.com/mtur2007/SetPrint/main/Development_files/md_images/X_Axis.png" width="600" alt="サンプル画像">
        
        This axis maintains the alignment of dimensions with the parallel array expanded in the y direction.

        ※ With the `f` option, even if dimensions differ, dimensions within the specified range are displayed on one line, making it impossible to detect mismatches in dimensions.

    <br>

    ---

    ### ※ About the Parallel Elements Represented by Both Axes
        
    In setprint, to enable debugging and visualization on a per-structure/object basis, arrays are arranged in parallel along the y and x directions for comparison of array order and dimensions.

    During this process, the meaning of each axis may differ; here are some clarifications:

    - `Parallel Elements` ( = ) 
        
        Portions expanded with the settings `'x'` or `'f'` serve as both order alignment and parallel elements—the interpretation depends on the context.  
        Portions expanded with the settings `'y'` or `'yf'` represent only parallel elements, without implying dimensional alignment.
        
        > Line breaks or representations indicating dimensional alignment are automatically applied when using the `'x'` or `'f'` options.

    ### ※ Consistency is maintained only along the expansion direction and its perpendicular axis; for parallel axes, consistency is maintained on a per-parallel-element basis.

<br>

## Methods

- ## `set_collection` Method

    The SetPrint class’s `set_collection` method is used to execute the formatting as shown in the examples above. It neatly arranges multi-dimensional lists and complex data structures, outputting them in a visually understandable format. This method enables optimal formatting according to the data’s dimensions.
    
   - #### Parameters

        - **`route`** (bool or str): Whether to enable the root display.
            - If set to `True`, lines representing containment relationships will also be output.
              <br>*If set to `maintenance` (str), a maintenance format is used, showing both enabled and disabled root display results simultaneously.*

        - **`keep_setting`** { `dict`_type } ( deep/`int` : direction/`str` ): Specifies the expansion direction for each dimension.
            - For example, { 1: 'y', 3: 'x', 4: 'yf' } specifies dimensions in descending order; dimensions not specified will inherit the parent’s setting.

              ※ The default setting is `x`

   - #### Return Value
        
        - `format_texts`: A list containing the formatted text output for each line.

    <br>

    - ### **Example Execution Template**

        ```python
        from setprint import SetPrint

        # Specify the array you want to format
        #                     　　 ∨
        list_data 　　= SetPrint(datas)
        
        # Specify the expansion direction (detailed explanation follows)
        #                    　　  ∨
        keep_settings = {1:'x', 3:'yf', 4:'f'}

        # Execute the formatting
        format_texts = list_data.set_collection(route=True, keep_settings=keep_settings)

        # Hide the output and write the result to a text file
        with open('output.txt', 'w') as f:
            for line in format_texts:
                f.write(line + '\n')
        ```
    
    <br><br>

    ---
    ## [] Relationship Between keep_setting and Data Alignment

    The `keep_setting` parameter allows you to specify the display direction for each dimension, enabling flexible formatting according to the data’s structure and usage.  
    Below are descriptions of how different `keep_setting` values affect behavior and the data formats they best suit.
    <br>

    <br>

    - ## **Setting Examples**
       
        # 1. **`y`**
        
        ### **Behavior**: Expands the specified dimension in the y direction.

        **Usage**: When you want to verify the order alignment of array elements on a per-dimension basis.

        **Effect**: Expansion in the y direction results in parallel arrays along the x axis.
        
        <br>
        
        - **Array Example**

            ```python 
            test_data = ['a', 'b', 'c']
            ```

        - **Formatted Output**

            <img src="https://raw.githubusercontent.com/mtur2007/SetPrint/main/Development_files/md_images/y.png" width="950" alt="サンプル画像">

        - **Setting Example**
            ```python
            keep_settings = {1: 'y'}
            ```
        <br>
        
        ---

        <br>

        # 2. **`x`**
        ### **Behavior**: Expands the specified dimension in the X direction.

        **Usage**:
        - When you want to verify the dimensional alignment of arrays element by element.
        - When you want to compare the order alignment of arrays (expanded using a `y` setting) with parallel arrays.
        - When you want to compare the dimensional alignment of arrays (expanded using an `x` setting) with parallel arrays.<br>
        ※ Differences in array dimensions are automatically expanded in the y direction.
        
        **Effect**: Expansion in the x direction results in parallel arrays along the y axis.

        <br>
        
        - **Array Example**
            ```python 
            test_data = ['a', 'b', 'c']
            ```

        - **Formatted Output**
            
            <img src="https://raw.githubusercontent.com/mtur2007/SetPrint/main/Development_files/md_images/x.png" width="950" alt="サンプル画像">

        - **Setting Example**
            ```python
            keep_settings = {1: 'x'}
            ```
        <br>
        
        ---
        <br>

        <br>

        # 3. **`yf`** (y_flat)

        ### **Behavior**: Expands the specified dimension in the y direction and displays subsequent dimensions on the same line as an expansion in the x direction.

        > #### Ideal for compactly aligning densely packed array data, such as stored photo data.

        <br>

        **Usage**: Expands the specified dimension in the y direction and presents the subsequent arrays as parallel arrays in the x direction, concisely summarizing both the `order alignment` (for missing data) and the `dimensional alignment` (for mismatched dimensions) in one line.
                
        <br>
        

        - **Array Example**
            ```python
            test_data = [
                [[1, 2, 3], [4, 5, 6]],
                [[7, 8, 9], [10, 11, 12]]
            ]
            ```

        - **Formatted Output**
            
            <img src="https://raw.githubusercontent.com/mtur2007/SetPrint/main/Development_files/md_images/yf.png" width="950" alt="サンプル画像">

        - **Setting Example**
            ```python
            keep_settings = {1: 'yf', 2: 'f', 3: 'f'}
            ```
        <br>

    <br><br>

    ---
    ## [] Changing the Display Style
    
    > Currently, only the text image for array types can be modified.

    - ### **Example Execution Template**

        ```python
        '''
        from demo_setprint_0_3_0 import SetPrint
        
        # Specify the array you want to format
        #                         ∨
        list_data = SetPrint(datas)        
        '''

        #----------------------------------------------------

        style_settings = (
          ("Collections",
            { 'image': {
                'list': '►list',
                'tuple': '▷tuple',
                'ndarray': '>nadarray',
                'dict': '◆dict'
              }
            }
          ),
        )

        list_data.update_data_with_arguments(style_settings)

        #----------------------------------------------------
        """        
        # Specify the expansion direction (detailed explanation follows)
        #                         ∨
        keep_settings = {1: 'x', 3: 'yf', 4: 'f'}

        # Execute the formatting
        format_texts = list_data.set_collection(route=True, keep_settings=keep_settings)

        # Hide the output and write the result to a text file
        with open('output.txt', 'w') as f:
            for line in format_texts:
                f.write(line + '\n')
        """
        ```
