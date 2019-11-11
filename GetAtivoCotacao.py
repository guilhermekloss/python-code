from datetime import datetime
from json import loads
from time import gmtime, mktime, strptime
import authentication
import requests
from requests import get
import json

a = authentication
base = a.BASE_COTACAO
assets = base + '/stock/list?size=10000'


# 3 ativos para teste
# assets = {'PETR4.SA': 484, 'CTAX4.SA': 227, 'IGUA3.SA': 364}


def GetCodigosAtivos():
    asset = '729'
    intraday = base + '/'+asset+'/intraday?size=400&callback=uolfinancecallback0'
    print (intraday)
    response = requests.get(intraday)
    retorno = json.loads(response.text)
    retorno = json.dumps(retorno)   
    print (response)



GetCodigosAtivos()
