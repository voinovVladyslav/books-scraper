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
