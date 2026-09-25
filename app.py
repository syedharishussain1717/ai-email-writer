import streamlit as st
from groq import Groq

# Read the API key from Streamlit Secrets (never hard-coded)
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

MODEL = "openai/gpt-oss-20b"

st.title("✉️ AI Email Writer")
st.write("Describe what you want to say, and I'll write the email.")

user_request = st.text_area("What should the email be about?")

if st.button("Generate Email"):
    if not user_request.strip():
        st.warning("Please type something first.")
    else:
        prompt = f"Write a short, polite, professional email for this request: {user_request}"
        try:
            with st.spinner("Writing..."):
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=[{"role": "user", "content": prompt}],
                )
            st.subheader("Your email")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Something went wrong: {e}")