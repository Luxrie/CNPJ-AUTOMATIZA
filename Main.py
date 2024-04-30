import time
from urllib.parse import quote
import webbrowser
import time
import openpyxl
import pyautogui
import random

arquivo = openpyxl.load_workbook(input("Digite o nome do arquivo: "))
paginas_empresas = arquivo['Sheet1']

# Saudações informais
saudacoes_informais = [
    "Oi, tudo bem?",
    "Olá, como vai?",
    "Oi, tudo certo?",
    "Oi, como você está?"
]

# Saudações aleatórias
input("Aperte enter caso já logado no whatsapp web")
time.sleep(5)

# Loop para enviar mensagens para todos os contatos
for linha in paginas_empresas.iter_rows(min_row=2):
    empresa_nome = linha[0].value
    # Verifica se o número de telefone está vazio
    if linha[2].value is None or linha[2].value == "":
        print(f"Número de telefone vazio encontrado para a empresa {empresa_nome}. Passando para próxima linha.")
        continue  # Passa para a próxima iteração do loop

    contatos = str(linha[2].value).split('/')  # Convertendo para string e dividindo os contatos separados por '/'
    saudacao_informal = random.choice(saudacoes_informais)  # Escolhe uma saudação informal aleatoriamente
    mensagem_fixa = f"Meu nome é Saul Martins, sou executivo de contas do Grupo Arpini & Araújo Assessoria Empresarial ⚖ — Inteligência Tributária. Responsáveis por trazer empresas para a regularidade fiscal. Falo com o responsável pela empresa? *Seria para tratar de um assunto tributário da empresa {empresa_nome}.* Aguardo sua resposta. Obrigado!"
    for contato in contatos:
        contato = contato.strip()  # Removendo espaços em branco em excesso
        mensagem1 = f'https://web.whatsapp.com/send?phone={contato}&text={quote(saudacao_informal)}'
        mensagem2 = f'https://web.whatsapp.com/send?phone={contato}&text={quote(mensagem_fixa)}'
        webbrowser.open(mensagem1)
        try:
            time.sleep(25)
            setinha = pyautogui.locateCenterOnScreen('SETINHA.png')
            time.sleep(5)
            pyautogui.click(setinha[0], setinha[1])
            time.sleep(5)
            pyautogui.hotkey('ctrl','w')
            time.sleep(8)
        except:
            print(f'Não foi possível enviar mensagem para a empresa {empresa_nome}')
            time.sleep(5)
        try:
            webbrowser.open(mensagem2)
            time.sleep(25)
            setinha = pyautogui.locateCenterOnScreen('SETINHA.png')
            time.sleep(5)
            pyautogui.click(setinha[0], setinha[1])
            time.sleep(5)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(40)
        except:
            print(f'Não foi possível enviar mensagem para a empresa {empresa_nome}')
            time.sleep(5)
