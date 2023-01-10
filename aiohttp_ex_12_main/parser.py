import requests
from bs4 import BeautifulSoup
from app import settings


def curr_nbu_private():

    result = {}
    url = settings.url_nbu
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    table_curr = soup.find('tbody')
    curr_desc = table_curr.find_all(class_='ciClTw')
    curr_value = table_curr.find_all(class_='glerpA')

    for (cd, cv) in zip(curr_desc, curr_value):
        result[cd.text] = cv.text

    n = 0
    desc_value = ['EUR_PB', 'USD_PB', 'PLN_PB']
    url = settings.url_private
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    table_curr = soup.find('div', class_='courses-currencies')
    curr_value = table_curr.find_all('div', class_='purchase')
    for cv in curr_value:
        result[desc_value[0 + n]] = cv.text.strip()
        n = n + 1
    return result


