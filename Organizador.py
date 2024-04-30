import re

def organizar_numeros_telefone(lista_informacoes):
    for i, info in enumerate(lista_informacoes):
        if info.startswith("Número de Telefone da Empresa:"):
            numeros_telefone = re.findall(r'\(\d+\) \d+-\d+', info)
            numeros_telefone_formatados = ["+55" + re.sub(r'\D', '', num) for num in numeros_telefone]
            lista_informacoes[i] = "Número de Telefone da Empresa: " + " / ".join(numeros_telefone_formatados)
    return lista_informacoes
