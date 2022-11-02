# -*- coding: utf-8 -*-

import requests 
from bs4 import BeautifulSoup
import pandas as pd

#WebScraping para obtener la tabla en un DataFrame

url = 'https://www.worldometers.info/world-population/population-by-country/'
response = requests.get(url)
mysoup = BeautifulSoup(response.content, 'html.parser')

table_countries = mysoup.find('table', attrs={"id":"example2"})

rows = table_countries.find('tbody').find_all('tr')
columns = [column.get_text() for column in table_countries.find('thead').find_all('th')]

table = {}

for idx in range(len(columns)):
    table[columns[idx]] = []

for row in rows:
    for idx, column in enumerate(columns):
        table[column].append(row.find_all('td')[idx].get_text())
    
df = pd.DataFrame(table)
df.to_csv('population-by-country.csv', index=False)