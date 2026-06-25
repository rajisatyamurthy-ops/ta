"""
Trend Assistant — AI design & trend companion powered by live web search.

Main Streamlit entry point. Keeps the app modular by delegating:
  - styling        -> styles.py
  - LLM calls       -> groq_client.py
  - web search      -> tavily_client.py
  - static content  -> config.py
"""

import streamlit as st

from config import COMPANY_NAME, TAGLINE, SUGGESTED_PROMPTS, SYSTEM_PROMPT
from styles import CUSTOM_CSS
from groq_client import get_groq_response
from tavily_client import get_web_context

st.set_page_config(
    page_title=f"{COMPANY_NAME} Trend Assistant",
    page_icon="💎",
    layout="wide",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Session state
# ---------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None


def queue_prompt(prompt: str) -> None:
    """Stash a prompt (from a suggestion button or the chat box) to be run."""
    st.session_state.pending_prompt = prompt


# ---------------------------------------------------------------------------
# Sidebar — Setup
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### ⚙️ Setup")
    st.markdown("Both are **free**, no card needed:")
    st.markdown(
        "🔑 [Groq key](https://console.groq.com/keys) — the AI brain  \n"
        "🔍 [Tavily key](https://app.tavily.com/) — live web search"
    )

    groq_api_key = st.text_input("Groq API key", type="password", placeholder="gsk_...")
    tavily_api_key = st.text_input("Tavily API key", type="password", placeholder="tvly-...")

    st.caption("Keys are kept only for this session and are never stored or logged.")

    st.markdown("---")
    st.markdown("**What you can ask**")
    for example in SUGGESTED_PROMPTS[:4]:
        st.markdown(f"- *{example}*")

    if st.session_state.messages:
        st.markdown("---")
        if st.button("🗑️ Clear conversation"):
            st.session_state.messages = []
            st.rerun()

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown(
    f"""
    <div class="header-block">
        <p class="eyebrow">◦ {COMPANY_NAME.upper()} ◦</p>
        <h1 class="hero-title">Trend <span class="accent">Assistant</span></h1>
        <p class="subtitle">{TAGLINE}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Suggestion grid (only shown before the conversation starts)
# ---------------------------------------------------------------------------
if not st.session_state.messages:
    st.markdown(
        """
        <div class="ask-block">
            <h3>Ask me anything about jewellery trends</h3>
            <p class="livesearch-caption">I HAVE LIVE WEB SEARCH — SO MY KNOWLEDGE IS ALWAYS CURRENT</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(4)
    for i, prompt in enumerate(SUGGESTED_PROMPTS):
        with cols[i % 4]:
            if st.button(prompt, key=f"suggestion_{i}", use_container_width=True):
                queue_prompt(prompt)

# ---------------------------------------------------------------------------
# Chat history
# ---------------------------------------------------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------------------------------------------------------
# Chat input
# ---------------------------------------------------------------------------
typed_prompt = st.chat_input("Ask about a trend, campaign idea, or design direction...")
if typed_prompt:
    queue_prompt(typed_prompt)

# ---------------------------------------------------------------------------
# Run the pending prompt (from a button click or the chat box)
# ---------------------------------------------------------------------------
if st.session_state.pending_prompt:
    prompt = st.session_state.pending_prompt
    st.session_state.pending_prompt = None

    if not groq_api_key or not tavily_api_key:
        st.warning("Please add both your Groq and Tavily API keys in the sidebar to continue.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Searching the web for the latest trends..."):
                web_context, sources = get_web_context(prompt, tavily_api_key)

            with st.spinner("Thinking..."):
                answer = get_groq_response(
                    system_prompt=SYSTEM_PROMPT.format(company=COMPANY_NAME),
                    chat_history=st.session_state.messages[:-1],
                    user_prompt=prompt,
                    web_context=web_context,
                    api_key=groq_api_key,
                )

            st.markdown(answer)
            if sources:
                with st.expander("Sources"):
                    for s in sources:
                        st.markdown(f"- [{s['title']}]({s['url']})")

        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.rerun()
