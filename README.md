# Trend Assistant

An AI jewellery trend assistant: it searches the live web (Tavily) and uses
that fresh context to answer questions via an LLM (Groq), in a Streamlit chat UI.

Rebrand it by editing `COMPANY_NAME` in `config.py`.

## Files

- `app.py` — main Streamlit app (UI + flow)
- `config.py` — brand name, copy, suggested prompts (edit this to re-brand)
- `styles.py` — custom CSS for the cream/gold look
- `tavily_client.py` — web search API calls
- `groq_client.py` — LLM API calls
- `requirements.txt` — dependencies

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

You'll enter your own Groq and Tavily API keys in the sidebar at runtime.
Keys are kept only in the browser session (`st.session_state`) — never
written to disk, logged, or committed anywhere.

- Get a free Groq key: https://console.groq.com/keys
- Get a free Tavily key: https://app.tavily.com/

## Deploy on Streamlit Community Cloud

1. Push this folder to a GitHub repo.
2. On https://share.streamlit.io, create a new app pointing at `app.py` in that repo.
3. Deploy — no secrets need to be configured, since each user enters their own
   API keys in the app's sidebar.
