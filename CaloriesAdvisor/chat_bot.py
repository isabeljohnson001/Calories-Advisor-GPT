from urllib import response
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro")

def get_response(question):
    response=model.generate_content(question)
    return response.text


st.set_page_config(page_title="QA Demo")
st.header("Gemini LL Application")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit:
    response=get_response(input)
    st.subheader("The response is")
    st.write(response)
    