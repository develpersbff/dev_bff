import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import re


# def tag_selector():
#     return tag.name == "a" and tag.has_attr("data-testid") and "result-title-a" in tag.get("data-testid")


def web_scraper(query):
    with sync_playwright() as p:
        user_input = str(input('>>'))
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        # browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f'https://duckduckgo.com/?q=' + user_input)
        # top_result = page.get_by_text('r1-0')
        # print(top_result)
        content = page.content()
        # beautiful soup and run parsing function
        soup = BeautifulSoup(content, features='html.parser')
        top_search = soup.find(id='r1-0')
        # A special attribution to ChatGPT for giving us the regex pattern below:
        pattern = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"

        matches = re.findall(pattern, str(top_search))
        top_result = matches[0][:-1]
        top_result_link = "https://" + top_result
        print(top_result_link)
        return top_result_link


def article_scraper(web_scraper):
    top_result_link = web_scraper('query')
    print(f'this is the top result link {top_result_link}')
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        # browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(top_result_link)
        # top_result = page.get_by_text('r1-0')
        # print(top_result)
        content = page.content()
        # beautiful soup and run parsing function
        soup = BeautifulSoup(content, features='html.parser')
        # raw_text = page.inner_html("#article").text
        print(soup)

        # print(top_link)

        # browser.close()


article_scraper(web_scraper)




