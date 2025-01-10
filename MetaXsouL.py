import google.generativeai as genai
import streamlit as st
import random

js = [
    "He is my creator", "Joy Sutradhar is my creator", "He is a great person he created me",
    "He is a good person, he created me", "Joy Sutradhar is the core developer of me",
    "He made me, he is my creator", "He is my god, he created me", "Such a nice man he created me"
]

genai.configure(api_key="AIzaSyBniEYo7qQCJdCkWfWHEdmE7s06Vg9XEmU")
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("MetaXsouL AI")
st.write("This is a simple demo of MetaXsouL AI. You can ask any question and get an answer from the AI model.")
question = st.text_input("Enter your question here:")

if st.button("Ask"):
    if "sutradhar" in question.lower():
        st.write(random.choice(js))
    elif any(keyword in question.lower() for keyword in ["who is your creator", "who created you", "who is your developer", "who developed you", "who made you", "who is your god", "who is your godfather","who creat you","who is your creator","who is your developer","who is your god","who is your godfather","who developed you","who made you"]):
        st.write(random.choice(["I'm created by Joy Sutradhar", "My creator is Joy Sutradhar", "My developer is Joy Sutradhar"]))
    else:
        response = model.generate_content(question)
        st.write(response.text)
