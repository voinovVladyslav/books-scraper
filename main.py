import requests

from scraper.parser import BooksParser
from scraper.utils import get_urls


BASE_URL = 'http://books.toscrape.com/'


response = requests.get(BASE_URL)
print('Status:', response.status_code, BASE_URL)

parser = BooksParser(response.content)
number_of_pages = parser.get_number_of_pages()

urls = get_urls(number_of_pages)
print(urls)
