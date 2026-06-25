"""
Thin wrapper around the Groq chat completions API (OpenAI-compatible schema).
Keeps all LLM-call logic isolated from the rest of the app.
"""

from typing import List, Dict
import requests

GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.3-70b-versatile"


def get_groq_response(
    system_prompt: str,
    chat_history: List[Dict],
    user_prompt: str,
    web_context: str,
    api_key: str,
) -> str:
    """
    Send the conversation (plus fresh web context) to Groq and return the
    assistant's reply as plain text.
    """
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(
        {"role": m["role"], "content": m["content"]} for m in chat_history
    )
    messages.append(
        {
            "role": "user",
            "content": (
                f"Live web search results:\n{web_context}\n\n"
                f"User question: {user_prompt}"
            ),
        }
    )

    try:
        response = requests.post(
            GROQ_ENDPOINT,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": MODEL,
                "messages": messages,
                "temperature": 0.6,
                "max_tokens": 1024,
            },
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except requests.RequestException as exc:
        return f"Sorry, I couldn't reach the AI model. ({exc})"
    except (KeyError, IndexError):
        return "Sorry, I received an unexpected response from the AI model."
