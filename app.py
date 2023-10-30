import streamlit as st
import openai
import pdfplumber

# Initialize the OpenAI API with your API key
openai.api_key = "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"

# Define a chat history dictionary to store user-chatbot interactions
chat_history = []

st.title("PDF Chatbot")

# Upload PDF
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

pdf_text = ""  # Initialize pdf_text outside the if condition

if pdf_file:
   # Process the PDF and extract text
   with pdfplumber.open(pdf_file) as pdf:
       pdf_text = ""
       for page in pdf.pages:
           pdf_text += page.extract_text()

   # Allow the user to interact with the chatbot
   user_input = st.text_input("You: ")
   if user_input:
       chat_history.append({"role": "user", "content": user_input})

       # Send the chat history to OpenAI
       chatbot_response = openai.ChatCompletion.create(
           model="gpt-3.5-turbo",
           messages=chat_history
       )

       # Get and display the chatbot's reply
       chat_history.append({"role": "assistant", "content": chatbot_response.choices[0].message["content"]})
       st.text("Chatbot: " + chatbot_response.choices[0].message["content"])

# Display the PDF content
st.text("PDF Content:")
st.text(pdf_text)
