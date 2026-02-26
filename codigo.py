# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 3

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(4)
    

# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click()
# escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.click() # clique no botao de login
import pandas as pd

time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd


tabela = pd.read_csv("produtos.csv")

