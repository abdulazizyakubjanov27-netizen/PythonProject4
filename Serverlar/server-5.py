import requests
import re

visited = set()

def crawl(url):

    if url in visited:
        return

    visited.add(url)

    print("Ochilyapti:", url)

    try:
        html = requests.get(url).text
    except:
        return

    links = re.findall(r'href="(https?://.*?)"', html)

    for link in links[:5]:
        crawl(link)

crawl("https://example.com")