import re

def remover_letras(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, "r") as f_entrada:
        linhas = f_entrada.readlines()

    cnpj_regex = r"\d{14}"

    linhas_limpas = []
    for linha in linhas:

        linha_sem_caracteres_especiais = re.sub(r'[./-]', '', linha)
        match_cnpj = re.search(cnpj_regex, linha_sem_caracteres_especiais)
        if match_cnpj:

            linhas_limpas.append(match_cnpj.group())

    with open(arquivo_saida, "w") as f_saida:
        f_saida.write("\n".join(linhas_limpas))