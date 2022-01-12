from PySimpleGUI import PySimpleGUI as sg
from cadastro import *

#Layout
sg.theme('DarkBlue')
layout = [
    [sg.Text()],
    [sg.Button('VER PESSOAS CADASTRADAS')],
    [sg.Button('  CADASTRAR NOVA PESSOA  ')],
    [sg.Button('        SAIR DO SISTEMA            ')]
]

#Janela
janela = sg.Window('sistema 3.0', layout, size=(400, 300), element_justification='c')

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'VER PESSOAS CADASTRADAS':
        ver()

    if eventos == '  CADASTRAR NOVA PESSOA  ':
        janela_add()

    if eventos == '        SAIR DO SISTEMA            ':
        print('SAINDO DO SISTEMA...')
        janela.close()
        break
