import requests
from bs4 import BeautifulSoup
from app import settings


def curr_nbu():
    result = {}
    url = settings.url_nbu
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    table_curr = soup.find('tbody')
    curr_desc = table_curr.find_all(class_='ciClTw')
    curr_value = table_curr.find_all(class_='glerpA')

    for (cd, cv) in zip(curr_desc, curr_value):
        result[cd.text] = cv.text
    return result


# def curr_private():
#     url = settings.url_private
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     table_curr = soup.find('div', class_='courses-currencies')
#     curr_sale = table_curr.find_all(class_='sale')
#     curr_buy = table_curr.find_all(class_='purchase')
#     curr_name = table_curr.find_all(class_='names')
#     print('Курс валют Приват Банк')
#     for (cs, cb, cn) in zip(curr_buy, curr_sale, curr_name):
#         print(f'{cn.text.strip()[0:3]}  {cs.text.strip()}  {cb.text.strip()}')


# curr_nbu()
# print('---'*10)
# curr_private()
