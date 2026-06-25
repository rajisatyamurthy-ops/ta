"""
Thin wrapper around the Tavily search API.
Keeps all web-search logic isolated from the rest of the app.
"""

from typing import List, Tuple, Dict
import requests

TAVILY_ENDPOINT = "https://api.tavily.com/search"


def get_web_context(query: str, api_key: str, max_results: int = 5) -> Tuple[str, List[Dict]]:
    """
    Run a live web search and return:
      - a plain-text context block to feed to the LLM
      - a list of {"title", "url"} source dicts for display

    Fails gracefully: on any error, returns an empty context so the app can
    still attempt to answer without live search.
    """
    try:
        response = requests.post(
            TAVILY_ENDPOINT,
            json={
                "api_key": api_key,
                "query": query,
                "search_depth": "advanced",
                "max_results": max_results,
                "include_answer": False,
            },
            timeout=20,
        )
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as exc:
        return f"[Web search unavailable: {exc}]", []

    results = data.get("results", [])
    if not results:
        return "[No web search results found.]", []

    context_lines = []
    sources = []
    for r in results:
        title = r.get("title", "Untitled")
        url = r.get("url", "")
        content = (r.get("content") or "").strip()
        context_lines.append(f"Source: {title} ({url})\n{content}")
        sources.append({"title": title, "url": url})

    context = "\n\n---\n\n".join(context_lines)
    return context, sources
