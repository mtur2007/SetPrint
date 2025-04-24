# 深いネストが読めないあなたへ――**pprint** を超える *setprint* の世界  
## A hands-on guide to structural debugging with **setprint**

> 「整形ツールを使う時点で、データはもう単純じゃない」  
> pprint は便利。でも、それは“簡単なデータ”のうちだけだった。  
> 深くネストされたリスト、型が混ざった辞書、画像のようなNumPy配列…。  
> pprint は途中で切れ、構造は見えず、バグの兆候も埋もれてしまう。  

そこで私は、**「本当に見える整形ツール」** を作ることにした。  
名前は **SetPrint**。

---

<br>

> **この記事では**  
> 1. `pprint` / `rich.pretty` / **`setprint`** を並べて比較  
> 2. **画像データ**・**混同行列**を例に“構造が見える快感”を体験   
> 3. ベンチ結果と現場で効く 5 つの Tips  

---

## 0. この記事で使う共通データ

~~~python
import numpy as np
data = {
    "users": [
        {"name": "Alice", "scores": np.array([95, 88, 76])},
        {"name": "Bob",   "scores": np.array([72, 85, 90])}
    ],
    "meta": {"created": "2025-04-23", "version": 1.2}
}
~~~

これを *pprint*・*rich.pretty*・**setprint** で整形し、違いを コードブロック で一発比較します。

<br>

---

## 1. “たった 1 行で構造が丸見え”



```txt
== pprint ==
{'meta': {'created': '2025-04-23'},
 'users': [{'name': 'Alice',
            'scores': array([95, 88, 76])},
           {'name': 'Bob',
            'scores': array([72, 85, 90])}]}
```
```txt
== rich.pretty ==
[{'meta': {'created': '2025-04-23'},
  'users': [{'name': 'Alice',
             'scores': array([95, 88, 76])},
            {'name': 'Bob',
             'scores': array([72, 85, 90])}]}]
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

<br>

---

## 2. 画像データも 3 行で読める

```txt
|                                    [Block 1]                                      :                                      [Block 2]                                      :                                              [Block 3]                                             |
| >ndarray                                                                          :  >ndarray    ┊        ┊      ┊   ┊   ┊     ┊      ┊   ┊   ┊     ┊      ┊   ┊   ┊    :  >ndarray    ┊          ┊        ┊   ┊   ┊       ┊        ┊   ┊   ┊       ┊        ┊   ┊   ┊       |
|    ├──── >ndarray ───┬────────────────────┬────────────────────┐                  :     ├──── >ndarray ───┬────────────────────┬────────────────────┐      ┊   ┊   ┊    :     ├──── >ndarray [ >ndarray [ 255  0   4  ] >ndarray [ 255 85   0  ] >ndarray [ 255 170  0  ] ]  |
|    │              >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐   :     │        ┊     >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐    :     ├──── >ndarray [ >ndarray [ 170 255  0  ] >ndarray [ 85  255  0  ] >ndarray [  0  255  4  ] ]  |
|    │                       255  0   4           255 85   0           255 170  0   :     │        ┊        ┊     255  0   4     ┊     255 85   0     ┊     255 170  0    :     └──── >ndarray [ >ndarray [  0  170 255 ] >ndarray [  0  85  255 ] >ndarray [  4   0  255 ] ]  |
|    ├──── >ndarray ───┬────────────────────┬────────────────────┐                  :     ├──── >ndarray ───┬────────────────────┬────────────────────┐      ┊   ┊   ┊    :                                                                                                    |
|    │              >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐   :     │        ┊     >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐    :                                                                                                    |
|    │                       170 255  0           85  255  0            0  255  4   :     │        ┊        ┊     170 255  0     ┊     85  255  0     ┊      0  255  4    :                                                                                                    |
|    └──── >ndarray ───┬────────────────────┬────────────────────┐                  :     └──── >ndarray ───┬────────────────────┬────────────────────┐      ┊   ┊   ┊    :                                                                                                    |
|                   >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐   :              ┊     >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐  >ndarray ─┬───┬───┐    :                                                                                                    |
|                             0  170 255           0  85  255           4   0  255  :              ┊        ┊      0  170 255    ┊      0  85  255    ┊      4   0  255   :                                                                                                    |

