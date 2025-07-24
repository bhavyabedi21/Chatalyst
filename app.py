import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai

# Configuring the Key and initiating the model
genai.configure(api_key=os.getenv('GOOGLE-API-KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

st.markdown("<h2 style='text-align: center;'>🤖 Gemini Chatbot</h2>", unsafe_allow_html=True)

# Initiate the memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display the chat
for chat in st.session_state.chat_history:
    with st.chat_message(chat['role']):
        st.markdown(chat['content'])

user_input = st.chat_input("What do you want to ask?")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role":"user",
                                         "content":user_input})
    
    gemini_history = [{"role":msg["role"],
                       "parts":msg["content"]} for msg in st.session_state.chat_history]
    
    response = model.generate_content(gemini_history).text


    # Show Gemini Response
    bot_reply = response
    st.chat_message(bot_reply).markdown(bot_reply)
    st.session_state.chat_history.append({"role":"assistant",
                                          "content":bot_reply})