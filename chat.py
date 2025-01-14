from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Configure the Gemini Pro model with API key
genai.configure(api_key="AIzaSyAUHnrRdMaiKoepWe3cRsczAC8kMoCUc80")

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize the Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Input and submit button
user_input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# If the "Ask the question" button is clicked
if submit and user_input:
    response = get_gemini_response(user_input)
    
    st.subheader("The Response is")
    response_text = ""
    for chunk in response:
        st.write(chunk.text)
        st.write("_" * 80)
        response_text += chunk.text

    st.write(chat.history)
