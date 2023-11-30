import requests

from scraper.parser import BooksParser, BookDetailParser
from scraper.utils import get_urls, make_links_absolute
from scraper.constants import BASE_URL


response = requests.get(BASE_URL)
print('Status:', response.status_code, BASE_URL)

parser = BooksParser(response.content)
number_of_pages = parser.get_number_of_pages()

urls = get_urls(number_of_pages)

links = []
for url in urls[:1]:
    response = requests.get(url)
    print('Status:', response.status_code, url)
    parser = BooksParser(response.content)
    links += make_links_absolute(parser.get_detail_links())

print(len(links))

detail_link = links[0]
print(detail_link)
response = requests.get(detail_link)
detail_parser = BookDetailParser(response.content)
print(detail_parser.get_book_details())
