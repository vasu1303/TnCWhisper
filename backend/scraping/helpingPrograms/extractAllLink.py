import requests
from bs4 import BeautifulSoup



def get_links(url,header):
    r = requests.get(url, headers=header)
    # if r.status_code != 200:
    #     r = requests.get(url)
    #     if r.status_code!=200:
    #         print(f"error {r.status_code} \nunable to extract the data")
    #         return []

    soup = BeautifulSoup(r.text, 'html.parser')

    # header = soup.find('header')
    # footer = soup.find('footer')


    all_links = soup.find_all('a', href=True)

    filteredLinks = []
    for link in all_links:
        filteredLinks.append(link['href'])

    return filteredLinks



