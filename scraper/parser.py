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
