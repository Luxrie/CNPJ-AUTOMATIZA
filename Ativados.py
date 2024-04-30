import re

def verificar_ativo(numero):

    padrao = r'\bATIVA\b'

    if re.search(padrao, numero):
        return True
    else:
        return False

def numeros_ativos_arquivo(nome_arquivo):
    numeros_validos = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                if verificar_ativo(linha):
                    numeros_validos.append(linha.strip())
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    return numeros_validos
