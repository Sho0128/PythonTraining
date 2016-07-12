#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        mk_geo_matrix_estat002.py
# Purpose:      python勉強会（第1回）
# Description:  変数, リスト, 反復, 条件分岐
#               pythonの基礎の説明のために多少無駄な処理があります
# Author:      Sho0128
#
# Created:     12/07/2016
# Copyright:   (c) Sho0128
#-------------------------------------------------------------------------------

print u"処理はじめ"

# 処理対象のestatのファイル
inputfile = r"data\002.csv"
# 処理後の出力ファイル
outputfile = r"data\output_002.csv"

# ----------------------------------------------------------------------------
# ファイルを開く

# 読み込みモード
inf = open(inputfile, "r")
# 書き込みモード
outf = open(outputfile, "w")
# ----------------------------------------------------------------------------


# フィールド名を書き込み（ \n は改行の意味）
outf.write("KEYCODE,POP,POP_MALE,POP_FEMALE,HH\n")

# 行数をカウントする変数
i = 0

# ファイルを1行ずつ読み込む
for line in inf:
    # カウントが4未満の時はelse以下の処理を飛ばす
    if i < 4:
        pass

    # 地理行列を作る処理
    else:
        # ----------------------------------------------------------------------------
        # 文字列処理

        # 改行とか「-」とか無駄な文字を除去
        stripline = line.strip().replace("-", "").replace('"', '').replace("X", "")
        # カンマで文字列を区切りリスト型のsplitlineに要素を格納
        splitline = stripline.split(",")
        # ----------------------------------------------------------------------------


        # ----------------------------------------------------------------------------
        # フィールドに入れる値を作成

        # 市区町村コード
        citycode = splitline[1]
        # 町字コード
        choazacode = splitline[2]
        # 人口総数
        pop = splitline[11]
        # 男性人口
        pop_male = splitline[12]
        # 女性人口
        pop_female = splitline[13]
        # 世帯数
        household = splitline[14]
        # keycode = citycode + choazacode
        # e.g. 14101050005 = 14101 + 050005
        keycode = citycode + choazacode
        # ----------------------------------------------------------------------------

        # 出力ファイルに書き込み（カンマ区切り）
        # keycode, 人口総数, 男性人口, 女性人口
        outf.write(keycode + "," + pop + "," + pop_male + "," + pop_female + "," + household + "\n")

    # カウントを1増やす
    i += 1

# ファイルを閉じる
inf.close()
outf.close()

print u"処理おわり"