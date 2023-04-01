from requests import get, exceptions
from bs4 import BeautifulSoup as sp
from operator import itemgetter
import pandas as pd


url = 'https://asloterias.com.br/lista-de-resultados-da-mega-sena'

carregaurl = get(url, stream=True)

saida_colunas = []
for linhas_tr in sp(carregaurl.content, "lxml")\
    .findAll("div", class_="limpar_flutuacao"):
     saida_colunas.append(linhas_tr.previous_sibling)

# print(saida_colunas)

saida_colunas = [w.replace(' - ', '') for w in saida_colunas]

df = pd.DataFrame(saida_colunas)

df.rename(columns = {0: 'valores'}, inplace=True)
df['Data'] = df['valores'].str[:10]


df['Dezenas'] = df['valores'].str[11:28]

df = df.drop(columns=['valores'])
df.to_csv('dataframe_megasena.csv', index=True)