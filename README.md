# 背景削除アプリくん😶‍🌫️

AI（人工知能）を使って画像から背景を自動で削除するWebアプリケーションです。

## 🌟 機能

- **簡単アップロード**: JPG、PNG、JPEG形式の画像をドラッグ&ドロップまたはクリックでアップロード
- **AI背景削除**: 最新のAI技術（rembg）を使用して、自動的に背景を検出・削除
- **リアルタイム処理**: アップロードした画像をその場で処理し、結果をすぐに確認
- **ダウンロード機能**: 背景を削除した画像をPNG形式でダウンロード
- **日本語対応**: 分かりやすい日本語インターフェース

## 🚀 使い方

1. アプリを起動すると、ファイルアップロード画面が表示されます
2. 「背景を消したい画像をアップロードしてください！📂✨」ボタンをクリック
3. JPG、PNG、またはJPEG形式の画像を選択
4. 「背景削除スタート！✨」ボタンをクリック
5. 処理が完了すると、背景が削除された画像が表示されます
6. 「けしけし後の画像をダウンロード！💾」ボタンで結果をダウンロード

## 💻 セットアップ

### 必要な環境
- Python 3.8以上
- pip（パッケージ管理ツール）

### インストール手順

1. リポジトリをクローン:
```bash
git clone https://github.com/e10tech/remove_bg.git
cd remove_bg
```

2. 必要なパッケージをインストール:
```bash
pip install -r requirements.txt
```

3. アプリケーションを起動:
```bash
streamlit run mian.py
```

4. ブラウザで http://localhost:8501 にアクセス

### Dev Container使用の場合

このプロジェクトはDev Containerに対応しています：

1. VS Codeでプロジェクトフォルダを開く
2. Dev Container拡張機能がインストールされていることを確認
3. 「Reopen in Container」を選択
4. 自動的に環境が構築され、Streamlitサーバーが起動します

## 🛠 技術スタック

- **[Streamlit](https://streamlit.io/)**: Webアプリケーションフレームワーク
- **[rembg](https://github.com/danielgatis/rembg)**: AI背景削除ライブラリ
- **[Pillow (PIL)](https://pillow.readthedocs.io/)**: Python画像処理ライブラリ
- **[ONNX Runtime](https://onnxruntime.ai/)**: 機械学習モデル実行エンジン
- **Python**: プログラミング言語

## 📁 ファイル構成

```
remove_bg/
├── README.md           # このファイル
├── mian.py            # メインアプリケーション
├── requirements.txt   # 依存パッケージ一覧
└── .devcontainer/     # Dev Container設定
    └── devcontainer.json
```

## 🎯 対応画像形式

- JPG/JPEG
- PNG

## 📝 注意事項

- 初回実行時、AIモデルのダウンロードが行われるため、時間がかかる場合があります
- 画像サイズが大きい場合、処理に時間がかかることがあります
- インターネット接続が必要です（モデルダウンロード時）

## 🤝 貢献

プルリクエストやイシューの報告を歓迎します！

## 📄 ライセンス

このプロジェクトのライセンスについては、リポジトリの設定をご確認ください。