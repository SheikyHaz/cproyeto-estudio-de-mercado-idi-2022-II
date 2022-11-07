# -*- coding: utf-8 -*-
import os
import requests
import fitz

# Función: Crea o sobreescribe un archivo .pdf para poder consultarlo después
def generate_pdf(pdf_url, pdf_file, dir):
    os.chdir(dir)
    response = requests.get(pdf_url)
    with open(pdf_file, 'wb') as pdf:
        pdf.write(response.content)

Path = os.getcwd()
dir_pdf_list = Path + '\pdf_list'
dir_pdf = Path + '\pdf_doc'
pdf_file = 'temporal.pdf'

os.chdir(Path)
if not os.path.exists(dir_pdf):
    os.mkdir(dir_pdf)

os.chdir(dir_pdf_list)
with open('pdf.txt', 'rb') as f:
    pdf_urls = f.readlines()
    os.chdir(dir_pdf)
    for pdf_url in pdf_urls:
        url = str(pdf_url[:-2], 'utf-8')
        generate_pdf(url, pdf_file, dir_pdf)
        pdf_doc = fitz.open(pdf_file)
        txt_file = open(pdf_file+'.txt', 'wb')
        for page in pdf_doc:
            text = page.get_text().encode('utf-8')
            txt_file.write(text) #Sobreescribe el archivo .txt
            #TODO: Guardar el texto en una lista o diccionario
        txt_file.close()
        
        break # para que haga una sola iteracion (solo para prueba)


# Eliminamos el pdf generado
# if os.path.exists(pdf_file):
#     os.remove(pdf_file)
os.chdir(Path)