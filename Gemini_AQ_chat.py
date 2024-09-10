import streamlit as st
import os 
import google.generativeai as genai
import google.generativeai as genai
genai.configure(api_key='AIzaSyCs1tMPxILJffcuhSTJVJ0Wq_MSNpF6e6k')
model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])
def get_gemini_answer(question):
    response=chat.send_message(question,stream=True)
    return response
#initialize of streamlit app
st.header("Gemini Application")
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
input=st.text_input("Input:",key="input")
submit=st.button("Ask the question")
if submit and input:
    response=get_gemini_answer(input)
    # add chat to chat history
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader("The chat history is")
for role,text in st.session_state["chat_history"]:
    st.write(f"{role}:{text}")
