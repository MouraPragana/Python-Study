from operator import truediv
import random  # Biblioteca para valores aleatórios.
import PySimpleGUI as sg  # Interface gráfica.
import os   # Criação de arquivos.
from playsound import playsound  # Reproduzir música.


class PassGen:
    def __init__(self):

        # Layout
        sg.theme('SystemDefaultForReal')
        playsound('secret.mp3', block=False)
        layout = [
            [sg.Text('Site/Software', size=(12, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuário', size=(12, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres', size=(22, 1)), sg.Combo(
                values=list(range(31)), key="total_chars", default_value=1, size=(7, 1), readonly=True)],
            [sg.Multiline(key='output', size=(34, 5),
                          disabled=True, autoscroll=False)],

            [sg.Button('Gerar Senha')]
        ]

        # Declarar janela
        self.janela = sg.Window('Password Generator', layout)

    def Iniciar(self):
        while True:
            event, values = self.janela.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Gerar Senha':
                if self.validar_campos(values):
                    new_password = self.gerar_senha(values['total_chars'])
                    self.salvar_senha(new_password, values)
            self.janela['site'].update('')
            self.janela['usuario'].update('')
            self.janela['site'].SetFocus()

    def validar_campos(self, values):
        if len(values['site'].strip()) and len(values['usuario'].strip()):
            return True
        else:
            self.janela['output'].update(
                "Por favor preencha todos os campos para prosseguir!")
            return False

    def gerar_senha(self, values):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*()_+-='
        chars = random.choices(char_list, k=int(values))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, new_password, values):
        with open('password.txt', 'a', newline='', encoding='utf-8') as file:
            file.write(
                f"site/software: {values['site']}, user: {values['usuario']}, password: {new_password}\n")
        self.janela['output'].update(
            f"Senha gerada \n{new_password}")


gen = PassGen()
gen.Iniciar()
