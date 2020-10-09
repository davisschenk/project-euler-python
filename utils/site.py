import bs4
import requests
from dateutil import parser


def get_problems(page):
    page = bs4.BeautifulSoup(page, 'html.parser')
    table = page.find(id="problems_table")

    for row in table.find_all("tr")[1:]:
        id_ = row.find("td", class_="id_column").get_text()
        title_element = row.find("a")
        title = title_element.get_text()
        published = parser.parse(title_element["title"].strip("Published on "))
        solved_by = row.find("div").get_text()

        yield id_, title, published, solved_by


def scrape_problems():
    page = requests.get("https://projecteuler.net/archives")
    current_page = 2
    last_page = None

    while page.status_code == 200:
        if last_page == page.text:
            break
        yield from get_problems(page.text)
        last_page = page.text
        page = requests.get(f"https://projecteuler.net/archives;page={current_page}")
        current_page += 1


for p in scrape_problems():
    print(p)
