import pytest
from src.web_scraping_module import web_scraper

import requests
from bs4 import BeautifulSoup

# tests that both the git request and BeasutifulSoup is working
# @pytest.mark.skip("TODO")
def test_web_scraper_get_working():
    url = 'https://www.demoblaze.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features='html.parser')
    search = soup.find('h5')
    actual = search.text
    # print(f" the soup find is {actual}")
    expected = 'New message'

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_web_scraper_gives_result():
    actual = web_scraper('testing123')
    expected = 'https://testing123.education.mn.gov/test/index.htm'
    assert actual == expected


def test_web_scrapper_valid_url():







test_web_scraper_get_working()
test_web_scraper_gives_result()
