import PySimpleGUI as sg
import string
import random
 
sg.theme('Darkgrey16')
layout = [
   [sg.Text('Adicionar Letras:     ') , sg.Checkbox(key='Adicionar Letras', text='',default = False)] ,
   [sg.Text('Adicionar Números: ') ,sg.Checkbox(key='Adicionar Números', text='',default = False)],
   [sg.Text('Adicionar Especiais:') ,sg.Checkbox(key='Adicionar Especiais', text='',default = False)],
   [sg.Text('')],
   [sg.Text('Password Length')],
   [sg.Slider(key='len_senha',range=(6,64),default_value=6,orientation='h',size=(31.5,10))],
   [sg.Text('')],
   [sg.Text('Senha Gerada')],
   [sg.Input(key='output',size=40)],
   [sg.Text('')],
   [sg.Button('Gerar Senha') ,sg.Text('      '), sg.Button('Copiar'),sg.Text('     '), sg.Button('Cancelar')]
]
 
window = sg.Window('Gerador de Senha', layout=layout )
 
def gerar_senha(len_senha,add_maiuscula,add_minuscula,add_especial):
    letras = string.ascii_uppercase + string.ascii_lowercase
    caracteres_especiais = string.punctuation
 
    senha_gerada = []
 
    for i in range(add_maiuscula):
        senha_gerada.append(random.choice(letras_maiusculas))
 
    for input in range(add_minuscula):
        senha_gerada.append(random.choice(letras_minusculas))
       
    for i in range(add_especial):
        senha_gerada.append(random.choice(caracteres_especiais))
 
 
    while len(senha_gerada) < len_senha:
        senha_gerada.append(str(random.randint(0,9)))
       
    random.shuffle(senha_gerada)
    senha = ''.join(senha_gerada)  
    return senha
 
while True:
    event,values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break
    elif event == 'Gerar Senha':
        len_senha = values['len_senha']
        try:
            if not len_senha.isdigit():
                sg.popup("Favor digite apenas números.")
                continue
            else:
                len_senha = int(values['len_senha'])
                if len_senha < 6:
                    sg.popup("O tamanho da senha deve ter no mínimo 6 digitos. Tente Novamente!")
                    continue      
        except:
            continue
 
        add_maiuscula = int(values['maiuscula'])
        add_minuscula = int(values['minuscula'])
        add_especial  = int(values['especial'])
       
        senha = gerar_senha(len_senha,add_maiuscula,add_minuscula,add_especial)
        window['output'].update(senha)
   
    elif event == 'Copiar':
        sg.clipboard_set(values['output'])
        sg.popup('Senha copiada para a área de transferência!')
