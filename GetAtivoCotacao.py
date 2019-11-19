import os
import authentication
import requests
import json

#inicia
a = authentication



base = a.BASE_COTACAO


def GetAtivo(codtivo):
    intraday = base + '/'+str(codtivo)+'/intraday?size=400&callback=uolfinancecallback0'
    response = requests.get(intraday)
    print(response.text)
 

