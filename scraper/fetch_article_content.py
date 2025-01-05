import requests
from bs4 import BeautifulSoup

def fetch_article_content(article_url, headers):
    # fetch and parse the content of a single article
    try:
        response2 = requests.get(article_url, headers=headers, timeout=10)
        response2.raise_for_status()
        soup2 = BeautifulSoup(response2.text, "html.parser")
        
        content_div = soup2.find('div', class_='index_richTextContent__9H5yk')
        if content_div:
            return content_div.get_text(separator="\n").strip()
        else:
            return "Content not found."
    except Exception as e:
        # print(f"Error fetching article content: {e}")
        return "Error fetching content."