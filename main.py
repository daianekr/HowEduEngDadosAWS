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

df = pd.DataFrame(saida_colunas)
print(df)
