# 必要なライブラリをインポート
import streamlit as st
import numpy as np
import pandas as pd

# タイトルとテキストを記入
st.title('Streamlit 基礎')
st.write('Hello World!')

# データフレームの準備
df = pd.DataFrame({
    '1列目' : [1, 2, 3, 4],
    '2列名' : [10, 20, 30, 40]
})

# 動的なテーブル
st.dataframe(df)

# 引数を使用した動的テーブル
st.dataframe(df.style.highlight_max(axis = 0) , width = 100 , height = 150)

# 静的なテーブル
st.table(df)

# 10行3列のデータフレームを準備
df = pd.DataFrame(
    np.random.rand(10,3),
    columns = ['a', 'b', 'c']
)

# 折れ線グラフ
st.line_chart(df)

# 面グラフ
st.area_chart(df)

# 棒グラフ
st.bar_chart(df)

# プロットする乱数をデータフレームで用意
df = pd.DataFrame(

    # 乱数 + 新宿の緯度と経度
    np.random.rand(100,2) / [50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)

# マップをプロット
st.map(df)

# Pillowをインポート
from PIL import Image

# 画像の読み込み
# パスをコピーするとエラーになった。
# PillowのImageメソッドを代入して、それをstreamlitに埋め込んでいる。
img = Image.open('Iris.jpg')
# captionで設定したのは画像のタイトル
# use_column_width=Trueでアプリのレイアウトに合わせて自動調整
st.image(img, caption = 'Iris', use_column_width = True)

# チェックボックス
if st.checkbox('Show Image'):
    img = Image.open('Iris.jpg')
    st.image(img, caption = 'Iris', use_column_width = True)

# セレクトボックス
option = st.selectbox(
    '好きな数字を入力してください。',
    list(range(1,11))
)

'あなたの好きな数字は', option, 'です。'

# テキスト入力による値の動的変更
text = st.text_input('あなたの好きなスポーツを教えてください。')

'あなたの好きなスポーツ: ', text

# スライダーによる値の動的変更
condition = st.slider('あなたの今の調子は?', 0, 100, 50)

'コンディション: ', condition

# テキスト入力による値の動的変更
text = st.sidebar.text_input('あなたの好きなスポーツを教えて下さい。')
'あなたの好きなスポーツ：' , text

# スライダーによる値の動的変更
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：' , condition

# expander
expander1 = st.expander('質問1')
expander1.write('質問1の回答')
expander2 = st.expander('質問2')
expander2.write('質問2の回答')
expander3 = st.expander('質問3')
expander3.write('質問3の回答')

# プログレスバーの表示
import time

latest_iteration = st.empty()
bar = st.progress(0)

# プログレスバーを0.1秒ごとに進める
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done'

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

import pydeck as pdk

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))
