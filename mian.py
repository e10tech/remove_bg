#streamlit用のコード
import streamlit as st
from PIL import Image # PillowライブラリからImageを読み込むよ！画像操作に使うんだ～
from rembg import remove # rembgライブラリからremoveっていう機能を借りてくるよ！これが背景消すマン！🦸‍♀️
import io # ioライブラリは、バイトデータを扱うときに使う便利なやつだよ！

# アプリのタイトルを表示するよ！絵文字も使えるの、かわいくない？😍
st.title("背景削除アプリくん😶‍🌫️")

# ファイルアップローダーを設置！これで画像をアップロードできるようになるよ✨
uploaded_file = st.file_uploader("背景を消したい画像をアップロードしてください！📂✨", type=["jpg", "png", "jpeg"])

# もしファイルがアップロードされたら…っていう意味のif文だよ！
if uploaded_file is not None:
    # アップロードされた画像をPillowライブラリのImageを使って開くよ！
    image = Image.open(uploaded_file)

    # st.image() を使うと、Streamlitアプリ上に画像を表示できるよ！
    st.image(image, caption="アップロードされた画像だよ！📸", use_container_width=True) # ← ここが変わったよ！✨

    # 「背景を削除する」ボタンを設置するよ！このボタンが押されたら、背景削除処理が始まるんだ～ワクワク！🥳
    if st.button("背景削除スタート！✨"):
        # st.spinner()を使うと、処理中にくるくるアニメーションが出て、ユーザーに「今がんばってるよ！」って伝えられるの！親切だよね～😉
        with st.spinner("背景をけしけし中…少しまってね！🌀"):
            # uploaded_file.getvalue() で、アップロードされたファイルの中身をバイトデータっていう形式で取り出すよ！
            # rembgのremove関数は、このバイトデータを入力として受け取るんだ！
            input_bytes = uploaded_file.getvalue()

            # いよいよ背景削除！rembgのremove関数にさっきのバイトデータを渡すと、背景が消えた画像のバイトデータが返ってくるよ！魔法みたい！🧙‍♀️
            output_bytes = remove(input_bytes)

            # 背景が消えたバイトデータを、またPillowのImageオブジェクトとして開くよ！
            # io.BytesIO()っていうのは、バイトデータをファイルみたいに扱えるようにするためのものなんだ！便利だね！👍
            processed_image = Image.open(io.BytesIO(output_bytes))

            # 背景を削除した画像を表示するよ！
            st.image(processed_image, caption="背景が消えた画像だよ！やったね！🎉", use_container_width=True) # ← こっちも変わったよ！✨

            st.balloons() # 成功したら風船でお祝い！🎈🎈🎈
            st.success("背景けしけし、かんりょー！✨ ダウンロードもできるよ！👇")

            # 背景を削除した画像をダウンロードできるようにするよ！
            # まずは、PillowのImageオブジェクトをPNG形式のバイトデータに変換するんだ。
            # io.BytesIO()を使って、メモリ上に一時的なファイルみたいなものを作るイメージだよ！
            buf = io.BytesIO()
            processed_image.save(buf, format="PNG")
            byte_im = buf.getvalue()

            # st.download_button() でダウンロードボタンを設置！
            # "label" はボタンに表示される文字
            # "data" はダウンロードさせたいデータ（今回はPNG画像のバイトデータ）
            # "file_name" はダウンロードするときのファイル名
            # "mime" はファイルの種類を指定するところ。PNG画像だから "image/png" だよ！
            st.download_button(
                label="けしけし後の画像をダウンロード！💾",
                data=byte_im,
                file_name="background_removed.png",
                mime="image/png"
            )

else:
    st.write("ここに画像が表示されるよ！わくわく！🥳")
