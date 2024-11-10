import PySimpleGUI as sg
import string
import random

sg.theme('Darkgrey16')

layout = [
    [sg.Column([
        [sg.Text('Adicionar Letras Maiúsculas:',size=(25, 1)), sg.Checkbox(key='maiuscula', text='', default=False, pad=(5, 0))],
        [sg.Text('Adicionar Letras Minúsculas:',size=(25, 1)), sg.Checkbox(key='minuscula', text='', default=False, pad=(5, 0))],
        [sg.Text('Adicionar Caracteres Especiais:',size=(25, 1)), sg.Checkbox(key='especiais', text='', default=False, pad=(5, 0))]
    ], pad=(0, 10))],
    [sg.Text('Tamanho da Senha:')],
    [sg.Slider(key='len_senha', range=(8, 64), default_value=8, orientation='h', size=(27, 10))],
    [sg.Text('')],
    [sg.Text('Senha Gerada')],
    [sg.Multiline(key='output', size=(34, 3),write_only=False,no_scrollbar=True)],
    [sg.Button('Gerar Senha',pad=(10, 10)), sg.Button('Copiar',pad=(10, 10)), sg.Button('Cancelar',pad=(10, 10))]
]
sg.Input()
window = sg.Window('Gerador de Senha', layout=layout)

def gerar_senha(len_senha, add_maiuscula, add_minuscula, add_especial):
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    caracteres_especiais = string.punctuation
    numeros = string.digits

    num_maiuscula = int(len_senha * 0.20)
    num_minuscula = int(len_senha * 0.20)
    num_especiais = int(len_senha * 0.15)
    num_numeros = len_senha - (num_maiuscula + num_minuscula + num_especiais)
    
    senha_gerada = []

    if add_maiuscula:
        senha_gerada.extend(random.choices(letras_maiusculas,k=num_maiuscula))
    if add_minuscula:
        senha_gerada.extend(random.choices(letras_minusculas,k=num_minuscula))
    if add_especial:
        senha_gerada.extend(random.choices(caracteres_especiais,k=num_especiais))

    senha_gerada.extend(random.choices(numeros , k=num_numeros))
        
    random.shuffle(senha_gerada)
    senha = ''.join(senha_gerada) 
    return senha

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break
    elif event == 'Gerar Senha':
        len_senha = int(values['len_senha'])
        add_maiuscula = values['maiuscula']
        add_minuscula = values['minuscula']
        add_especial = values['especiais']

        senha = gerar_senha(len_senha, add_maiuscula, add_minuscula, add_especial)
        window['output'].update(senha)

    elif event == 'Copiar':
        sg.clipboard_set(values['output'])
        sg.popup('Senha copiada para a área de transferência!')
