import requests
import time

def consultar_cnpj(cnpj):
    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
    response = requests.get(url)
    data = response.json()
    return data


def verificar_status(cnpj):
    while True:
        try:
            data = consultar_cnpj(cnpj)
            situacao = data.get('situacao', None)
            if situacao:
                return situacao
            else:
                return "CNPJ inválido ou não encontrado."
            time.sleep(3)
        except requests.exceptions.RequestException:
            print("PAUSA de 60 Segundos")
            time.sleep(60)



def Arquivocolocar(arquivo_saida, arquivo_saida2):
    with open(arquivo_saida, 'r') as file:
        cnpjs = file.readlines()

    linhas_limpas = []
    for cnpj in cnpjs:
        cnpj = cnpj.strip()
        status = verificar_status(cnpj)
        print(f'O CNPJ {cnpj} está {status}.')
        linhas_limpas.append(f'{cnpj}: {status}')
        time.sleep(3)

    with open(arquivo_saida2, 'w') as file2:
        for linha in linhas_limpas:
            file2.write(linha + '\n')