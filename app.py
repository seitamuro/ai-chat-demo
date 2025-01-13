import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from utils.generate_history import generate_history
import PIL.Image

# 環境変数の読み込み
load_dotenv()

API_KEY = os.getenv("API_KEY")
MODEL_ID = os.getenv("MODEL_ID")

# Gemini APIを使うためのセットアップ
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction="日本語で会話を行ってください。")

st.title("Gemini AI Chat Demo")

uploaded_file = st.file_uploader("アップロードするファイルを選択してください", type=["png", "jpg", "jpeg"])


if "messages" not in st.session_state:
  st.session_state.messages = []

# チャットの開始
chat = model.start_chat(history=generate_history(st.session_state.messages))

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
      image = PIL.Image.open(uploaded_file)
      prompts.append(image)
    
    # ユーザーのメッセージから回答を生成する
    response = chat.send_message(prompts)
    for chunk in response:
      full_response += chunk.text
      message_placeholder.markdown(full_response + "...")
    message_placeholder.markdown(full_response)

  st.session_state.messages.append({"role": "assistant", "content": full_response})
  print(st.session_state.messages)
