# このリポジトリについて

Gemini API の使い方について色々検証するためのリポジトリです。
Gemini API の呼び出し方のサンプルコード、Gemini API の性能検証に利用することを想定しています。

ざっくり触った感想としては

- Gemini API のパッケージを使うと簡単にモデルを呼び出すことができる
- CSV、TXT、PNG、JPG については簡単にマルチーモーダルな回答を得ることができる
- PDF については実際に GCP 上のストレージにアップロードするなどひと手間いりそう

# Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

上記を実行後に`.env`ファイルを作成し、下記の値を設定してください。

```
API_KEY="<APIキー>"
MODEL_ID="gemini-1.5-flash" # 他の値でも大丈夫
```

# Chat 画面を起動する

```
streamlit run app.py
```

# 参考文献

- [Google AI for Developers - Gemini API](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja&lang=python)
  - 基本的な Gemini API の呼び出し方
- [Gemini で PDF ファイルを処理する](https://cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-pdf?hl=ja#generativeaionvertexai_gemini_pdf-python)
  - Gemini に PDF ファイルを渡す方法
