import google.generativeai as genai
import streamlit as st
genai.configure(api_key="AIzaSyBniEYo7qQCJdCkWfWHEdmE7s06Vg9XEmU")
model = genai.GenerativeModel("gemini-1.5-flash")
st.title("MetaXsouL AI")
st.write("This is a simple demo of MetaXsouL AI. You can ask any question and get an answer from the AI model.")
question = st.text_input("Enter your question here:")
if st.button("Ask"):
    if "sutradhar" or "Sutradhar" in question:
        st.write("He is my creator")
    else:
        response = model.generate_content(question)
    
        st.write(response.text)
