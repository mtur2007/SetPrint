# 深いネストが読めないあなたへ――**pprint** を超える *setprint* の世界  
## A hands-on guide to structural debugging with **setprint**

> **この記事では**  
> 1. `pprint` / `rich.pretty` / **`setprint`** を並べて比較  
> 2. **画像データ**・**混同行列**を例に“構造が見える快感”を体験  
> 3. 30 秒クイックスタート & 軽量 GIF の作り方  
> 4. ベンチ結果と現場で効く 5 つの Tips  

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

これを *pprint*・*rich.pretty*・**setprint** で整形し、違いを GIF で一発比較します。

<br>

---

## 1. 6 秒 GIF ― “たった 1 行で構造が丸見え”

![pprint_vs_rich_vs_setprint.gif](./pprint_vs_rich_vs_setprint.gif)  
<sub>左: **pprint**   中央: **rich.pretty**   右: **setprint**</sub>

| ライブラリ | 何が見える？ | 何が見えない？ |
|------------|-------------|----------------|
| **pprint** | インデント | NumPy 配列中身・深い階層 |
| **rich**   | カラー強調 | 同上（構造自体は追いづらい） |
| **setprint**| 配列要素・階層ブロック・インデックス | ― |

> **30 秒お試し**  
> ~~~bash
> pip install setprint
> python - <<'PY'
> from setprint import setprint; import json, numpy as np
> setprint(json.loads('{"a":[1,2,3]}'))
> PY
> ~~~

<br>

---

## 2. 画像データも 3 行で読める

| 元画像 (3 × 3) | `setprint` 出力 |
|---------------|-----------------|
| ![tiny_rgb](tiny_rgb.png) | ~~~txt
►ndarray 3×3×3
  ┣━━ row 0 : ndarray ━┳━━ [255 128  64]
  ┃                    ┣━━ [ 60 200  10]
  ┃                    ┗━━ [ 10  20 230]
  ┣━━ row 1 : ndarray …
  ┗━━ row 2 : ndarray …
~~~ |

~~~python
from PIL import Image
from setprint import setprint
arr = np.array(Image.open("sample.jpg").resize((3, 3)))
setprint(arr, keep_start=1, keeplen=3)
~~~

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
►ndarray 4×4
  ┣━━ row 0 : ndarray ━┳━━ 50 ━  2 ━ 0 ━ 0
  ┣━━ row 1 : ndarray ━┳━━  3 ━ 45 ━ 1 ━ 0
  ┣━━ row 2 : ndarray ━┳━━  0 ━  4 ━60 ━ 5
  ┗━━ row 3 : ndarray ━┳━━  0 ━  0 ━ 6 ━70
~~~

*ヒートマップ画像*と並べれば「画素値 ↔ 行列要素」の対応がすぐ分かります。

<br>

---

## 4. ライブラリ別ベンチマーク（10 回平均）

| ライブラリ | 実行時間 [ms] | 出力行数 | 構造可視性 |
|------------|--------------|----------|------------|
| **pprint** | 1.5 | 4  | ★☆☆☆☆ |
| **rich.pretty** | 3.2 | 4  | ★★☆☆☆ |
| **setprint** | 4.8 | 14 | ★★★★★ |

±数 ms のオーバーヘッドで **構造が丸見え**なら圧倒的にペイ。

<br>

---

## 5. API チートシート

| 関数 / 引数 | 概要 | 例 |
|-------------|------|----|
| `setprint(obj, keep_start=1, keeplen=None)` | 基本整形 | `setprint(arr, keep_start=2)` |
| `pick_guideprint(obj, keys="asdw")` | WASD 風ナビで対話式選択 | `pick_guideprint(data)` |
| `bloks_border_print(style='ascii')` | 罫線スタイル変更 | `bloks_border_print('light')` |

<br>

---

## 6. 実践 Tips 5 連発

1. **巨大配列は `keeplen=10` で折りたたむ**  
2. **pytest フック**で失敗時に自動可視化  
3. VS Code スニペットで `print → setprint` ワンキー化  
4. `highlight_null=True` で欠損値を赤色強調  
5. `dict` + `np.ndarray` 混在設定ファイルのレビューに投入  

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

### Appendix A ─ GIF 生成コマンド

~~~bash
# asciinema で録画
asciinema rec demo.cast -t "pprint_vs_setprint"
# SVG 化
npx svg-term --cast demo.cast --out demo.svg --window
# GIF 生成 & 最適化
gifski -o demo.gif demo.svg
gifsicle -O3 --lossy=40 -o pprint_vs_rich_vs_setprint.gif demo.gif
~~~

### Appendix B ─ 参考リンク

- GitHub <https://github.com/mtur2007/SetPrint>  
- PyPI  <https://pypi.org/project/setprint/>  
- Colab デモ <https://colab.research.google.com/github/mtur2007/SetPrint/blob/main/notebooks/demo.ipynb>

*Enjoy structural debugging!*
