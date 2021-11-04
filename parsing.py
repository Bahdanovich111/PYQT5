import requests, time
from bs4 import BeautifulSoup
import re

URL = 'https://www.gismeteo.by/'
URL1 = 'https://pogoda.mail.ru/prognoz/minsk/'
URL2 = 'https://yandex.by/pogoda/'
HEADERS = {

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.41 YaBrowser/21.5.0.579 Yowser/2.5 Safari/537.36',
}


def get_html(url, params=''):
    resp = requests.get(url, headers=HEADERS, params=params)
    return resp


def get_content1(html1):
    soup = BeautifulSoup(html1, 'html.parser')
    items = soup.find_all('div', class_='information__content')
    list_1 = []
    for item in items:
        list_1.append(
            {'Температура сейчас': item.find('div',
                                             class_='information__content__additional information__content__additional_temperature').
                find('div', class_='information__content__temperature').get_text(strip=True)}
        )
        list_1.append(
            {'Ветер':
                 item.find('div', class_='information__content__additional information__content__additional_second').
                     find_all('div', class_='information__content__additional__item')[2].get_text(strip=True)}
        )
        list_1.append(
            {'Влажность':
                 item.find('div', class_='information__content__additional information__content__additional_second').
                     find_all('div', class_='information__content__additional__item')[1].get_text(strip=True)}
        )
    return list_1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='frame-now')
    # print(items)
    list_ = []
    for item in items:
        list_.append(
            {'Температура сейчас': item.find('span', class_='unit unit_temperature_c').get_text(strip=True)}
        )
        list_.append(
            {'Ветер': item.find('div', class_='weather-item weather-wind').find('div', class_='item-value').
                find('span', class_='unit unit_wind_m_s').get_text(strip=True)}
        )
        list_.append(
            {'Влажность': item.find('div', class_='weather-item weather-humidity').find('div', class_='item-value').
                get_text(strip=True)}
        )
    return list_


def get_content2(html2):
    soup = BeautifulSoup(html2, 'html.parser')
    items = soup.find_all('div', class_='b-page__container')
    list_2 = []
    for item in items:
        list_2.append(
            {'Температура сейчас': item.find('div', class_='content content_compressed i-bem').find('div',
                                                                                                    class_='fact__temp-wrap').
                find('div', class_='temp fact__temp fact__temp_size_s').find('span',
                                                                             class_='temp__value temp__value_with-unit').
                get_text(strip=True)}
        )
        list_2.append(
            {'Ветер': item.find('div', class_='content content_compressed i-bem').find('div', class_='fact__props').
                find('span', class_='wind-speed').get_text(strip=True)}
        )
        list_2.append(
            {'Влажность': item.find('div', class_='content__top').find('div', class_='fact__props').
                find('div', class_='term term_orient_v fact__humidity').get_text(strip=True)}
        )
    return list_2


def makeRequest():
    html = get_html(URL)  # gismetio
    html1 = get_html(URL1)  # pogoda.mail
    html2 = get_html(URL2)  # yandex.by
    gis = (get_content(html.text))
    gis_temp = (gis[0]['Температура сейчас'])
    gis_veter = (re.findall((r"\d\D\D\D"), (gis[1]['Ветер'])))
    gis_vlajnost = (gis[2]['Влажность'])
    yan = get_content2(html2.text)
    yan_temp = (yan[0]['Температура сейчас'])
    yan_veter = yan[1]['Ветер']
    yan_vlajnost = yan[2]['Влажность']
    pog = (get_content1(html1.text))
    pog_temp = (pog[0]['Температура сейчас'])
    pog_veter = (re.findall((r"\d"), pog[1]['Ветер']))[0]
    pog_vlajnost = (re.findall((r"\d\d%"), pog[2]['Влажность']))[0]

    return gis_temp, gis_veter, gis_vlajnost, yan_temp, yan_veter, yan_vlajnost, pog_temp, pog_veter, pog_vlajnost,

