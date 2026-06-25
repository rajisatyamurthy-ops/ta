"""
Custom CSS injected once at app start. Isolated here so the visual design
can be tweaked without touching app logic.
"""

CUSTOM_CSS = """
<style>
.stApp {
    background-color: #fdfbf6;
}

.header-block {
    text-align: center;
    padding-top: 1rem;
    padding-bottom: 0.5rem;
}

.eyebrow {
    letter-spacing: 0.25em;
    font-size: 0.75rem;
    color: #a8954f;
    text-transform: uppercase;
    margin-bottom: 0.25rem;
}

.hero-title {
    font-family: 'Georgia', 'Times New Roman', serif;
    font-size: 3rem;
    font-weight: 400;
    color: #2b2b2b;
    margin: 0;
}

.hero-title .accent {
    font-style: italic;
    color: #b08d3e;
}

.subtitle {
    color: #8a8a8a;
    font-size: 0.95rem;
    margin-top: 0.25rem;
}

.ask-block {
    text-align: center;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

.ask-block h3 {
    font-family: 'Georgia', 'Times New Roman', serif;
    font-style: italic;
    color: #b08d3e;
    font-size: 1.4rem;
    margin-bottom: 0.25rem;
}

.livesearch-caption {
    letter-spacing: 0.1em;
    font-size: 0.7rem;
    color: #aaaaaa;
    text-transform: uppercase;
}

div[data-testid="stButton"] button {
    background-color: #fffdf8;
    border: 1px solid #ecdfc0;
    border-radius: 10px;
    color: #4a4a4a;
    font-size: 0.85rem;
    padding: 1rem 0.75rem;
    min-height: 90px;
    white-space: normal;
}

div[data-testid="stButton"] button:hover {
    border-color: #b08d3e;
    color: #b08d3e;
}
</style>
"""