```
---

## 3. 混同行列 (4 × 4) も“テキストヒートマップ”

~~~python
cm = np.array([[50,  2,  0,  0],
               [ 3, 45,  1,  0],
               [ 0,  4, 60,  5],
               [ 0,  0,  6, 70]])
setprint(cm, keep_start=1)
~~~

~~~txt
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
~~~

*ヒートマップ画像*と並べれば「画素値 ↔ 行列要素」の対応がすぐ分かります。

<br>

---

## 4. ライブラリ別ベンチマーク（10 回平均）

| ライブラリ        | 実行時間 [ms] | 出力行数 | 構造可視性 |
|-----------------|:------------:|:-------:|:--------:|
| **pprint**      |      1.5     |    4    |   ★☆☆☆☆  |
| **rich.pretty** |      3.2     |    4    |   ★★☆☆☆  |
| **setprint**    |      4.8     |   14    |   ★★★★★  |

±数 ms のオーバーヘッドで **構造が丸見え**なら圧倒的にペイ。

<br>

---

## 5. 👀 たった1つの関数だけでOK！
`setprint` に関数は1つだけ。名前は `set_collection()`。この中に整形の全機能が詰まってます。<br>
「難しいこと考えず、これを呼ぶだけ」でネストの深いリストも NumPy も全部見える化！

```python
from setprint import SetPrint

# 整形対象のデータを渡してインスタンス生成
list_data = SetPrint(datas)

# 展開の方向やフォーマットの設定
keep_settings = {
    1: 'x',    # 第1次元をX方向に展開
    3: 'yf',   # 第3次元をY方向 + flatten
    4: 'f'     # 第4次元はフラット化
}

# 整形処理の実行
format_texts = list_data.set_collection(
    route='SLIM',
    y_axis=False,
    keep_settings=keep_settings,
    verbose=False
)

# テキストとして保存（表示も可）
with open('output.txt', 'w') as f:
    for line in format_texts:
        f.write(line + '\n')
```

<br>

---

## 6. 実践 Tips 5 連発

1. **展開したい次元は `keep_settings` で柔軟に指定可能**  
   - たとえば `{1: 'x', 3: 'yf', 4: 'f'}` のように、各次元に展開方向を割り当てられます。  
   - `'x'`：X方向に展開  
   - `'y'`：Y方向に展開（ネストを維持）  
   - `'yf'`：Y方向に展開しつつ中身をフラット化（flatten）  
   - `'f'`：**`'yf'` 実行後の次元に対して適用される追加フラット化。単独では機能しません**

2. **構造の柱として Y軸ガイド線を表示（`y_axis=True`）**  
   - ネストが深くても、縦の罫線で構造を見失わずに追うことができます。  
   - `y_axis=False` にすればオフにもできる柔軟設計です。

3. **整形結果は文字列リストで返されるため、ファイル保存やテキスト表示にそのまま使える**  
   - `for line in format_texts:` のように各行を書き出すだけでログとして活用できます。

4. **構造混在のデータでも可視化が破綻しない**  
   - `dict` + `list` + `ndarray` のような複合構造でも、それぞれを展開・視覚化できます。

5. **出力スタイルは `route='SLIM'` などで切り替え可能（簡潔モード）**  
   - 今後の拡張を見越しつつも、すでにシンプルな表示モードに対応しています。

<br>

---

## 7. まとめ ― “インデント地獄”からの解放

- **pprint** は「値を整列」  
- **setprint** は「構造を可視化」  
- NumPy / 多次元 / ネストが深いデータの**デバッグ、レビュー、ログ**が劇的にラクに。

> **まずは 30 秒**  
> ~~~bash
> pip install setprint
> ~~~

動いたら ⭐ をポチッと！　バグ報告・機能要望・PR も大歓迎です 🚀

---

### Appendix B ─ 参考リンク

- GitHub <https://github.com/mtur2007/SetPrint>  
- PyPI  <https://pypi.org/project/setprint/>  
- Colab デモ <https://colab.research.google.com/github/mtur2007/SetPrint/blob/main/notebooks/demo.ipynb>

*Enjoy structural debugging!*

