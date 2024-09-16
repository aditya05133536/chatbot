import os
import json
import streamlit as st
import openai

# configuring the openai api key
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
print(config_data)
# configure the openai api key
OPEN_AI_API_KEY = config_data["OPENAI_API_KEY"]
openai.api_key = OPEN_AI_API_KEY
# configure the streamlit app page
st.set_page_config(
    page_title="Chatgpt-chat",
    page_icon="💬",
    layout="centered"

)
# initialize the chat session in streamlit if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# streamlit title page
st.title("🤖GPT-4o-chatbot")
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
user_prompt = st.chat_input("Ask the question you want!!")

if user_prompt:
    st.chat_message("users").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "you are a helpful assistant"},
            *st.session_state.chat_history

        ]

)
assistant_response = response.choices[0].message.content
st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

# display chat-gpt response
with st.chat_message("assistant"):
    st.markdown(assistant_response)
