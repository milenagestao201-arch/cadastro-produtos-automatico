# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://d

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("microsoft edge")
pyautogui.press("enter")
time.sleep(3)

# entrar no link 
#print(pyautogui.position())

pyautogui.click(x=660, y=66)
pyautogui.write("site da empresa")
pyautogui.press("enter")
time.sleep(3)
#print(pyautogui.position())
pyautogui.click(x=1038, y=366)
# escrever o seu email
pyautogui.write("email da empresa")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
time.sleep(3)
#print(pyautogui.position())
pyautogui.click(x=1282, y=536) # clicar no botão de login

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)
# Passo 4: Cadastrar um produto
#print(pyautogui.position())
for linha in tabela.index:
    pyautogui.click(x=1087, y=243)
# pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim






