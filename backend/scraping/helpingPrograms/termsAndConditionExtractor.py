import requests
from bs4 import BeautifulSoup


def scrape_terms_and_conditions(url, path, headers):
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    header = soup.find('header')
    footer = soup.find('footer')
    button = soup.find('button')
    anchor = soup.find('a')
    select = soup.find('select')
    nav = soup.find('nav')
    if header:
        header.extract()
    if footer:
        footer.extract()
    if button:
        button.extract()
    if select:
        select.extract()
    if anchor:
        anchor.extract()
    if nav: 
        nav.extract()

    # for link in soup.find_all('a'):
    #     link.extract()

    terms_and_conditions = soup.text

    terms_and_conditions = terms_and_conditions.strip()
    with open(path, "w", encoding="utf-8") as f:
        f.write(terms_and_conditions)
    return terms_and_conditions
