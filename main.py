# Passo a passo do Projeto para entender a lógica que devemos seguir

# Passo 1 - Entrar no sistema da empresa
    # # https://dlp.hashtagtreinamentos.com/python/intensivao/login
        
# Passo 2 - Fazer login
# Passo 3 - Importar a base de dados
# Passo 4 - Cadastrar um produto
# Passo 5 - Repetir isso até acabar a base de dados 

# Bibliotecas usadas
import time
import pandas
import pyautogui

# Clicar -> pyautogui.click
# Escrever -> pyautogui.write
# Apertar tecla -> pyautogui.press
# Apertar teclas de atalho -> pyautogui.hotkey

pyautogui.PAUSE = 1

# Executando Passo 1:
    # # Apertar tecla Windows
    # # Digitar o nome do programa
    # # Apertar enter
    # # Digitar link
    # # Apertar enter
    
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
navegador = 'edge'

pyautogui.press('win')
pyautogui.write(navegador)
pyautogui.press('enter')
time.sleep(2)
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(5)

# Execuntando Passo 2:
    # # Clicar na caixa do email
    # # Escrever o email
    # # Passar para a caixa da senha
    # # Digitar a senha
    # # Clicar em Logar

pyautogui.press('tab')
pyautogui.write('testator225@gmail.com')
pyautogui.press('tab')
pyautogui.write('uma senha segura')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(5) 

# Executando Passo 3:
    # # Ler a base de dados
    
baseDeDados = pandas.read_csv('produtos.csv')

# Executando passo 4 e 5:

for linha in baseDeDados.index:

    pyautogui.click(x=397, y=239)
    
    # OBS: Para encontrar a posição do Mouse use a seguinte função:
        # # pyautogui.position(), ela vai fornecer a você a posição exata do Mouse

    #codigo
    pyautogui.write(baseDeDados.loc[linha, 'codigo'])
    pyautogui.press('tab')

    # marca
    pyautogui.write(baseDeDados.loc[linha, 'marca'])
    pyautogui.press('tab')

    # tipo
    pyautogui.write(baseDeDados.loc[linha, 'tipo'])
    pyautogui.press('tab')

    # categoria
    pyautogui.write(str(baseDeDados.loc[linha, 'categoria']))
    pyautogui.press('tab')

    # preco
    pyautogui.write(str(baseDeDados.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    # custo
    pyautogui.write(str(baseDeDados.loc[linha, 'custo']))
    pyautogui.press('tab')

    # obs
    obs = baseDeDados.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')

    # enviar
    pyautogui.press('enter')

    # voltar ao inicio
    pyautogui.scroll(3000)