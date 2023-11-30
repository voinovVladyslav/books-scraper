from .constants import BASE_URL


def get_urls(total_pages: int) -> list[str]:
    base_url = 'http://books.toscrape.com/catalogue/page-{page}.html'

    result = []
    for i in range(1, total_pages + 1):
        result.append(base_url.format(page=i))

    return result


def make_links_absolute(links: list[str]) -> list[str]:
    return [BASE_URL + 'catalogue/' + link for link in links]
