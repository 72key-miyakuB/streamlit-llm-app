from dotenv import load_dotenv
import os

load_dotenv()

import streamlit as st

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

st.title("料理に相性の良いお酒をアドバイスしてくれるアプリ")

st.divider()

st.write("##### 1: 入力テキスト")
input_message = st.text_input(label="料理名を入力してください。")

st.write("##### 2: 専門家を選択")
st.write("A:ワインの専門家、B:日本酒の専門家、それぞれの専門家の知識で回答します。")

    # Add a visual divider to separate the input section from the output section
selected_item = st.radio(
    "AとBのどちらの専門家に回答させるかを選択してください。",
    ["A", "B"]
)
st.divider()

if st.button("実行"):
    st.divider()

    if input_message:
        st.write(f"料理名: {input_message}")

    else:
        st.error("料理名を入力してから「実行」ボタンを押してください。")

    if selected_item:
        if selected_item == "A":
            st.write(f"選択された専門家: ワインの専門家")
        else:
            st.write(f"選択された専門家: 日本酒の専門家")
    else:
        st.error("専門家の種類を選択してから「実行」ボタンを押してください。")

if input_message and selected_item:
    if selected_item == "A":
        model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
        llm = ChatOpenAI(model_name=model_name, temperature=0)
        messages = [
            SystemMessage(content=f"(ワインの専門家として{input_message}にあうワインのタイプを回答してください。)"),
            HumanMessage(content=input_message),
        ]
    else:
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
        messages = [
        SystemMessage(content=f"(日本酒の専門家として{input_message}にあう日本酒のタイプを回答してください。)"),
            HumanMessage(content=input_message),
        ]
    result = llm.invoke(messages)
    st.write(result.content)