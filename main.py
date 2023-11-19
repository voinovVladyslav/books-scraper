import requests

from scraper.parser import BooksParser


BASE_URL = 'http://books.toscrape.com/'


response = requests.get(BASE_URL)
print('Status:', response.status_code, BASE_URL)

parser = BooksParser(response.content)
