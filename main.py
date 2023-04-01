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
# print(saida_colunas)


# with open('todos_os_resultados.csv', 'w') as arquivo_com_resultados:

#     arquivo_com_resultados.truncate(0)
#     for resultado in list(saida_colunas):
#         dez1 = int(resultado[17:19])
#         dez2 = int(resultado[20:22])
#         dez3 = int(resultado[23:25])
#         dez4 = int(resultado[26:28])
#         dez5 = int(resultado[29:31])
#         dez6 = int(resultado[32:34])
#         dezenas = f'{dez1},{dez2},{dez3},{dez4},{dez5},{dez6}'
#         print(dezenas, file=arquivo_com_resultados)