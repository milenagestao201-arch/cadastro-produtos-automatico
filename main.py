import pyautogui
import pandas as pd
import time

# ============================================
# CONFIGURAÇÕES DO ROBÔ
# ============================================
pyautogui.PAUSE = 0.5

URL_LOGIN = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
EMAIL = "pythonimpressionador@gmail.com"
SENHA = "sua_senha"  # substitua pela senha da aula
ARQUIVO_CSV = "produtos.csv"

# ============================================
# PASSO 1: ABRIR NAVEGADOR
# ============================================
pyautogui.press("win")
pyautogui.write("microsoft edge")
pyautogui.press("enter")
time.sleep(4)

# ============================================
# PASSO 2: ENTRAR NO SISTEMA E FAZER LOGIN
# ============================================
pyautogui.click(x=660, y=66)
pyautogui.write(URL_LOGIN)
pyautogui.press("enter")
time.sleep(4)

pyautogui.click(x=1038, y=366)
pyautogui.write(EMAIL)
pyautogui.press("tab")
pyautogui.write(SENHA)
time.sleep(3)
pyautogui.click(x=1282, y=536)
time.sleep(3)

# ============================================
# PASSO 3: LER ARQUIVO DE PRODUTOS
# ============================================
tabela = pd.read_csv(ARQUIVO_CSV)
print(tabela)

# ============================================
# PASSO 4: CADASTRAR PRODUTOS AUTOMATICAMENTE
# ============================================
for linha in tabela.index:
    pyautogui.click(x=1087, y=243)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
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
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)