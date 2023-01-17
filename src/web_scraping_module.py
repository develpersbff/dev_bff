import requests
from bs4 import BeautifulSoup


def web_scraper(query):
    user_input = str(input('>>'))
    req = requests.get(f'https://duckduckgo.com/?q=' + user_input)
    soup = BeautifulSoup(req.text, 'html.parser')
    top_result_class = soup.findAll('div', data_testid='result-title-a')
    # top_results_data = soup.find(data_testid='result-title-a')



    # for data in top_result_div:
    #     if data.find(class_='g'):
    #         print(data)



    # soup = BeautifulSoup(top_result_div, 'xml')
    # top_result_class = soup.findAll(class_='g')
    # top_result_class = soup.find(class_='g')
    # title = top_result.find('h3').text
    # url = top_result.find('a')['href']
    # text = top_result.get_text()
    # scrape_results = {'title': title, 'url': url, 'text': text}
    # print(scrape_results)
    # return scrape_results
    print('top_result', top_result_class)

    # print('req.text', req.text)
    # print(len(top_result_div))

web_scraper('query')





