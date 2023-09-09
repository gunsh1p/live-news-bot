import requests

from fake_useragent import UserAgent
from bs4 import BeautifulSoup

from parsed_data import ParsedData
from clean_html import cleanhtml

class TheVerge:
    def __init__(self, link) -> None:
        self.link = link
        self.ua = UserAgent()
    
    def parse(self) -> ParsedData:
        result = ParsedData(self.link, [])
        headers = {
            "User-Agent": self.ua.random
        }
        req = requests.get(
            url=self.link,
            headers=headers
        )
        bs = BeautifulSoup(req.text, features="html.parser")
        blocks = bs.find_all('div', {'class': ['duet--article--article-body-component']})
        for block in blocks:
            text = block.find('p')
            if not text:
                continue
            result.text.append(cleanhtml(block.text))
        return result