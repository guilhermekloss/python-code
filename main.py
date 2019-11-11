import GetArquiveInformation
import os

def main():
    csvObj = GetArquiveInformation.GetInformation('arquivo.csv')
    print(csvObj)
main()