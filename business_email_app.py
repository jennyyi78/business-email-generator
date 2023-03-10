import openai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Load the OpenAI API key
openai.api_key = os.getenv("API_KEY")

# Define the prompt for GPT-3
prompt = "Generate a business email in US English that is friendly, but still professional and appropriate for the workplace. The email topic is: "

def generate_email():
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{prompt} {scenario}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

st.title("Business Email Generator")

# Define the scenario for the business email
scenario = st.text_input("Enter topic")

if st.button("Generate Email"):
    email = generate_email()
    st.write("Here's your email:")
    st.write("=" * 30)
    st.write(email)
