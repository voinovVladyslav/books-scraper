import requests

from scraper.parser import BooksParser
from scraper.utils import get_urls, make_links_absolute
from scraper.constants import BASE_URL


response = requests.get(BASE_URL)
print('Status:', response.status_code, BASE_URL)

parser = BooksParser(response.content)
number_of_pages = parser.get_number_of_pages()

urls = get_urls(number_of_pages)

links = []
for url in urls:
    response = requests.get(url)
    print('Status:', response.status_code, url)
    parser = BooksParser(response.content)
    links += make_links_absolute(parser.get_detail_links())

print(len(links))
