# -*- coding: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Nos dirigimos al directorio actual
Path = os.getcwd()

# Ejemplo para la página de PromPerú, obtención del contenido html
url = 'https://exportemos.pe/inteligencia-para-exportar/mercados'
response = requests.get(url)
mysoup = BeautifulSoup(response.content, 'html.parser')

# Separamos el contenido en una lista, según separador entre los PDFs
pdf_links = str(mysoup).split('"')

# Verificación de directorio existente, sino se crea
dir_name_pdf = Path+'\pdf_list'
if not os.path.exists(dir_name_pdf):
    os.mkdir(dir_name_pdf)

# Me dirijo al directorio creado y abro un .txt
os.chdir(dir_name_pdf)
with open('pdf.txt', 'w', encoding='utf-8') as file:
    for i in pdf_links:
        #Selecciono solo los elementos que terminan en .pdf (los archivos que quiero), y los escribo en un .txt
        if i.endswith('.pdf'):
            file.write(i+'\n')

# Regreso al directorio actual
os.chdir(Path)