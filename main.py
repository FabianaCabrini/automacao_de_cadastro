#Sistema
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

email = "fakeemail@gmail.com"
senha = "senhadafa"

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=638, y=414)

pyautogui.write(email)
pyautogui.press("tab")

pyautogui.write(senha)
pyautogui.press("tab")

pyautogui.press("enter")

time.sleep(3)


#pip install pandas openpylx (leitura da nossa tabela)
import pandas as pd


#ler as informações da base de dados e armazena na tabela
tabela = pd.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
    # codigo
    pyautogui.click(x=652, y=295)  # Posição da barra de cadastro
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    #preco_unitario
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    #volta para o inicio da tela
    pyautogui.scroll(5000)

