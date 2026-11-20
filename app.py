import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

st.title("🤖 Gemini AI Text Generator")

prompt = st.text_area(
    "Enter your prompt",
    height=150
)

if st.button("Generate"):

    if prompt:

        try:

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

            st.success("Response Generated!")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter a prompt")