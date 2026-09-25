# ✉️ AI Email Writer

A simple Streamlit web app that uses the **Groq API** to turn a rough description into a short, polite, professional email.

Built as a beginner-friendly project: tested in Google Colab, deployed on Streamlit Community Cloud.

## How it works

1. You type what you want to say (e.g. *"ask my manager for Friday off"*).
2. The app sends your text to Groq's `openai/gpt-oss-20b` model.
3. The AI writes a short professional email, shown right on the page.

## Tech stack

- **Python**
- **[Streamlit](https://streamlit.io)** — web interface
- **[Groq API](https://console.groq.com)** — AI text generation

## Project files

```text
ai-email-writer/
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
├── .gitignore           # Keeps secrets out of GitHub
└── README.md            # This file
```

## Running locally

1. Clone this repo and open the folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.streamlit/secrets.toml` file with your Groq key:
   ```toml
   GROQ_API_KEY = "your_real_key_here"
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Deployment

This app is deployed on **Streamlit Community Cloud**. The `GROQ_API_KEY` is stored in the app's Secrets settings — it is never hard-coded or committed to GitHub.

## Notes

- Get a free Groq API key at [console.groq.com](https://console.groq.com).
- Model used: `openai/gpt-oss-20b` (Groq's free tier).