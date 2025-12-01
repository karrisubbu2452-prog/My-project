import requests
from bs4 import BeautifulSoup

def get_web_summary(topic: str):
    try:
        # Use DuckDuckGo instant answers (free, no API key needed)
        url = f"https://duckduckgo.com/?q={topic.replace(' ', '+')}&ia=web"
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract descriptions/snippets
        results = soup.find_all("a", class_="result__a")

        if not results:
            return "No results found."

        summary_text = f"Web Summary for '{topic}':\n\n"

        count = 0
        for r in results[:5]:  # take top 5
            summary_text += "- " + r.get_text(strip=True) + "\n"
            count += 1

        return summary_text

    except Exception as e:
        return f"Error fetching summary: {str(e)}"
