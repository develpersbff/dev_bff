import pytest
from src.web_scraping_module import web_scraper, web_scraper_second, sync_playwright, re

import requests
from bs4 import BeautifulSoup

# Test to check to see if BeautifulSoup import works
# @pytest.mark.skip("TODO")
def test_web_scraper_import_beautifulSoup():
    beautiful_soup = BeautifulSoup
    actual = bool(BeautifulSoup)
    expected = True
    assert actual == expected

def test_web_scraper_second_import_beautifulSoup():
    beautiful_soup = BeautifulSoup
    actual = bool(BeautifulSoup)
    expected = True
    assert actual == expected


# Test to check to see if Playwright import works
# @pytest.mark.skip("TODO")
def test_web_scraper_import_playwright():
    playwright = sync_playwright()
    actual = bool(playwright)
    expected = True
    assert actual == expected


# Test to check to see if Regex import works
# @pytest.mark.skip("TODO")
def test_web_scraper_import_regex():
    regex = re
    actual = bool(re)
    expected = True
    assert actual == expected


# Test to check to see if the web_scarper is making a successful get request
# @pytest.mark.skip("TODO")
def test_web_scraper_get_request():
    url = 'https://www.demoblaze.com/'
    r = requests.get(url)
    print(r)
    actual = bool(r)
    expected = True
    assert actual == expected


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










test_web_scraper_get_working()
test_web_scraper_gives_result()
