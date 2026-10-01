'''
Steps:

1 - Title
2 - Message input field
3 - When the user sends a message:
    3.1 - Display the message in the conversation
    3.2 - Send the message to the AI ​​for a response
    3.3 - Display the AI's response
    
Import library: pip install streamlit openai

Run the program using the 'streamlit run' command in the Terminal.

'''

import streamlit as st
import openai as op

st.write('# AI CHATBOT')

user_message = st.chat_input('Escreva sua mensagem aqui...')

print(user_message)