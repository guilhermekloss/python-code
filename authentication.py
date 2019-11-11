import os
from datetime import datetime
from json import loads
from time import gmtime, mktime, strptime


BASE_COTACAO = 'http://cotacoes.economia.uol.com.br/ws/asset'