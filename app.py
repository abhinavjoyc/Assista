from dotenv import load_dotenv
import streamlit as st
import os
import textwrap
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Gemini Pro model with API key
genai.configure(api_key="AIzaSyAUHnrRdMaiKoepWe3cRsczAC8kMoCUc80")

# Function to load Gemini Pro model and get responses
def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text

# Initialize the Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Chatbot")

# Input and submit button
user_input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# If the "Ask the question" button is clicked
if submit and user_input:
    response = get_gemini_response(user_input)
    
    st.subheader("The Response is")
    st.write(response)
