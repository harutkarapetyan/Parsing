from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service

import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


#Ключевое слово для поиска на Avito
SEARCH_QUERY = "Ноутбук"

#URL для поиска на Avito
URL = f"https://www.avito.ru/all?q={SEARCH_QUERY}"

#Настройка ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#Открываем страницу
driver.get(URL)
time.sleep(5)  # Ожидаем загрузки страницы

#Получаем HTML
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

#Классы для itemprop
ITEM_CLASS = "iva-item-body-GQomw"  # Основной класс блока товаров
NAME_ITEMPROP = "name"              # itemprop для названия
PRICE_ITEMPROP = "price"            # itemprop для цены
CURRENCY_ITEMPROP = "priceCurrency" # itemprop для валюты

#Получение данных о товарах
items = soup.find_all("div", class_=ITEM_CLASS)

data = []

for item in items:
    try:

        name_tag = item.find("h3", itemprop=NAME_ITEMPROP)
        name = name_tag.text.strip() if name_tag else "Не найдено"

        #Цена
        price_tag = item.find("meta", itemprop=PRICE_ITEMPROP)
        price = price_tag.get("content") if price_tag else "Не найдено"

        #Валюта
        currency_tag = item.find("meta", itemprop=CURRENCY_ITEMPROP)
        currency = currency_tag.get("content") if currency_tag else "Не найдено"

        #Сохранение данных
        data.append({"Название": name, "Цена": price, "Валюта": currency})

    except Exception as e:
        print(f"Ошибка: {e}")

#Закрываем браузер
driver.quit()

#Сохраняем данные в файлы CSV и Excel
df = pd.DataFrame(data)
df.to_csv("avito_data.csv", index=False)
df.to_excel("avito_data.xlsx", index=False)

print("Данные успешно сохранены!")