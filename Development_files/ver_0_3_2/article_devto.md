
# Why not pprint anymore?<br>Introducing SetPrint — <br>Structural Debugging for Real Data

> When your data grows beyond a toy example, `pprint` starts to break.  
> You see cut-off arrays. Flattened hierarchies. Lost context.  
> And worst of all? Hidden bugs buried under “pretty” formatting.

That’s why I created **SetPrint** — a Python library that shows **structure, not just values**.

---

## 🔍 What this article covers

- ✅ Side-by-side comparisons: `pprint` / `rich.pretty` / **`setprint`**
- ✅ Real-world examples: **image data**, **confusion matrices**
- ✅ Benchmarks + 5 must-know tips for structured debugging

---

## 🧪 Quick Colab Demo

Want to see it in action? Try this demo notebook — no install needed.
  
🔗 [Try this notebook on Google Colab](https://colab.research.google.com/drive/1Qs3xgB7pWxmOPtsWonyj29r1VMDwo6KF?usp=sharing)

<br>

---

## 1. Visual Comparison — pprint vs rich vs setprint

```python
data = {
    "users": [
        {"name": "Alice", "scores": np.array([95, 88, 76])},
        {"name": "Bob",   "scores": np.array([72, 85, 90])}
    ],
    "meta": {"created": "2025-04-23", "version": 1.2}
}
```

```txt
== pprint ==
{'meta': {'created': '2025-04-23'},
 'users': [{'name': 'Alice',
            'scores': array([95, 88, 76])},
           {'name': 'Bob',
            'scores': array([72, 85, 90])}]}
```

```txt
== setprint ==
keep_settings
['y', 'y', 'y', 'y']
--------------------------------------------------------

◆dict 
  ├── users:►list 
  │        ├───── -------.  ◆dict    
  │        │              ├─────────  name : Alice   
  │        │              └───────── scores:>ndarray 
  │        │                                ├─────── 95 
  │        │                                ├─────── 88 
  │        │                                └─────── 76 
  │        └───── -------.  ◆dict    
  │                       ├─────────  name :  Bob    
  │                       └───────── scores:>ndarray 
  │                                         ├─────── 72 
  │                                         ├─────── 85 
  │                                         └─────── 90 
  └── meta :◆dict 
           ├───── created:2025-04-23 
           └───── version:   1.2     

--------------------------------------------------------
```


Even at a glance, the structure is crystal clear.

<br>

---

## 2. Image Arrays? No Problem

```python
rgb = np.random.randint(0, 255, size=(3, 3, 3))
set_collection ( route='SLIM', y_axis=False, keep_settings={1: 'yf', 2: 'f'} )
```
```txt
keep_settings
['yf', 'f', 'f']
-------------------------------------------------------------------------------------------------

>ndarray 
   ├──── >ndarray [ >ndarray [ 255  0   4  ] >ndarray [ 255 85   0  ] >ndarray [ 255 170  0  ] ] 
   ├──── >ndarray [ >ndarray [ 170 255  0  ] >ndarray [ 85  255  0  ] >ndarray [  0  255  4  ] ] 
   └──── >ndarray [ >ndarray [  0  170 255 ] >ndarray [  0  85  255 ] >ndarray [  4   0  255 ] ] 

-------------------------------------------------------------------------------------------------
```

You don’t just see the values—you see the **hierarchy**.

<br>

---

## 3. Confusion Matrices as Text-Based Heatmaps

```python
cm = np.array([[50, 2, 0, 0], [3, 45, 1, 0], [0, 4, 60, 5], [0, 0, 6, 70]])
set_collection ( route='SLIM', y_axis=False, keep_settings={1:'y', 2:'x'} )
```
```txt
keep_settings
['y', 'x']
------------------------------

>ndarray 
   ├──── >ndarray ┬──┬──┬──┐
   │              50 2  0  0  
   ├──── >ndarray ┬──┬──┬──┐
   │              3  45 1  0  
   ├──── >ndarray ┬──┬──┬──┐
   │              0  4  60 5  
   └──── >ndarray ┬──┬──┬──┐
                  0  0  6  70 

------------------------------
```

<br>

---

## 4. Benchmark: Visibility vs Speed

| Library         | Runtime (ms) | Lines | Structure Clarity |
|-----------------|:------------:|:-----:|:------------------:|
| `pprint`        |      1.5     |   4   |       ★☆☆☆☆        |
| `rich.pretty`   |      3.2     |   4   |       ★★☆☆☆        |
| `setprint`      |      4.8     |  14   |       ★★★★★        |

A few ms extra for full visibility? Totally worth it.

<br>

---

## 5. 5 Must-Know Tips for Using SetPrint

1. Use `keep_settings = {1: 'x', 3: 'yf', 4: 'f'}` for full control over dimensions  
2. Show vertical guides with `y_axis=True`  
3. Output is a list of lines → easy to write to file  
4. Handles mixed types: `dict` + `list` + `ndarray`? No problem  
5. Switch between styles like `'SLIM'`, `'BOLD'`, or even `'HALF'`

<br>

---

## 6. One Function, Infinite Views

```python
from setprint import SetPrint
list_data = SetPrint(data)

formatted = list_data.set_collection(
    keep_settings={1:'x', 2:'yf', 3:'f'},
    route='SLIM', y_axis=True
)

for line in formatted:
    print(line)
```

<br>

---

## 🚀 Try it Now

```bash
pip install setprint
```

<br>

🎯 If you found it useful, please consider giving a ⭐ on GitHub!
🐛 Bug reports, 💡 feature requests, and 📬 pull requests are all welcome!

📎 GitHub: [mtur2007/SetPrint](https://github.com/mtur2007/SetPrint)  
📘 PyPI: [setprint](https://pypi.org/project/setprint/)  
🔍 Colab Demo: [Try on Colab](https://colab.research.google.com/drive/1Qs3xgB7pWxmOPtsWonyj29r1VMDwo6KF?usp=sharing)

---

*If you’ve ever said “I just want to see the damn structure” — SetPrint is for you.*
