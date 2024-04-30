def remover_palavra_ativa(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r') as f_in, open(arquivo_saida, 'w') as f_out:
        for linha in f_in:
            if 'ATIVA' in linha:
                nova_linha = linha.replace('ATIVA', '').replace(':', '').strip()
                if nova_linha:
                    f_out.write(nova_linha + '\n')
            else:
                f_out.write(linha)