import requests
from bs4 import BeautifulSoup

def obterDezenasMegaSena():
    try:
        req = requests.get( "http://loterias.caixa.gov.br/wps/portal/loterias")
        soup = BeautifulSoup( req.content, "html.parser" )
        ul = soup.findAll( "ul", class_="resultado-loteria mega-sena" )
        return [ int(li.text) for li in ul[0].findAll( "li" ) ]
    except:
        return None

print(obterDezenasMegaSena())