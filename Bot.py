from threading import local
import pyautogui
import time
import keyboard
import pydirectinput

"""
O tempo no time.sleep, .PAUSE e posição dos cliques são arbitrários, subjetivos a cada pessoa e máquina.
O 'f1' por padrão é a tecla para sair da execução.
"""
pyautogui.PAUSE = 0.5

#Função para encontrar posição no monitor caso seja diferente de 1980x1080p
def printa_posicao():
    time.sleep(2)
    print(pyautogui.position())


def Clicker():
    pydirectinput.PAUSE = 0.01
    while(keyboard.is_pressed('f1') == False):
        pydirectinput.click()


# É necessário o moveTo + click(x,y) devido a um possivel incompatibilidade entre o DirectX(Roblox) e pyautogui/pydirectinput.
# Uma Alternativa que encontrei é antes de usar o click é dar Alt + Tab duas vezes. Além disto caso o jogo verifique os inputs do
# Usuário é bom o usar o numpy("np.random.uniform") para criar um intervalo entre os cliques ou ações.
def BrawOut():
    pydirectinput.PAUSE = 0.2
    while(keyboard.is_pressed('f1') == False):
        # Caso perca conexão com Roblox ele para a execução.
        if(pyautogui.locateOnScreen('Net.png',grayscale=True, confidence=0.8) != None):
            break
        # Caso esteja no modo infinito e necessite clicar no replay.
        if(pyautogui.locateOnScreen('Replay.png',grayscale=True, confidence=0.8) != None):
            pyautogui.moveTo(1144,793)
            pydirectinput.click(1144,793)
            time.sleep(20)
        else:
            pyautogui.moveTo(479,982)
            pydirectinput.click(479,982)
            
            pyautogui.moveTo(669,982)
            pydirectinput.click(669,982)

            pyautogui.moveTo(669,982)
            pydirectinput.click(861,982)

            pyautogui.moveTo(1052,982)
            pydirectinput.click(1052,982)

            pyautogui.moveTo(1252,982)
            pydirectinput.click(1252,982)

            pyautogui.moveTo(1452,982)
            pydirectinput.click(1452,982)

            time.sleep(8)


def Main():
    if(pyautogui.confirm(text='Iniciar o Bot?', title='Bot', buttons=['OK', 'Cancel']) == 'OK'):

        resposta = pyautogui.confirm('Qual funcionalidade você deseja?', buttons =['Clicker', 'BrawOut'])
        time.sleep(3)
        pyautogui.hotkey('alt','tab')
        pydirectinput.doubleClick()

        if(resposta == 'BrawOut'):
            BrawOut()
        elif(resposta == 'Clicker'):
            Clicker()
        
        time.sleep(1)
        pyautogui.alert(text='Bot Terminou com Sucesso', title='Resposta', button='Obrigado pelo Aviso')
        
    else:
        time.sleep(1)
        pyautogui.alert(text='Sem problemas', title='Resposta', button='OK')


Main()