import requests
url = 'https://loterias.caixa.gov.br/Paginas/Download-Resultados.aspx'

r = requests.get(url)

print(r.text)