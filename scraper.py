import requests
from bs4 import BeautifulSoup
with open('scraped_content.html', 'w', encoding='utf-8') as f: f.write(str(BeautifulSoup(requests.get(input("Enter the URL to scrape: ")).text, 'html.parser')))
input("Scraped Successfully. Press Enter to exit...")