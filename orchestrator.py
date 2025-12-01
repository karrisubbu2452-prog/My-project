import os
import re
import requests
from pathlib import Path
from bs4 import BeautifulSoup

def sanitize_filename(name):
    """
    Replace any character that is not a letter, number, underscore, or dash with '_'.
    """
    return re.sub(r'[^A-Za-z0-9_-]', '_', name)

def get_web_summary(topic):
    try:
        print(f"Fetching summary for topic: {topic}")
        url_topic = topic.replace(" ", "_")
        url = f"https://en.wikipedia.org/wiki/{url_topic}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.select("p")
        summary = ""

        for p in paragraphs:
            text = p.get_text(strip=True)
            if text:
                summary = text
                break

        if not summary:
            summary = f"No summary found for '{topic}'."
        return summary

    except requests.RequestException:
        return f"Error fetching summary for '{topic}'. Using dummy text."

def run_episode(topic="demo", style=None):
    # Sanitize topic to create a safe folder name
    safe_topic = sanitize_filename(topic)
    output_dir = f"./artifacts/{safe_topic}"
    os.makedirs(output_dir, exist_ok=True)

    # Get web summary
    web_summary = get_web_summary(topic)

    # Save summary to a text file
    output_path = os.path.join(output_dir, "transcript.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(web_summary)

    return {"status": "ok", "topic": topic, "output": output_path}

if __name__ == "__main__":
    topic = input("Enter podcast topic: ")
    result = run_episode(topic)
    print(result)
