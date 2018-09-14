from bs4 import BeautifulSoup
import urllib.request
import os


def search_spider():
    url = "https://en.wikipedia.org/wiki/Deep_learning"
    source_code = urllib.request.urlopen(url)
    plain_text = source_code
    soup = BeautifulSoup(plain_text, "html.parser")

    result_title = soup.title
    print("The title is" , result_title)

    result_a = soup.find_all('a')
    print("The a tags are", result_a)

    for link in result_a:
        result_href = link.get('href')
        print(result_href)



search_spider()