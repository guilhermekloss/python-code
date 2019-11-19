import authentication
import requests
import json
import GetAtivoCotacao

#inicia
a = authentication



base = a.BASE_COTACAO
assets = base + '/stock/list?size=10000'

def GetCodigosAtivos():
    response = requests.get(assets)
    retorno = json.loads(response.text)
    
    for element in retorno["data"]:
        companyAbvName = element["companyAbvName"]
        idt = element["idt"]
        code = element["code"]
        name = element["name"]
        companyName = element["companyName"]
        
        GetAtivoCotacao.GetAtivo(idt)
        

        print(companyAbvName,idt,code,name,companyName)


    retorno = json.dumps(retorno, sort_keys=True, indent=4)
 

    #print (retorno)
    
    f = open("codativos.json", "w")
    f.write(retorno)
    f.close()




GetCodigosAtivos()