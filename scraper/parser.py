import re
from bs4 import BeautifulSoup


class BooksParser:
    def __init__(self, page: str | bytes):
        self.soup = BeautifulSoup(page, 'lxml')

    def get_categories(self) -> list[dict]:
        ul = self.soup.find('ul', 'nav nav-list').find('ul')
        categories = ul.find_all('a')
        result = [
            {
                'name': x.text.strip(),
                'url': x.get('href'),
            }
            for x in categories
        ]
        return result

    def get_number_of_pages(self) -> int:
        li = self.soup.find('li', 'current')
        text = li.text
        total_pages = text.split()[-1]
        return int(total_pages)

    def get_detail_links(self) -> list[str]:
        ol = self.soup.find('ol', 'row')
        book_cards = ol.find_all('li')
        result = []

        for card in book_cards:
            div = card.find('div', 'image_container')
            result.append(div.a.get('href'))

        return result


class BookDetailParser:
    def __init__(self, page: str | bytes):
        self.soup = BeautifulSoup(page, 'lxml')

    def get_book_details(self) -> dict:
        return {
            'title': self._get_title(),
            'description': self._get_description(),
            'upc': self._get_upc(),
            'price': self._get_price(),
            'stock': self._get_stock(),
            'rating': self._get_rating(),
            'number_of_reviews': self._get_number_of_reviews(),
        }

    def _get_title(self) -> str:
        div = self.soup.find('div', 'product_main')
        return div.h1.text

    def _get_description(self) -> str:
        div = self.soup.find('div', id='product_description')
        return div.find_next('p').text

    def _get_upc(self) -> str:
        table = self.soup.find('table')
        rows = table.find_all('tr')
        for row in rows:
            if row.th.text.lower() == 'upc':
                return row.td.text

    def _get_price(self) -> float:
        price = self.soup.find('p', 'price_color').text
        res = re.search(r'\d+\.\d+', price)
        return float(res.group())

    def _get_stock(self) -> int:
        p = self.soup.find('p', 'instock availability')
        stock = p.text.strip()
        result = re.search(r'\d+', stock)
        return int(result.group())

    def _get_rating(self) -> int:
        p = self.soup.find('p', 'star-rating')
        rating = p['class'][-1]
        return self._rating_mapper(rating)

    def _rating_mapper(self, rating: str) -> int:
        return {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5,
        }.get(rating, 0)

    def _get_number_of_reviews(self) -> int:
        table = self.soup.find('table')
        rows = table.find_all('tr')
        for row in rows:
            if row.th.text.lower() == 'number of reviews':
                return int(row.td.text)
