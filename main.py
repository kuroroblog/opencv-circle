import cv2
import sys

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# imreadについて : https://kuroro.blog/python/wqh9VIEmRXS4ZAA7C4wd/
# 第一引数 : 画像のファイルパス
# 戻り値 : 行 x 列 x 色の三次元配列(numpy.ndarray)が返される。
img = cv2.imread('./sample.jpg')

# 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
if img is None:
    sys.exit("Could not read the image.")

# circle関数 : 画像内へ円を描画する関数

# 第一引数(必須) : 多次元配列(画像情報)
# 第二引数(必須) : 円の中心座標。tuple型。
# 第三引数(必須) : 円の半径(px)を指定する。int型(0以上の整数のみ指定可能)。
# 第四引数(必須) : 円の色を指定する。B(Blue)G(Green)R(Red)形式で指定する。tuple型。

# thickness : 円の枠線の太さ(px)を指定する。int型。デフォルト(thicknessを指定しない場合)は1が設定される。
# 負の整数(-1, -3など)を与えると、枠線で囲まれる円の、中の塗りつぶしを行います。
cv2.circle(img, (300, 250), 50, (255, 0, 0), thickness=-1)

# imwrite : 画像の保存を行う関数
# 第一引数 : 保存先の画像ファイル名
# 第二引数 : 多次元配列(numpy.ndarray)
# <第二引数の例>
# [
# [
# [234 237 228]
# ...
# [202 209 194]
# ]
# [
# [10 27 16]
# ...
# [36 67 46]
# ]
# [
# [34 51 40]
# ...
# [50 81 60]
# ]
# ]
# imwriteについて : https://kuroro.blog/python/i0tNE1Mp8aEz8Z7n6Ggg/
cv2.imwrite('output.jpg', img)
