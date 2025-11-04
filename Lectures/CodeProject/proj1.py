import requests
from bs4 import BeautifulSoup
import re

url = 'https://en.wikipedia.org/wiki/BTS'

def get_wiki(url) :
    myHeader = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Wind64; x64)'}
    response = requests.get(url, headers=myHeader)

    soup = BeautifulSoup(response.text, "html.parser")

    paragraph = soup.find_all('p')
    full_text = ""
    for para in paragraph:
        text = para.get_text()
        if text.strip():
            full_text += text + "\n"

    words = re.findall(r"\b\w+\b", full_text.lower())

    return words
    
word_list = get_wiki(url)
print(word_list)