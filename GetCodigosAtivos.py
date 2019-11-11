import authentication
import requests
import json

#inicia
a = authentication



base = a.BASE_COTACAO
assets = base + '/stock/list?size=10000'

def GetCodigosAtivos():
    response = requests.get(assets)
    retorno = json.loads(response.text)
    retorno = json.dumps(retorno)   
    print (retorno)
    f = open("codativos.json", "w")
    f.write(retorno)
    f.close()



GetCodigosAtivos()