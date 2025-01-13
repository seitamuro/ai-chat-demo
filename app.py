import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from utils.generate_history import generate_history
import PIL.Image
from audio_recorder_streamlit import audio_recorder

# 環境変数の読み込み
load_dotenv()

API_KEY = os.getenv("API_KEY")
MODEL_ID = os.getenv("MODEL_ID")

# Gemini APIを使うためのセットアップ
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction="日本語で会話を行ってください。")

st.title("Gemini AI Chat Demo")

image_exts = ["png", "jpg", "jpeg"]
text_exts = ["csv", "txt"]
uploaded_file = st.file_uploader("アップロードするファイルを選択してください", type=image_exts + text_exts)


if "messages" not in st.session_state:
  st.session_state.messages = []

# チャットの開始
chat = model.start_chat(history=generate_history(st.session_state.messages))

# 録音ボタンの作成
audio_bytes = audio_recorder()
if st.button("録音を保存"):
  with open("recorded_audio.wav", "wb") as f:
    f.write(audio_bytes)
  st.success("録音が保存されました。")

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

if prompt := st.chat_input("メッセージを入力してください"):
  st.session_state.messages.append({"role": "user", "content": prompt})

  with st.chat_message("user"):
    st.markdown(prompt)
    
  with st.chat_message("assistant"):
    message_placeholder = st.empty()
    full_response = ""

    # アップロードされたファイルの取得
    prompts = [prompt]
    if uploaded_file is not None:
      file_ext = uploaded_file.name.split(".")[-1]
      if file_ext in text_exts:
        prompts.append(uploaded_file.read().decode())
      elif file_ext in image_exts:
        prompts.append(PIL.Image.open(uploaded_file))
      else:
        st.error("対応していないファイル形式です。")
        st.stop()
    
    # ユーザーのメッセージから回答を生成する
    response = chat.send_message(prompts)
    for chunk in response:
      full_response += chunk.text
      message_placeholder.markdown(full_response + "...")
    message_placeholder.markdown(full_response)

  st.session_state.messages.append({"role": "assistant", "content": full_response})
  print(st.session_state.messages)
