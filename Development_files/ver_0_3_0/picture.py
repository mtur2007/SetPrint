import numpy as np
import matplotlib.pyplot as plt

# --- 1. 3x3の虹色RGB画像配列を作成 ---
cmap = plt.get_cmap('rainbow')
# Matplotlib の "rainbow" カラーマップから9色（RGB）の取得（α成分は除く）
colors = cmap(np.linspace(0, 1, 9))[:, :3]
colors_uint8 = (colors * 255).astype(np.uint8)  # 0〜255の整数に変換

# 3x3の画像配列に各セルへ順番に色を割り当てる
image = np.zeros((3, 3, 3), dtype=np.uint8)
for i in range(3):
    for j in range(3):
        idx = i * 3 + j  # 0～8のインデックス
        image[i, j] = colors_uint8[idx]

# --- 2. BGR形式への変換 ---
# RGBの各セルの色順序を反転させる（BGR形式）
image_bgr = image[..., ::-1]

# --- 3. 白黒の２値化 ---
# まず、標準的な輝度変換（R,G,Bの比率：0.2989, 0.5870, 0.1140）でグレースケール画像を作成
gray_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
# 輝度が128を超えるなら白(255)、それ以外なら黒(0)にする
binary_image = np.where(gray_image > 128, 255, 0).astype(np.uint8)

# --- 出力 ---
print("RGB image (3x3 Rainbow):")
print(image)
print("\nBGR image (3x3 Rainbow):")
print(image_bgr)
print("\nGrayscale image:")
print(gray_image)
print("\nBinary image (thresholded):")
print(binary_image)

# --- 画像の表示 ---
plt.figure(figsize=(12, 3))

plt.subplot(1, 4, 1)
plt.imshow(image)
plt.title("RGB Image")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.imshow(image_bgr)
plt.title("BGR Image")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.imshow(gray_image, cmap='gray', vmin=0, vmax=255)
plt.title("Grayscale")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.imshow(binary_image, cmap='gray', vmin=0, vmax=255)
plt.title("Binary")
plt.axis("off")

plt.tight_layout()
plt.show()

