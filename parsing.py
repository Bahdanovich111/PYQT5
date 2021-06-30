import requests, datetime
from bs4 import BeautifulSoup
import re

import sqlite3 as sq

URL = 'https://www.gismeteo.by/'
URL1 = 'https://pogoda.by/'
URL2 = 'https://yandex.by/pogoda/'
HEADERS = {

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.41 YaBrowser/21.5.0.579 Yowser/2.5 Safari/537.36',
}


# with sq.connect('archive.db') as conn:
#     cur = conn.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS archive(
#         id INT,
#         time TEXT
#
#     )""")


def get_html(url, params=''):
    resp = requests.get(url, headers=HEADERS, params=params)
    return resp


def get_content1(html1):
    soup = BeautifulSoup(html1, 'html.parser')
    items = soup.find_all('div', style='background: url(tpl/img/downpanel.gif) bottom repeat-x;')
    #print(items)
    list_1 = []
    for item in items:
        list_1.append(

                item.find('table', class_='src').find('td', valign="top").find('p').get_text(strip=True)


        )
    #print(list_1)
    return list_1



def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='wn_body')
    list_ = []
    for item in items:
        list_.append(
            {
                'Температура сейчас': item.find('div', class_='info_item _main clearfix').find('div',
                                                                                               class_='ii _temp').find(
                    'div', class_='js_meas_container temperature').find('span',
                                                                        class_='value unit unit_temperature_c').get_text(
                    strip=True),
                'Скорость ветра':
                    item.find('div', class_='information _attention').find_all('div', class_='info_item clearfix')[
                        1].find('div', class_='ii info_value').find('span', class_='unit unit_wind_m_s').get_text(
                        strip=True)
            }
        )
    return list_

def get_content2(html2):
    soup = BeautifulSoup(html2, 'html.parser')
    items = soup.find_all('div', class_='b-page__container')
    list_2 = []
    for item in items:
        list_2.append(
            {
                'Температура сейчас': item.find('div', class_='content content_compressed i-bem').find(
                     'div', class_='fact__temp-wrap').find('div',
                                                           class_='temp fact__temp fact__temp_size_s').get_text(
                      strip=True)

            }
        )
        list_2.append(
            {
                'Температура сейчас': item.find('div', class_='content content_compressed i-bem').find(
                     'div', class_='link__condition day-anchor i-bem').get_text(
                      strip=True)

            }
        )
    return list_2



def makeRequest():
    html = get_html(URL)              #gismetio
    html1 = get_html(URL1)              #pogoda.by
    html2 = get_html(URL2)                  #yandex.by
    gis = (get_content(html.text))
    gis_temp = (gis[0]['Температура сейчас'])
    yan = get_content2(html2.text)
    print('GISMETIO:', *get_content(html.text))
    yan_temp = (yan[0]['Температура сейчас'])
    l1 = (get_content1(html1.text))
    #print(('POGODA.BY:', get_content1(html1.text))[1][0])
    print('POGODA.BY:', re.findall(r"\w{11}\b.+\w\/\w", *l1))
    pog_temp = re.findall(r"\d{2}[.].", *l1)
    print(*l1)
    print(pog_temp)

    return gis_temp, yan_temp, pog_temp







#makeRequest()

# time = (datetime.datetime.now().strftime("%Y-%m-%d-%H.%M"))
# # time = (datetime.datetime.now().strftime("%Y-%m-%d-%H.%M"))
# print(datetime.datetime.now().strftime("%Y-%m-%d-%H.%M"))
# temp =

# cur.execute(f"INSERT INTO archive VALUES ({gis_},{time})")
# conn.commit()
#
# cur.execute("SELECT * FROM archive")
# result = cur.fetchall()
# print(result)
# time_ = (datetime.datetime.today())
# time1 = (datetime.datetime.now())
# print(time_)
# print(time1)

# cur.execute("SELECT time FROM archive")
# resul = cur.fetchall()
# print(resul)
