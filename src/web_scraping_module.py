from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import re


def web_scraper(user_input):
    with sync_playwright() as p:
        # user_input = str(input('>>'))
        if user_input:
            browser = p.chromium.launch(slow_mo=1000)
            page = browser.new_page()
            page.goto(f'https://duckduckgo.com/?q=' + user_input)
            content = page.content()
            # beautiful soup and run parsing function
            soup = BeautifulSoup(content, features='html.parser')
            top_search = soup.find(id='r1-0')
            # print(f"this is the r1-0 {top_search}")
            # A special attribution to ChatGPT for giving us the regex pattern below:
            pattern = r"(^https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
            matches = re.findall(pattern, str(top_search))
            # print(f"this is the matches {matches}")
            top_result = matches[2][:-1]
            top_result_link = top_result
            # print(top_result_link)
        else:
            print("Please enter a valid search query")
            user_input = str(input('>>>'))
        return top_result_link

def web_scraper_second(user_input):
    with sync_playwright() as p:
        # user_input = str(input('>>'))
        if user_input:
            browser = p.chromium.launch(slow_mo=1000)
            page = browser.new_page()
            page.goto(f'https://duckduckgo.com/?q=' + user_input)
            content = page.content()
            # beautiful soup and run parsing function
            soup = BeautifulSoup(content, features='html.parser')
            top_search = soup.find(id='r1-1')
            # print(f"this is the r1-0 {top_search}")
            # A special attribution to ChatGPT for giving us the regex pattern below:
            pattern = r"(^https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
            matches = re.findall(pattern, str(top_search))
            # print(f"this is the matches {matches}")
            second_result_link = matches[2][:-1]
            # print(second_result_link)
        else:
            print("Please enter a valid search query")
            user_input = str(input('>>>'))
        return second_result_link


# def article_scraper(web_scraper):
#     top_result_link = web_scraper()
#     print(f'this is the top result link {top_result_link}')
#     with sync_playwright() as p:
#         browser = p.chromium.launch(slow_mo=1000)
#         page = browser.new_page()
#         page.goto(top_result_link)
#         content = page.content()
#         # beautiful soup and run parsing function
#         soup = BeautifulSoup(content, features='html.parser')
#         p_tags = soup.find_all('p')
#         for p in p_tags:
#             print(p.get_text())



