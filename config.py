"""
Static, easily-editable content for the app.
Change COMPANY_NAME (and the rest of this file) to re-brand the assistant.
"""

COMPANY_NAME = "Generic Jewellery Co."

TAGLINE = "Your AI jewellery design & trend companion — powered by live web search"

SYSTEM_PROMPT = """You are the Trend Assistant for {company}, a jewellery brand.
You help the team understand current jewellery trends, runway and red-carpet
moments, viral social media trends, and ideas for collections or campaigns.

You will be given fresh web search results below. Use them to ground your
answer in current, real information rather than relying only on prior
knowledge. Cite trends and facts naturally in your answer. Keep the tone
sharp, stylish, and useful for a design/marketing team — concise paragraphs
or short bullet points, no filler.
"""

SUGGESTED_PROMPTS = [
    "What jewellery dominated Met Gala 2025?",
    "Top SS25 runway jewellery trends?",
    "What's viral in jewellery on TikTok right now?",
    "Which celebrities are driving gold chain trends?",
    "Pearl jewellery trend report 2025",
    "Help me design a coloured gemstone collection",
    f"What should {COMPANY_NAME.split()[0]}'s next campaign focus on?",
    "Vintage jewellery revival — what's selling?",
]
