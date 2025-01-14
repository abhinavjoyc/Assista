import streamlit as st
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

# Initialize session state for chat history if not already done
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input and submit button
user_input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit and user_input:
    response = get_gemini_response(user_input)
    
    # Append user query and response to chat history
    st.session_state['chat_history'].append(("You", user_input))

    st.subheader("The Response is")
    response_text = ""
    for chunk in response:
        st.write(chunk.text)
        response_text += chunk.text

    st.session_state['chat_history'].append(("Bot", response_text))

# Display chat history
st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
