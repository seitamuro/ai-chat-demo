# Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

上記を実行後に`.env`ファイルを作成し、下記の値を設定してください。

```
API_KEY="<APIキー>"
MODEL_ID="<gemini apiのモデルID>"
```

# Chat 画面を起動する

```
streamlit app.py
```

# 参考文献

[Gemini API Documentation](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja&lang=python)
