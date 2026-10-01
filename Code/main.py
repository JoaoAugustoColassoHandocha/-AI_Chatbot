'''    
Import library: pip install streamlit openai

Run the program using the command 'streamlit run "FileName.py"' in the terminal.

'''

import streamlit as st
import openai as op

st.write('# AI CHATBOT')

if not 'message_list' in st.session_state:
    
    st.session_state['message_list'] = []

user_message = st.chat_input('Escreva sua mensagem aqui...')

for message in st.session_state['message_list']:
    
    sender = ''
    message_text = ''
    st.chat_message(sender).write(message_text)

if user_message:
    
    st.chat_message('user').write(user_message)
    question = {'role': 'user', 'content': user_message}
    st.session_state['message_list'].append(question)
    
    ai_response = 'Você perguntou: ' + user_message
    st.chat_message('assistant').write(ai_response)
    response = {'role': 'assistant', 'content': ai_response}
    st.session_state['message_list'].append(response)