'''    
Import library: pip install streamlit openai

Run the program using the command 'streamlit run "FileName.py"' in the terminal.

'''

import streamlit as st
import openai as op

st.write('# AI CHATBOT')

user_message = st.chat_input('Escreva sua mensagem aqui...')

if user_message:
    
    st.chat_message('user').write(user_message)
    
    ai_response = 'Você perguntou: ' + user_message
    
    st.chat_message('assistant').write(ai_response)