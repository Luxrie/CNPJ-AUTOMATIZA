import requests
import time
import re

def consultar_dados_cnpj(cnpj):
    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
    response = requests.get(url)
    data = response.json()
    if data is None:
        print("Erro: Nenhum dado retornado para o CNPJ:", cnpj)
    return data.get('nome', ''), data  # Retorna o nome da empresa e o JSON completo dos dados



def obter_donos_e_telefone_empresa(cnpj):
    while True:
        nome_empresa, data = consultar_dados_cnpj(cnpj)
        if 'error' not in data:
            donos = []
            for dono in data.get('qsa', []):  # Itera sobre os proprietários
                if 'nome' in dono:
                    donos.append(dono['nome'])
                else:
                    donos.append("Nome do proprietário não encontrado")
            telefone = data.get('telefone', 'Telefone não encontrado')
            return nome_empresa, donos, telefone
        else:
            return "Empresa não encontrada", ["CNPJ inválido ou não encontrado."], "Telefone não encontrado"
        time.sleep(3)

